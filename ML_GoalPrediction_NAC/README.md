# Football Player Analytics & Machine Learning

A comprehensive data science project analyzing football player statistics using machine learning to predict goal-scoring potential and optimize player recruitment strategies.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-success.svg)

## 📋 Project Overview

This project demonstrates end-to-end data science workflow applied to football analytics, developed as part of a player recruitment optimization initiative for NAC Breda. The analysis combines exploratory data analysis, machine learning, and custom algorithm implementations to predict player performance and inform recruitment decisions.

### Key Features

- **Comprehensive Data Analysis**: Analysis of 16,535 player records across 114 performance metrics
- **Machine Learning Models**: Implementation of 6+ ML algorithms including Gradient Boosting, Random Forest, SVM, and K-Means
- **Custom Implementations**: Gradient descent optimization built from scratch
- **Data Visualization**: 10+ interactive visualizations exploring player performance patterns
- **Ethical Framework**: GDPR-compliant data handling with comprehensive ethical considerations

### Business Impact

- Developed predictive model with 95%+ accuracy for goal-scoring potential
- Reduced player evaluation time from manual scouting to data-driven insights
- Created framework for identifying undervalued talent in the transfer market

## 🗂️ Repository Structure

```
football-analytics/
│
├── Football_Analytics_Portfolio.ipynb    # Main analysis notebook
├── combined_data.csv                      # Player statistics dataset
├── NAC_Player_Recruitment_Report.pdf     # Detailed project report
├── README.md                              # This file
└── requirements.txt                       # Python dependencies
```

## 📊 Dataset

The dataset contains comprehensive football player statistics including:

- **16,535 players** from multiple leagues and teams
- **114 features** covering offensive, defensive, and passing metrics
- Key metrics: Goals, xG, Assists, Market Value, Passing Accuracy, Duels Won%, etc.

### Data Sources
- Combined from 45 unique data files
- Anonymized player performance data
- Time period: Multiple seasons

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Anaconda (recommended) or pip
- Jupyter Notebook/Lab

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/football-analytics.git
cd football-analytics
```

2. **Create and activate conda environment**
```bash
conda create -n football_analytics python=3.9
conda activate football_analytics
```

3. **Install dependencies**
```bash
# Core packages
conda install pandas numpy matplotlib seaborn scikit-learn scipy

# Jupyter support
conda install jupyter ipykernel

# Additional packages
conda install sympy requests
pip install mysql-connector-python missingno
```

4. **Register environment with Jupyter**
```bash
python -m ipykernel install --user --name=football_analytics --display-name="Python (Football Analytics)"
```

5. **Launch Jupyter**
```bash
jupyter notebook Football_Analytics_Portfolio.ipynb
```

### Alternative: Using requirements.txt

```bash
pip install -r requirements.txt
```

## 📓 Notebook Structure

The Jupyter notebook is organized into the following sections:

1. **Setup & Data Import** - Library imports and dataset loading
2. **Data Cleaning** - Handling missing values, duplicates, and outliers
3. **Exploratory Data Analysis** - Statistical analysis and key insights
4. **Data Visualizations** - Interactive plots and correlation analysis
5. **Machine Learning Models** - Multiple model implementations
6. **Model Optimization** - Hyperparameter tuning and feature selection
7. **Custom Implementations** - Gradient descent from scratch
8. **Results & Conclusions** - Key findings and recommendations

## 🔍 Key Findings

### Data Insights
- Player market value peaks between ages 25-28
- Strong correlation (0.85+) between xG and actual goals scored
- Position significantly impacts performance metrics
- Forward positions show 3x higher goals per 90 minutes than midfielders

### Model Performance
- **Best Model**: Gradient Boosting Classifier
- **Accuracy**: 95.3% on test set
- **F1-Score**: 0.94 (weighted average)
- **Key Predictors**: xG, Shots per 90, Age, Position, Matches Played

### Business Recommendations
1. Prioritize players aged 23-27 for optimal value-performance ratio
2. Focus on xG metrics for goal-scoring potential assessment
3. Implement data-driven scouting in undervalued markets
4. Combine ML predictions with traditional scouting for best results

## 🛠️ Technologies Used

**Languages & Tools**
- Python 3.9+
- Jupyter Notebook

**Data Analysis**
- pandas, numpy
- matplotlib, seaborn
- scipy, sympy

**Machine Learning**
- scikit-learn (multiple algorithms)
- Custom gradient descent implementation

**Additional Tools**
- MySQL (database operations)
- RESTful APIs (data integration)

## 📈 Model Comparison

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Gradient Boosting | 95.3% | 94.8% | 95.1% | 94.9% |
| Random Forest | 93.7% | 93.2% | 94.8% | 93.9% |
| SVM | 92.8% | 95.1% | 91.2% | 93.1% |
| Logistic Regression | 91.4% | 91.8% | 90.9% | 91.3% |

## 📄 Project Report

A detailed 15-page report is included (`NAC_Player_Recruitment_Report.pdf`) covering:
- Problem statement and objectives
- Data analysis methodology
- Machine learning approach
- Ethical considerations (GDPR compliance)
- Recommendations for implementation

## 🔮 Future Improvements

- [ ] Implement deep learning models (LSTM for time-series analysis)
- [ ] Add real-time data integration via APIs
- [ ] Create interactive dashboard (Streamlit/Dash)
- [ ] Incorporate injury prediction models
- [ ] Expand to team formation optimization
- [ ] Deploy as REST API for production use

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👤 Author

**Anastasiia Mokhonko**

## 🙏 Acknowledgments

- NAC Breda for providing the project context
- Breda University of Applied Sciences (BUas)
- Football analytics community for inspiration

---

**Note**: This project was developed as part of academic work in Data Science & Artificial Intelligence. The dataset has been anonymized and no proprietary information is included.

*Last Updated: January 2024*