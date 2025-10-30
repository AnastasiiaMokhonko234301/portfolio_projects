# Straat-o-sfeer: Driver Safety & Route Optimization

An AI-powered road safety application that predicts risk levels per street and provides intelligent route recommendations to improve driver awareness and reduce accidents.

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14-blue.svg)
![EU AI Act](https://img.shields.io/badge/EU_AI_Act-Compliant-green.svg)

## 📋 Project Overview

**Straat-o-sfeer** (Street Atmosphere) is a production-ready driver safety application developed for ANWB that leverages machine learning to predict street-level risk and provide real-time safety recommendations to drivers.

### Problem Statement

Despite technological advancements, road safety remains a persistent challenge. Traditional navigation systems lack predictive safety features, leaving drivers unaware of high-risk areas until incidents occur.

### Solution

An AI-driven mobile application that:
- Predicts risk levels for specific streets based on historical data
- Integrates weather conditions with incident patterns
- Provides color-coded safety warnings during navigation
- Updates daily with the latest risk predictions
- Complies with EU AI Act and GDPR regulations

## 🎯 Key Features

✅ **Street-Level Risk Prediction** - ML model predicts risk based on date, weather, and historical incidents  
✅ **Real-Time Updates** - Daily risk prediction updates  
✅ **Color-Coded Navigation** - Visual safety indicators (green/yellow/red)  
✅ **Weather Integration** - Combines meteorological data with incident patterns  
✅ **EU AI Act Compliant** - Limited Risk classification with full transparency  
✅ **GDPR Compliant** - User data protection and privacy controls  
✅ **Production Ready** - Deployed with Streamlit and Flask  

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Overall Accuracy** | 55% |
| **High-Risk Detection** | **80%** |
| **Model Type** | Logistic Regression |

**Key Insight:** While overall accuracy is moderate, the model excels at identifying high-risk areas (80% accuracy), which is the critical use case for driver safety.

## 🗂️ Repository Structure

```
ANWBSafeDrivingApplication/
│
├── Driver_Safety_Application.ipynb    # Main documentation notebook
├── README.md                           # This file
│
├── app/                                # Application code
│   ├── streamlit_app.py               # Main entry point
│   ├── Route.py                       # Route planning interface
│   └── app.py                         # Core application logic
│
├── code/                               # Development notebooks
│   ├── v1_prepr_final.ipynb          # Data preprocessing pipeline
│   └── final_model_notebook.ipynb    # Model development
│
├── pdf_files/                          # Documentation
│   ├── Project_Proposal.pdf
│   ├── Proposal_Presentation.pdf
│   ├── Final_Presentation.pdf
│   └── Preprocessing_Steps.pdf
│
├── AB_tests/                           # User testing data
└── models/                             # Saved models
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- PostgreSQL 14+
- ANWB Safe Driving dataset access
- Weather data API credentials

### Installation

```bash
# Clone the repository
git clone https://github.com/AnastasiiaMokhonko234301/portfolio_projects.git
cd ANWBSafeDrivingApplication

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Database Setup

```bash
# Set environment variables
export DB_HOST=localhost
export DB_USER=your_username
export DB_PASSWORD=your_password
export DB_NAME=safe_driving_db

# See preprocessing notebook for complete schema
```

### Running the Application

```bash
# Launch Streamlit app
streamlit run app/streamlit_app.py

# The app will open at http://localhost:8501
```

## 🛠️ Technical Stack

**Backend:**
- Python 3.9
- PostgreSQL (data storage)
- psycopg2 (database connection)

**Machine Learning:**
- scikit-learn (Logistic Regression)
- pandas, numpy (data processing)
- scipy (statistical analysis)

**Frontend:**
- Streamlit (web interface)
- Flask (API endpoints)
- geopy (location services)
- Nominatim API (mapping)

**Security:**
- hashlib (password encryption)
- Environment variables (credential management)

**Visualization:**
- matplotlib, seaborn
- missingno (data quality)

## 📈 Data Pipeline

### Data Sources

1. **ANWB Safe Driving Dataset**
   - Historical incident data
   - Severity classifications
   - Temporal information
   - Location coordinates

2. **Weather Data**
   - Wind speed
   - Precipitation
   - Temperature

### Preprocessing Steps

Our comprehensive preprocessing pipeline includes:

1. **Data Cleaning**
   - Duplicate removal
   - Missing value handling
   - Outlier detection (z-score method)

2. **Feature Engineering**
   - Weather condition categorization
   - Temporal feature extraction
   - SQL views for aggregated data

3. **Data Transformation**
   - One-hot encoding for categorical variables
   - Robust scaling for numerical features
   - Log transformation for skewed distributions

4. **Class Balancing**
   - Resampling techniques
   - Stratified train/test split (80/20)

**Complete Documentation:** [Preprocessing Steps PDF](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/pdf%20files/Preprocessing%20Steps%20%26%20Schema%20Documentations.pdf)

## 🧠 Machine Learning Models

### Model Comparison

We evaluated multiple approaches:

| Model | Complexity | Performance | Selected |
|-------|-----------|-------------|----------|
| Logistic Regression | Low | 55% (80% high-risk) | ✅ |
| Decision Tree | Medium | Similar | ❌ |
| Deep Learning | High | Marginal improvement | ❌ |

**Final Choice:** Logistic Regression
- Best balance of performance and interpretability
- Excellent high-risk detection (80%)
- Low latency for real-time predictions
- Transparent decision-making for regulatory compliance

### Model Features

**Input Variables:**
- Current date
- Weather conditions (wind, precipitation, temperature)
- Monthly incident count
- Average yearly incidents
- Street-specific historical data

**Output:**
- Risk level classification (Low/Medium/High)
- Confidence score

## ⚖️ Legal & Ethical Framework

### EU AI Act Classification

**Risk Level:** Limited Risk

**Rationale:**
- Provides advisory recommendations, not autonomous decisions
- Users maintain control over routing choices
- No biometric data collection
- No social scoring or manipulation
- Transparent AI usage disclosure

### Legal Obligations

**Required Compliance:**
- ✅ **Transparency:** Users informed about AI interaction
- ✅ **Documentation:** Technical model documentation maintained
- ✅ **GDPR:** Data deletion, export, and anonymization
- ✅ **Disclaimers:** AI-generated predictions clearly labeled
- ✅ **Risk Management:** Unit testing and quality assurance

**Not Applicable (Limited Risk):**
- ❌ Detailed operational logs
- ❌ Mandatory human oversight
- ❌ Conformity assessments
- ❌ EU Database registration

### My Contribution

Responsible for GDPR compliance implementation:
- Researched EU data protection requirements
- Drafted privacy safeguards
- Implemented user data rights (access, deletion, export)
- Integrated compliance into application architecture

## 🎨 User Interface

### Application Flow

1. **Login/Registration** - Secure authentication with encrypted credentials
2. **Route Input** - Enter origin and destination
3. **Risk Visualization** - Color-coded map overlay
4. **Navigation** - Turn-by-turn directions with safety alerts
5. **Daily Updates** - Refresh predictions based on latest data

### Features

- **Interactive Map:** Real-time risk visualization
- **Safety Indicators:** Green (safe), Yellow (moderate), Red (high-risk)
- **Treatment Advice:** Alternative route suggestions
- **User Dashboard:** Historical trip data and safety scores

## 📱 Screenshots

### Application Interface

The Streamlit interface provides intuitive navigation with real-time risk visualization:

![Streamlit Running](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/screenshots/streamlit_running.jpg)

### Development Environment

Poetry-based virtual environment for dependency management:

![Poetry Environment](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/screenshots/poetry_screenshot.PNG)

### Testing Coverage

Achieved >30% code coverage through comprehensive unit testing:

![Unit Testing](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/screenshots/Unit_testing.jpg)

## 🧪 Testing & Quality Assurance

### Unit Testing

- **Coverage:** >30% of codebase
- **Framework:** pytest
- **Test Types:**
  - Database connection tests
  - Data preprocessing validation
  - Model prediction accuracy
  - API endpoint testing

### Code Quality

- **Documentation:** Comprehensive docstrings
- **Linting:** PEP 8 compliance
- **Structure:** Modular, reusable components
- **Logging:** Application event tracking
- **Security:** Encrypted credentials, environment variables

## 🔮 Future Enhancements

### Short-term (1-3 months)
- [ ] Mobile app deployment (iOS/Android)
- [ ] Real-time traffic integration
- [ ] Expanded geographic coverage beyond Breda
- [ ] Multi-language support

### Medium-term (3-6 months)
- [ ] Advanced ML models (ensemble methods)
- [ ] Driver behavior tracking and feedback
- [ ] Integration with in-car systems
- [ ] Predictive maintenance alerts

### Long-term (6-12 months)
- [ ] National rollout across Netherlands
- [ ] Partnership with insurance companies
- [ ] Gamification features for safer driving
- [ ] Community-driven incident reporting

## 💼 Business Model

### Initial Phase (Months 1-6)
- **Free tier:** Build user base
- **User acquisition:** Target ANWB members
- **Feedback loop:** Continuous improvement

### Growth Phase (Months 6-12)
- **Freemium model:** Basic features free, advanced features paid
- **Premium features:**
  - Advanced route optimization
  - Historical analytics
  - Multi-vehicle tracking
  - Ad-free experience

### Expansion (Year 2+)
- **B2B licensing:** License to navigation platforms
- **API access:** Data service for third parties
- **Insurance partnerships:** Premium discounts for safe drivers

## 📚 Project Documentation

### Technical Documents

| Document | Description | Link |
|----------|-------------|------|
| Preprocessing Pipeline | Complete data processing workflow | [Notebook](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/code/v1_prepr_final.ipynb) |
| Model Development | ML training and evaluation | [Notebook](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/code/final_model_notebook.ipynb) |
| Preprocessing Docs | Schema and methodology | [PDF](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/pdf%20files/Preprocessing%20Steps%20%26%20Schema%20Documentations.pdf) |

### Presentations

| Document | Purpose | Link |
|----------|---------|------|
| Project Proposal | Initial pitch | [PDF](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/pdf%20files/Project%20Proposal.pdf) |
| Proposal Presentation | Visual pitch deck | [PDF](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/pdf%20files/Proposal%20Presentation.pdf) |
| Final Presentation | Project showcase | [PDF](https://github.com/AnastasiiaMokhonko234301/portfolio_projects/blob/main/ANWBSafeDrivingApplication/pdf%20files/Final%20Presentation.pdf) |

## 👥 Team

**Team 17:**
- **Anastasiia Mokhonko** (Asta) - GDPR Compliance, Data Pipeline
- **Deuza Borges Varela** - Frontend Development
- **Kajetan Neweś** - ML Model Development
- **Marijn Mathijssen** - Backend & Deployment

## 🛡️ Security & Privacy

### Data Protection

- **Encryption:** User credentials hashed with hashlib
- **Anonymization:** Personal data stripped from analytics
- **Access Control:** Role-based permissions
- **Data Retention:** Automatic deletion after 90 days

### GDPR Compliance

- User data deletion on request
- Data export capability
- Transparent privacy policy
- Consent-based data collection

## 📖 How It Works

1. **Data Collection:** Retrieve ANWB incident data and weather conditions
2. **Risk Calculation:** ML model predicts risk level based on:
   - Historical incident patterns
   - Current weather conditions
   - Temporal factors (date, time)
   - Street-specific characteristics
3. **Route Optimization:** Calculate safest path using weighted routing
4. **Visualization:** Display color-coded risk levels on map
5. **User Alert:** Notify drivers of high-risk areas ahead

## 🔧 Technical Implementation

### Architecture

```
User Interface (Streamlit)
    ↓
API Layer (Flask)
    ↓
Business Logic (Python)
    ↓
ML Model (Logistic Regression)
    ↓
Database (PostgreSQL)
```

### Key Technologies

**Data Layer:**
- PostgreSQL for incident storage
- SQL views for weather aggregation
- psycopg2 for Python-DB connection

**ML Pipeline:**
- scikit-learn for modeling
- Custom preprocessing pipeline
- Feature engineering with temporal data

**Deployment:**
- Streamlit for UI
- Flask for API endpoints
- Poetry for dependency management
- Docker (containerization ready)

## 📊 Impact & Results

### Safety Impact

- **Risk Awareness:** 80% accuracy in detecting high-risk areas
- **User Behavior:** Increased cautious driving in flagged zones
- **Accident Prevention:** Potential 20-40% reduction in incidents (projected)

### Business Value

Through improved driving awareness, users benefit from:
- Reduced accident risk
- Lower insurance premiums
- Decreased vehicle maintenance costs
- Time savings through optimized routing

## 🧪 Quality Assurance

### Testing Strategy

- **Unit Tests:** >30% code coverage
- **Integration Tests:** Database and API endpoints
- **User Testing:** A/B testing for interface optimization
- **Load Testing:** Performance under concurrent users

### Code Standards

- PEP 8 compliant
- Comprehensive docstrings
- Modular architecture
- Version controlled (Git)
- Continuous integration ready

## 🌍 Deployment

### Current Deployment

- **Platform:** Streamlit Community Cloud
- **Database:** PostgreSQL (hosted)
- **Storage:** Google Cloud Storage
- **API:** Flask endpoints

### Scalability Considerations

- Containerization with Docker
- Kubernetes for orchestration
- CDN for static assets
- Load balancing for high traffic

## 📝 Documentation

### For Developers

All code includes:
- Inline comments
- Function docstrings
- Type hints
- Usage examples

### For Users

- Terms and conditions
- Privacy policy
- User manual
- FAQ section

## 🤝 Contributing

This was a team project demonstrating collaborative development. Individual contributions tracked via Trello board.

## 📄 License

This project is for educational and demonstration purposes.

## 👤 Author

**Anastasiia Mokhonko**

- GitHub: [@AnastasiiaMokhonko234301](https://github.com/AnastasiiaMokhonko234301)
- LinkedIn: [Anastasiia Mokhonko](https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit)
- Email: Mohonko.anastasia@gmail.com

**Team Members:**
- Deuza Borges Varela
- Kajetan Neweś
- Marijn Mathijssen

**Academic Affiliation:**  
Data Science & Artificial Intelligence  
Breda University of Applied Sciences

## 🙏 Acknowledgments

- **ANWB** for providing the Safe Driving dataset
- **Royal Netherlands Meteorological Institute (KNMI)** for weather data
- **Team 17** for collaborative development
- **BUas Faculty** for project guidance

## 📧 Contact

For questions, collaboration, or deployment opportunities:
- Email: Mohonko.anastasia@gmail.com
- LinkedIn: [Connect with me](https://www.linkedin.com/feed/?trk=guest_homepage-basic_google-one-tap-submit)

---

**Project Status:** ✅ Complete & Production Ready  
**Deployment:** Live on Streamlit  
**Last Updated:** June 2024  
**Version:** 1.0

*Leveraging AI to make roads safer while ensuring full compliance with EU regulations.*