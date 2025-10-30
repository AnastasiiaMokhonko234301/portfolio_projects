import streamlit as st
import folium
from streamlit_folium import st_folium
import osmnx as ox
import networkx as nx
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError, GeopyError
import joblib
import os
import pandas as pd
from datetime import datetime
from collections import defaultdict

# Set page configuration for mobile-like layout
st.set_page_config(layout="centered")

# Initialize geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Determine the absolute path to model.joblib
model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log_model.joblib")

# Load your pre-trained model
@st.cache_resource
def load_model():
    if os.path.exists(model_path):
        return joblib.load(model_path)
    else:
        st.error(f"Error: log_model.joblib not found at {model_path}. Please check the file path.")
        return None

model = load_model()

# Load your data
@st.cache_data
def load_csv():
    return pd.read_csv('model_data.csv')

df = load_csv()

if st.button('Update Predictions'):
    # Get current date
    current_date = datetime.now()
    # Extract month and day
    month = current_date.month
    day = current_date.day
    # Filter dataframe for current month and day
    X = df[(df['month'] == month) & (df['day'] == day)]
    # Select the same columns used for training
    X = X[['month', 'day', 'most_common_condition', 'avg_yearly_accidents', 'average_monthly_occurrences']]
    # Make prediction
    prediction = model.predict(X)
    # Apply prediction to the column that is being predicted in the original DataFrame
    df.loc[X.index, 'Risk Level'] = prediction
    # Display confirmation
    st.write('Predictions Updated')

# Function to geocode an address
@st.cache_data
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        return location
    except GeocoderTimedOut:
        st.error("Error: Geocoding timed out. Please retry.")
        return None
    except (GeocoderServiceError, GeopyError) as e:
        st.error(f"Error: {e}. Please try again later or check your internet connection.")
        return None

# Function to create route map
@st.cache_data
def create_route_map(start_address, end_address):
    try:
        # Geocode addresses to coordinates
        start_location = geocode_address(start_address)
        end_location = geocode_address(end_address)

        if start_location and end_location:
            # Extract coordinates
            start_coords = (start_location.latitude, start_location.longitude)
            end_coords = (end_location.latitude, end_location.longitude)

            # Create a graph from OpenStreetMap data
            G = ox.graph_from_place('Breda, Netherlands', network_type='drive')

            # Find the nearest nodes to the start and end points
            start_node = ox.distance.nearest_nodes(G, X=start_coords[1], Y=start_coords[0])
            end_node = ox.distance.nearest_nodes(G, X=end_coords[1], Y=end_coords[0])

            # Find the shortest path between the nodes
            route = nx.shortest_path(G, start_node, end_node, weight='length')
            route_coords = [(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]

            # Create a map centered at the midpoint between the start and end points
            midpoint = [(start_coords[0] + end_coords[0]) / 2, (start_coords[1] + end_coords[1]) / 2]
            route_map = folium.Map(location=midpoint, zoom_start=13)

            road_segments = defaultdict(lambda: {'coords': [], 'length': 0})

            # Collect road segments
            for i in range(len(route) - 1):
                node1 = route[i]
                node2 = route[i + 1]
                edge_data = G[node1][node2][0]
                road_name = edge_data.get('name', 'Unnamed Road')
                length = edge_data.get('length', 0)

                if isinstance(road_name, str):
                    road_segments[road_name]['coords'].append(((G.nodes[node1]['y'], G.nodes[node1]['x']),
                                                               (G.nodes[node2]['y'], G.nodes[node2]['x'])))
                    road_segments[road_name]['length'] += length

            total_length = 0

            # Add road segments to the map and display information
            for road_name, segment_data in road_segments.items():
                coords = segment_data['coords']
                length = segment_data['length']
                total_length += length

                if not df[df['road_name'] == road_name].empty:
                    risk_level = df[df['road_name'] == road_name]['Risk Level'].values[0]
                else:
                    risk_level = '0'  # Default risk level

                # Define color based on risk level
                if risk_level == '3':
                    color = "red"
                elif risk_level == '2':
                    color = "orange"
                elif risk_level == '1':
                    color = 'yellow'
                else:
                    color = "green"

                # Display road name, risk level, and length
                st.write(f"Road Name: {road_name}, Risk Level: {risk_level}, Length: {length:.2f} meters")

                # Add road segment to the map with color representation
                for segment in coords:
                    folium.PolyLine([segment[0], segment[1]], color=color, weight=3).add_to(route_map)

            # Add markers for start and end points
            folium.Marker(route_coords[0], popup="Start", icon=folium.Icon(color="green")).add_to(route_map)
            folium.Marker(route_coords[-1], popup="End", icon=folium.Icon(color="red")).add_to(route_map)

            # Display total road length
            st.write(f"Total Route Length: {total_length / 1000:.2f} km")

            return route_map, route_coords

        else:
            st.error("Error geocoding addresses. Please check the addresses and try again.")

    except (GeocoderTimedOut, GeocoderServiceError, GeopyError) as e:
        st.error(f"Error: {e}. Please try again later or check your internet connection.")

    return None, None

# Main Streamlit application
def main():
    st.title("Route Navigation and Model Prediction")

    # Sidebar for user input
    start_address = st.text_input("Enter Starting Address:", "Breda")
    end_address = st.text_input("Enter Ending Address:", "Breda University of Applied Sciences")

    # Display the route map
    route_map, route_coords = create_route_map(start_address, end_address)

    if route_map:
        st.subheader("Route Map:")
        st_folium(route_map, width=600, height=500)

        # Display route information
        if 'G' in globals():  # Check if G is defined in the global scope
            route_distance = sum(ox.utils_graph.get_route_edge_attributes(G, route_coords, 'length')) / 1000  # in km
            route_info = f"Approx. Distance: {route_distance:.2f} km"
            st.markdown(f"<h3 style='text-align: center;'>{route_info}</h3>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
