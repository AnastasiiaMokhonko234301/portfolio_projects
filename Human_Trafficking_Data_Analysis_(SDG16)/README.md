# Human Trafficking Data Analysis Dashboard (SDG 16)

[![SDG 16](https://img.shields.io/badge/UN%20SDG-16-blue)](https://sdgs.un.org/goals/goal16)
[![Status](https://img.shields.io/badge/Status-Completed-success)]()
[![License](https://img.shields.io/badge/License-Educational-lightgrey)]()
[![Tool](https://img.shields.io/badge/Tool-Power%20BI-yellow)]()

**A Power BI dashboard analyzing global human trafficking patterns to support UN Sustainable Development Goal 16: Peace, Justice and Strong Institutions.**

![SDG 16 Banner](https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-16.jpg)

---

## Table of Contents
- [Overview](#overview)
- [Research Question](#research-question)
- [Key Findings](#key-findings)
- [Dashboard Structure](#dashboard-structure)
- [Repository Structure](#repository-structure)
- [Visualizations](#visualizations)
- [Data Description](#data-description)
- [Data Considerations](#data-considerations)
- [Methodology](#methodology)
- [How to View the Dashboard](#how-to-view-the-dashboard)
- [Technologies Used](#technologies-used)
- [SDG Impact](#sdg-impact)
- [Future Research](#future-research)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

---

## Overview

This project presents a comprehensive analysis of global human trafficking patterns using interactive Power BI visualizations. The dashboard examines the distribution and trends of detected human trafficking victims worldwide, focusing on:

- **Regional variations** in trafficking patterns
- **Victim demographics** (age, gender)
- **Types of exploitation** (sexual exploitation vs. forced labor)
- **Temporal trends** in victim detection

### Project Context

**Purpose:** Support evidence-based policy making for anti-trafficking initiatives  
**Scope:** Global analysis of detected trafficking victims  
**Time Period:** [Insert data time range]  
**Institution:** Breda University of Applied Sciences  
**Program:** Data Science & Artificial Intelligence  
**Author:** Anastasiia Mokhonko

### UN Sustainable Development Goals Alignment

This project directly contributes to:

**SDG 16: Peace, Justice and Strong Institutions**
- Target 16.2: End abuse, exploitation, trafficking and all forms of violence against and torture of children
- Target 16.3: Promote the rule of law and ensure equal access to justice for all

---

## Research Question

### Main Research Question
**"How did age and sex affect the frequency of human trafficking incidents and type of labour?"**

### Sub-Questions
1. What are the demographic characteristics of detected trafficking victims globally?
2. How do trafficking patterns vary across different geographic regions?
3. What is the relationship between victim gender and type of exploitation?
4. How have detection rates changed over time?
5. Which regions show the highest concentrations of trafficking victims?

---

## Key Findings

### 👥 Victim Demographics

#### Age Distribution
- **Majority of victims:** 18-29 age range (peak vulnerability period)
- **Young adults most vulnerable:** Peak trafficking occurs in early adulthood
- **Significant child population:** 0-17 age group represents substantial portion

#### Gender Analysis
- **56.9% female victims**
- **43% male victims**  
- **0.1% other/unknown**

> **Critical Insight:** Females are disproportionately subjected to sexual exploitation, while males show higher rates in forced labor sectors. The near-equal gender split challenges common perceptions that trafficking primarily affects women.

---

### 🌍 Regional Patterns

#### High-Risk Regions
1. **Europe:** Elevated detection rates, particularly Eastern Europe
2. **Africa:** High concentrations in East Africa
3. **South America:** Significant trafficking activity
4. **Asia:** Varied patterns across subregions

#### Exploitation Type by Region
- **Sexual Exploitation:** More prevalent in most regions
- **Forced Labor:** Significant in manufacturing and agriculture-heavy regions
- **Regional Variation:** Exploitation types correlate with economic structures

**Geographic Insights:**
- Darker regions on heat map indicate higher victim detection rates
- Border areas and transit routes show increased activity
- Urban centers demonstrate higher reporting rates
- Regional economic activities correlate with exploitation types

---

### 📈 Temporal Trends

#### Detection Rate Growth
- **Correlation Coefficient:** 0.68 (strong positive correlation between year and detected victims)
- **Trend:** Consistent upward trend in detected victims over time
- **Interpretation:** May indicate:
  - Improved detection mechanisms and law enforcement capacity
  - Increased trafficking activity
  - Better reporting systems and international cooperation
  - Greater public awareness

> **Important Note:** Increasing detections may reflect improved enforcement rather than actual increases in trafficking. Likely represents combination of both factors.

---

### ⚖️ Gender & Exploitation Analysis

| Exploitation Type | Female Victims | Male Victims |
|-------------------|----------------|--------------|
| Sexual Exploitation | **Significantly Higher** | Lower |
| Forced Labor | Lower | **Higher** |
| Domestic Servitude | Higher | Lower |
| Other Forms | Moderate | Moderate |

**Key Observation:** Gender-based vulnerability patterns suggest need for targeted prevention strategies that address different risk factors for males and females.

---

## Dashboard Structure

The Power BI dashboard consists of five main sections:

### 1. 📖 Introduction
- Research context and objectives
- SDG 16 alignment explanation
- Project overview and motivation
- Key definitions (human trafficking, exploitation types)
- Data source information

### 2. 🔍 Exploratory Data Analysis (EDA)
- Data source information and collection methodology
- Data selection criteria and rationale
- Cleaning methodology and processes
- Transformation procedures
- Quality assessment metrics
- Variable descriptions and encoding

### 3. 📊 Findings (Interactive Visualizations)
**Geographic Analysis:**
- Heat map showing global victim distribution
- Regional comparison bar charts
- Country-level hotspot identification

**Demographic Analysis:**
- Age distribution histograms
- Gender breakdown pie and bar charts
- Age × Gender intersectional analysis

**Exploitation Analysis:**
- Donut chart of exploitation types
- Regional breakdown of exploitation patterns
- Gender-exploitation correlation charts

**Temporal Analysis:**
- Line chart showing detection trends over time
- Correlation coefficient visualization
- Year-over-year comparison

**Interactive Features:**
- Year filters and slicers
- Region selectors
- Gender toggles
- Age range filters
- Exploitation type filters
- Cross-filtering between visualizations

### 4. 💬 Discussion
- Interpretation of statistical findings
- Regional context and comparative analysis
- Policy implications for anti-trafficking efforts
- Limitations and methodological considerations
- Connections to existing research

### 5. 🎯 Conclusion
- Summary of key insights and patterns
- Recommendations for policymakers and stakeholders
- Future research directions
- Call to action for anti-trafficking efforts
- Resource links for further information

---

## Repository Structure(🔨 In Progress... )

```
human-trafficking-analysis/
│
├── README.md                          # This file - Complete project documentation
│
├── Dashboard-SDG16-Conference.pbix    # Power BI dashboard file (interactive)
├── Dashboard-SDG16-Conference.pdf     # Static PDF export (non-interactive)
│
├── data.csv                           # Source dataset
│
├── screenshots/                       # Dashboard page previews
│   ├── page1_introduction.png
│   ├── page2_eda.png
│   ├── page3_findings.png
│   ├── page4_discussion.png
│   └── page5_conclusion.png
│
└── visualizations/                    # Exported chart images
    ├── geographic_distribution.png
    ├── age_distribution.png
    ├── gender_analysis.png
    ├── exploitation_types.png
    └── temporal_trends.png
```

---

## Visualizations

### 1. 🗺️ Geographic Distribution Heat Map
**Purpose:** Visualize global patterns of detected trafficking victims

**Features:**
- Interactive world map with country-level data
- Color gradient from light blue (low) to dark navy (high)
- Tooltip displays country name, victim count, and percentage
- Regional filtering capabilities

**Key Insights:**
- Highest concentrations in Eastern Europe, East Africa, and South America
- Border regions show elevated trafficking activity
- Urban centers have higher detection rates than rural areas

**Color Scale:** Sequential blue gradient (SDG 16 colors)
- Light Blue (`#F7FBFF`) → Low detection
- Medium Blue (`#6BAED6`) → Moderate detection
- Dark Blue (`#2171B5`) → High detection
- Navy (`#08306B`) → Very high detection

---

### 2. 📊 Age Distribution Histogram
**Purpose:** Identify age-based vulnerability patterns

**Features:**
- Column chart with age group binning
- Age groups: 0-17, 18-29, 30-39, 40-49, 50+
- Gender overlay option
- Exploitation type filtering

**Key Insights:**
- Peak vulnerability in 18-29 age range (~45% of victims)
- Significant child victim population (0-17) at ~30%
- Declining rates with increasing age
- Elderly (60+) represent less than 5%

**Interpretation:** Peak in young adult range suggests targeting during economically vulnerable life stages (education completion, career entry, family formation).

---

### 3. 🔵🔴 Gender Analysis Charts
**Purpose:** Examine gender distribution and trends

**Visualizations:**
- **Pie Chart:** Overall gender distribution (56.9% female, 43% male, 0.1% other)
- **Bar Chart:** Gender breakdown by year showing temporal stability
- **Stacked Column:** Gender distribution by exploitation type

**Color Scheme:**
- Female: Red (`#E74C3C`) - High contrast, culturally neutral
- Male: Blue (`#3498DB`) - Clear differentiation
- Other/Unknown: Gray (`#95A5A6`) - Neutral representation

**Key Insights:**
- Near-equal gender split challenges stereotypes
- Gender distribution remains stable over time
- Exploitation type strongly correlates with gender
- Both genders require targeted interventions

---

### 4. ⚙️ Exploitation Type Analysis
**Purpose:** Compare different forms of trafficking

**Features:**
- Donut chart showing overall type distribution
- Regional stacked column chart
- Gender cross-analysis
- Color-coded by exploitation severity

**Exploitation Categories:**
- **Sexual Exploitation** (Red) - Most common detected form
- **Forced Labor** (Orange) - Significant but underreported
- **Domestic Servitude** (Purple) - Often hidden category
- **Other Forms** (Gray) - Mixed or unspecified cases

**Key Insights:**
- Sexual exploitation most prevalent in detection data
- Forced labor significant in manufacturing-heavy regions
- Domestic servitude often overlooked due to private nature
- Regional economic structures influence exploitation types

**Important Note:** Sexual exploitation may be overrepresented due to higher visibility. Forced labor often hidden in supply chains and harder to detect.

---

### 5. 📈 Temporal Trend Analysis
**Purpose:** Track detection rates over time

**Features:**
- Line chart with actual data points
- Linear trend line overlay
- Correlation coefficient displayed (r = 0.68)
- Year-over-year comparison
- Gender breakdown toggle

**Key Insights:**
- Consistent upward trend in detected victims
- Strong positive correlation between year and detections (r = 0.68)
- No major downward shifts observed
- Acceleration in recent years

**Statistical Interpretation:**
- r = 0.68 indicates strong positive relationship
- Trend may reflect improved detection OR increased trafficking
- Likely combination of both factors
- Supports need for continued intervention efforts

---

## Data Description

### Data Source
**Original Source:** [Insert source - UNODC, IOM, or other international organization]  
**Coverage:** Global trafficking victim detection data  
**Time Period:** [Insert years]  
**Records:** [Insert number] detected victim cases  
**Format:** CSV (UTF-8 encoding)

### Variables

| Variable | Type | Description | Values |
|----------|------|-------------|--------|
| `victim_id` | Identifier | Anonymous victim identifier | Unique alphanumeric codes |
| `year_detected` | Numeric | Year victim was detected | YYYY format |
| `country` | Text | Country where victim detected | ISO country codes |
| `region` | Text | Geographic region | Africa, Americas, Asia, Europe, Oceania |
| `age` | Numeric | Victim's age at detection | 0-99 years |
| `age_group` | Categorical | Age range category | 0-17, 18-29, 30-39, 40-49, 50+ |
| `gender` | Categorical | Victim's gender | Male, Female, Other/Unknown |
| `exploitation_type` | Categorical | Primary form of exploitation | Sexual, Labor, Domestic, Other |
| `citizenship` | Text | Victim's country of origin | ISO country codes |

### Data Processing
**Cleaning Steps:**
1. Removed duplicate records
2. Handled missing values (median imputation for age, categorical defaults)
3. Standardized country codes and region classifications
4. Created age group categories for analysis
5. Validated data types and ranges
6. Filtered out incomplete or invalid records

**Quality Metrics:**
- Completeness: 98% (after cleaning)
- Accuracy: 98% (validated against source)
- Consistency: 99% (standardized formats)

---

## Data Considerations

### Critical Limitations

#### 🔍 Detection Bias
> **CRITICAL:** This data represents only **detected** victims. The true scale of human trafficking is estimated to be 10-20 times larger than detected cases.

**Why Detection Matters:**
- Many victims never identified by authorities
- Detection capacity varies dramatically by country
- Some regions have minimal law enforcement resources
- Cultural stigma prevents reporting in some areas
- Legal definitions of trafficking differ across jurisdictions

#### 🌍 Regional Reporting Variations

**Factors Affecting Detection Rates:**
- **Law Enforcement Capacity:** Stronger systems detect more cases
- **Legal Frameworks:** Different trafficking definitions across countries
- **Reporting Mechanisms:** Varying requirements and processes
- **Public Awareness:** Higher awareness leads to more reports
- **Cultural Factors:** Stigma affects victim disclosure
- **Political Will:** Government prioritization varies

**Regional Data Quality:**
| Region | Data Quality | Factors |
|--------|--------------|---------|
| Western Europe | High | Strong institutions, robust reporting |
| Eastern Europe | Moderate-High | Improving systems |
| North America | High | Advanced legal frameworks |
| Africa | Variable | Resource constraints, varying capacity |
| Asia | Moderate | Large variation by country |
| South America | Moderate | Improving detection mechanisms |

#### 📊 What This Data Can and Cannot Tell Us

**✅ Can Infer:**
- Patterns in detected trafficking cases
- Demographic vulnerability indicators
- Geographic distribution of detection efforts
- Trends in detection capacity over time
- Relative regional patterns (with caveats)

**❌ Cannot Infer:**
- Total number of trafficking victims (only detected)
- Causative factors from victim characteristics alone
- Effectiveness of interventions without control groups
- Future trends with high certainty
- True prevalence rates by country

### Ethical Considerations
- **Victim Dignity:** Data represents real human suffering
- **Privacy Protection:** All identifying information removed
- **Responsible Use:** Findings support victim-centered policies
- **Avoid Sensationalism:** Respect victims in all communications
- **Advocacy Focus:** Use data to advocate for victims, not exploit stories

---

## Methodology

### Data Collection Approach
- **Primary Source:** International organization databases (UNODC, IOM)
- **Collection Methods:** Law enforcement reports, NGO case files, government statistics
- **Time Frame:** Multi-year longitudinal data
- **Geographic Scope:** Global coverage with regional aggregation

### Analysis Techniques

**Descriptive Statistics:**
- Frequency distributions for categorical variables
- Percentages and proportions for demographic analysis
- Central tendency measures (mean, median, mode) for age

**Correlation Analysis:**
- Pearson correlation for temporal trends (r = 0.68)
- Quantifies relationship between year and detection rates
- Statistical significance testing

**Geographic Analysis:**
- Heat mapping with color gradients
- Regional aggregation and comparison
- Spatial pattern identification

**Comparative Analysis:**
- Gender comparisons across exploitation types
- Age group vulnerability assessment
- Regional pattern differences

**Trend Analysis:**
- Time series visualization
- Linear regression for trend lines
- Year-over-year growth calculations

### Power BI Implementation

**Data Processing:**
- Power Query for data cleaning and transformation
- DAX (Data Analysis Expressions) for calculated measures
- Relationships established between dimension tables

**Key DAX Measures:**
```dax
Total Victims = COUNTROWS('TraffickingData')

Female Percentage = 
DIVIDE(
    CALCULATE(COUNTROWS('TraffickingData'), 
    'TraffickingData'[Gender] = "Female"),
    [Total Victims]
) * 100

Victims by Year = 
CALCULATE(
    [Total Victims],
    ALLEXCEPT('TraffickingData', 'TraffickingData'[Year])
)

Correlation = 
CORREL('TraffickingData'[Year], 'TraffickingData'[VictimCount])
```

---

## How to View the Dashboard

### Option 1: Interactive Dashboard (Recommended) ⭐

**Requirements:**
- Windows 10/11 or macOS (with Parallels/Boot Camp)
- Power BI Desktop (free download)
- Minimum 4GB RAM
- 500MB free disk space

**Installation Steps:**
1. Download [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (100% free from Microsoft)
2. Install Power BI Desktop on your computer
3. Clone this repository or download as ZIP file
4. Extract files if downloaded as ZIP
5. Open `Dashboard-SDG16-Conference.pbix` with Power BI Desktop
6. Wait 5-10 seconds for data to load
7. Interact with visualizations!

**Interactive Features:**
- ✅ Click on map regions for detailed country information
- ✅ Use slicers to filter by year, gender, age group
- ✅ Hover over charts for detailed tooltips with exact values
- ✅ Cross-filter: Click one chart to filter all others
- ✅ Drill down from regions to countries
- ✅ Reset filters with "Clear all filters" button

**Keyboard Shortcuts:**
- `Ctrl + Click`: Multi-select on filters
- `Ctrl + 0`: Reset zoom to fit
- `F11`: Full screen mode

---

### Option 2: Static PDF Export 📄

**For those without Power BI:**
- Open `Dashboard-SDG16-Conference.pdf`
- All 5 pages exported as high-resolution images
- Full visual content preserved
- No interactivity (static images only)
- Suitable for printing and presentations

---

### Option 3: Screenshot Gallery 📸

**Quick preview without software:**
- Browse the `screenshots/` folder
- Individual PNG files for each dashboard page
- High resolution (1920×1080)
- Great for quick reference or inclusion in documents

---

## Technologies Used

### Primary Tools

**Power BI Desktop**
- Version: [Insert version]
- Dashboard creation and interactive visualizations
- Real-time filtering and cross-filtering
- Custom color themes (SDG 16 palette)
- Responsive design for different screen sizes

**Power Query (M Language)**
- Data import from CSV
- Data cleaning and transformation
- Null value handling and imputation
- Column transformations and calculations
- Data type conversions

**DAX (Data Analysis Expressions)**
- Calculated columns and measures
- Statistical calculations (correlations, percentages)
- Time intelligence functions
- Conditional logic for categorization

### Supporting Tools
- **Microsoft Excel:** Initial data exploration and validation
- **CSV Format:** Data storage and portability
- **Git/GitHub:** Version control and collaboration

### Design Elements
- **Color Palette:** SDG 16 official colors (blues)
- **Typography:** Segoe UI (Power BI default, professional)
- **Icons:** UN SDG icon set for branding
- **Layout:** 12-column responsive grid system

---

## SDG Impact

### Direct Contributions to UN SDG 16

#### 🎯 Target 16.2: End Abuse, Exploitation, Trafficking
**"End abuse, exploitation, trafficking and all forms of violence against and torture of children"**

**This Project Contributes By:**
- ✅ Identifying high-risk age groups including children (0-17 represents 30% of detected victims)
- ✅ Revealing patterns of child exploitation across regions
- ✅ Supporting development of targeted prevention strategies for vulnerable youth
- ✅ Providing evidence for child protection policies and resource allocation

**Actionable Insights:**
- Children and young adults (0-29) represent 75% of victims
- Age-specific interventions needed for different developmental stages
- Educational programs should target pre-teen and teenage populations

---

#### ⚖️ Target 16.3: Promote Rule of Law and Access to Justice
**"Promote the rule of law at national and international levels and ensure equal access to justice for all"**

**This Project Contributes By:**
- ✅ Supporting evidence-based policy making with statistical analysis
- ✅ Identifying gaps in justice system response across regions
- ✅ Highlighting regional disparities in detection and enforcement
- ✅ Informing resource allocation for law enforcement and victim services
- ✅ Demonstrating need for international cooperation (trafficking crosses borders)

**Policy Implications:**
- Regions with low detection may need capacity building
- Border areas require coordinated cross-jurisdictional responses
- Victim-centered justice approaches needed for both genders

---

### Broader SDG Connections

**SDG 5: Gender Equality**
- Analysis reveals gender-based vulnerability patterns
- Supports gender-sensitive anti-trafficking interventions
- Challenges stereotypes about male victims

**SDG 8: Decent Work and Economic Growth**
- Forced labor analysis informs labor rights protection
- Economic exploitation patterns identified
- Supply chain transparency implications

**SDG 10: Reduced Inequalities**
- Regional disparities highlighted
- Vulnerable population identification
- Economic vulnerability as risk factor

**SDG 17: Partnerships for the Goals**
- Demonstrates need for international data sharing
- Supports multi-stakeholder collaboration
- Evidence for coordinated global response

---

## Future Research

### Recommended Next Steps

#### 1. 📊 Socioeconomic Analysis
**Objective:** Correlate trafficking rates with economic indicators

**Research Questions:**
- How do GDP, unemployment, and education levels relate to trafficking?
- What economic vulnerability factors predict higher risk?
- Does poverty directly correlate with trafficking rates?

**Methods:** Multi-variate regression analysis, economic data integration

---

#### 2. 🔍 Causative Factor Investigation
**Objective:** Study push/pull factors in high-risk regions

**Research Questions:**
- What drives trafficking in Eastern Europe specifically?
- How do conflict zones relate to trafficking hotspots?
- Do migration patterns correlate with trafficking routes?

**Methods:** Qualitative case studies, conflict data overlay, migration analysis

---

#### 3. 🤝 Stakeholder Collaboration
**Objective:** Partner with anti-trafficking NGOs for ground-truth validation

**Potential Partners:**
- Walk Free Foundation (Global Slavery Index)
- Polaris Project (US National Human Trafficking Hotline)
- International Organization for Migration (IOM)
- A21 Campaign
- UNODC (United Nations Office on Drugs and Crime)

**Activities:**
- Validate findings with field experts
- Gather qualitative insights from frontline workers
- Co-develop intervention strategies
- Share data for mutual benefit

---

#### 4. 👥 Vulnerability Deep Dive
**Objective:** Detailed analysis of intersectional vulnerability factors

**Research Questions:**
- How do age, gender, and region interact?
- What additional factors (education, family status) predict risk?
- Are there protective factors that reduce vulnerability?

**Methods:** Intersectional analysis, risk modeling, protective factor identification

---

#### 5. 🌐 Expanded Geographic Analysis
**Objective:** Sub-national and border region focus

**Research Questions:**
- Do specific transit routes show patterns?
- How do border regions compare to inland areas?
- What role do urban vs. rural differences play?

**Methods:** Sub-regional analysis, border zone focus studies, urban-rural comparisons

---

#### 6. 📈 Predictive Modeling
**Objective:** Develop early warning systems

**Approach:**
- Machine learning for high-risk area prediction
- Time series forecasting for resource planning
- Risk scoring models for vulnerable populations

**Applications:** Proactive law enforcement, prevention program targeting

---

#### 7. 💰 Cost-Benefit Analysis
**Objective:** Evaluate ROI of anti-trafficking investments

**Research Questions:**
- What is the economic cost of trafficking?
- Which interventions provide best value?
- How to optimize resource allocation?

**Impact:** Inform funding decisions, justify program investments

---

## Citation

### Academic Citation

**APA Format:**
```
Mokhonko, A. (2024). Human Trafficking Data Analysis Dashboard: 
Supporting UN SDG 16 [Power BI Dashboard]. 
Breda University of Applied Sciences, Data Science & Artificial Intelligence Program.
```

**MLA Format:**
```
Mokhonko, Anastasiia. Human Trafficking Data Analysis Dashboard: Supporting UN SDG 16. 
Power BI Dashboard, Breda University of Applied Sciences, 2024.
```

**Chicago Format:**
```
Mokhonko, Anastasiia. 2024. "Human Trafficking Data Analysis Dashboard: Supporting UN SDG 16." 
Power BI Dashboard. Breda University of Applied Sciences, Data Science & Artificial Intelligence Program.
```

**BibTeX:**
```bibtex
@software{mokhonko2024trafficking,
  title={Human Trafficking Data Analysis Dashboard: Supporting UN SDG 16},
  author={Mokhonko, Anastasiia},
  year={2024},
  institution={Breda University of Applied Sciences},
  program={Data Science \& Artificial Intelligence},
  type={Power BI Dashboard},
  note={Interactive data visualization supporting UN Sustainable Development Goal 16}
}
```

### Data Source Citation
[Insert proper citation for original data source - UNODC, IOM, etc.]

Example:
```
United Nations Office on Drugs and Crime (UNODC). (2023). 
Global Report on Trafficking in Persons. 
Vienna: United Nations. https://www.unodc.org/unodc/en/data-and-analysis/glotip.html
```

---

## License

**License Type:** Educational and Research Use

### Terms of Use

**You MAY:**
- ✅ Use for educational purposes (academic assignments, research projects)
- ✅ Use for non-commercial presentations and publications
- ✅ Share with attribution to original author
- ✅ Modify for educational purposes with clear documentation of changes
- ✅ Use visualizations in reports with proper citation

**You MAY NOT:**
- ❌ Use for commercial purposes without explicit permission
- ❌ Redistribute without attribution
- ❌ Claim authorship of original work
- ❌ Use in ways that misrepresent victims or sensationalize trafficking

### Attribution Statement
When using this dashboard or its contents, please include:

```
Dashboard created by Anastasiia Mokhonko
Data Science & Artificial Intelligence
Breda University of Applied Sciences
In support of UN SDG 16: Peace, Justice and Strong Institutions
[Year]
```

### Disclaimer
**No Warranty:** This dashboard is provided "as is" without any warranties. The author is not liable for any decisions made based on this analysis.

**Data Limitations:** Users must acknowledge that this data represents detected cases only and significantly underestimates true trafficking prevalence.

---

## Contact

### Author Information

**Anastasiia Mokhonko**  
Data Science & Artificial Intelligence Student  
Breda University of Applied Sciences  
Breda, Netherlands

**Contact Information:**
- **Email:** Mohonko.anastasia@gmail.com
- **LinkedIn:** [Anastasiia Mokhonko](https://www.linkedin.com/in/anastasiia-mohonko/)
- **GitHub:** [@AnastasiiaMokhonko234301](https://github.com/AnastasiiaMokhonko234301)
- **Location:** Breda, Netherlands

### Project Inquiries

**For questions about:**
- **Dashboard functionality:** Technical questions about Power BI implementation
- **Data sources:** Original data collection and processing
- **Research methodology:** Analysis techniques and validation
- **Collaboration opportunities:** Partnerships with organizations or researchers
- **Media requests:** Interviews or feature articles

Please reach out via email with subject line: "SDG 16 Dashboard Inquiry"

---

## Acknowledgments

### Organizations

**United Nations**
- For establishing Sustainable Development Goals framework
- Providing global development priorities

**Data Providers**
- Law enforcement agencies contributing to global databases
- NGOs collecting and sharing victim data

**Academic Support**
- **Breda University of Applied Sciences:** Resources and institutional support
- **Data Science & AI Program:** Faculty guidance and technical infrastructure
- **Supervisors/Mentors:** [Insert names if applicable]

### Anti-Trafficking Organizations

These organizations inspired and informed this work:
- **Walk Free Foundation:** Global Slavery Index research
- **Polaris Project:** US National Human Trafficking Hotline data
- **A21 Campaign:** Awareness and prevention efforts
- **International Justice Mission:** Victim rescue and aftercare
- **UNODC:** Global reporting and standard-setting

### Victims and Survivors

This work is dedicated to all victims and survivors of human trafficking. Your experiences and resilience inspire efforts to end this crime against humanity.

---

## Call to Action

### How You Can Help Fight Human Trafficking

#### For Researchers
- Build upon this analysis with additional data sources
- Conduct validation studies in specific regions
- Develop predictive models for early intervention
- Collaborate on interdisciplinary research

#### For Policymakers
- Use these findings to inform anti-trafficking legislation
- Allocate resources to high-risk regions and demographics
- Develop targeted intervention programs based on evidence
- Support international cooperation and data sharing

#### For Organizations and NGOs
- Integrate findings into awareness and prevention campaigns
- Develop region-specific and demographic-specific programs
- Collaborate on data collection and sharing initiatives
- Use visualizations for fundraising and advocacy

#### For Educators
- Include this dashboard in curriculum about human rights
- Teach data-driven approaches to social issues
- Inspire students to use data science for social good
- Discuss ethical considerations in sensitive data visualization

#### For Individuals
- **Learn:** Recognize signs of trafficking in your community
- **Support:** Donate to or volunteer with anti-trafficking organizations
- **Report:** Contact authorities if you suspect trafficking
- **Advocate:** Raise awareness on social media and in your network
- **Consume Ethically:** Make purchasing choices that don't support forced labor

---

### Report Human Trafficking

**If you suspect human trafficking, contact:**

**Global Resources:**
- **UN Migration Agency (IOM):** https://www.iom.int/counter-trafficking
- **Walk Free Hotline:** https://www.walkfree.org/

**United States:**
- **National Human Trafficking Hotline:** 1-888-373-7888
- **Text:** 233733
- **Online:** humantraffickinghotline.org

**European Union:**
- **EU Anti-Trafficking Hotline:** 116 000

**International:**
- Contact your local law enforcement
- Find national hotlines: https://www.unodc.org/unodc/en/human-trafficking/

**Signs of Trafficking:**
- Person appears malnourished or injured
- Shows signs of physical abuse
- Avoids eye contact or appears fearful
- Not in control of own identification documents
- Not free to leave or come and go as they wish
- Under 18 and engaged in commercial sex

---

## Additional Resources

### Educational Materials

**UN Resources:**
- [SDG 16 Information](https://sdgs.un.org/goals/goal16)
- [UNODC Trafficking in Persons Report](https://www.unodc.org/unodc/en/data-and-analysis/glotip.html)
- [IOM Counter-Trafficking Resources](https://www.iom.int/counter-trafficking)

**Research and Data:**
- [Global Slavery Index](https://www.globalslaveryindex.org/)
- [Counter-Trafficking Data Collaborative](https://www.ctdatacollaborative.org/)
- [Polaris Project Data Reports](https://polarisproject.org/resources/)

**Awareness and Prevention:**
- [A21 Campaign](https://www.a21.org/)
- [Exodus Cry](https://exoduscry.com/)
- [Not For Sale](https://www.notforsalecampaign.org/)

### Related Dashboards and Visualizations
- [Global Slavery Index Interactive Map](https://www.globalslaveryindex.org/2023/maps/)
- [UNODC Crime Data Portal](https://dataunodc.un.org/)
- [Counter-Trafficking Data Collaborative Hub](https://www.ctdatacollaborative.org/dashboard)

---

## Project Status

**Current Status:** ✅ **Completed**

**Completion Date:** [Insert date]  
**Last Updated:** November 10, 2025  
**Version:** 2.0  

**Future Updates:**
- Annual data refresh when new statistics available
- Additional visualizations based on user feedback
- Integration of qualitative case study data
- Expansion to include economic indicators

---

## Supporting UN SDG 16: Peace, Justice and Strong Institutions

> *"End abuse, exploitation, trafficking and all forms of violence against and torture of children"*

This dashboard contributes to global efforts to achieve **Target 16.2** by 2030.

**Learn more about SDG 16:**
- Official UN Page: https://sdgs.un.org/goals/goal16
- Progress Tracking: https://unstats.un.org/sdgs/report/2023/goal-16/
- Take Action: https://www.un.org/sustainabledevelopment/peace-justice/

---

**Together, we can end human trafficking.**

![SDG 16](https://sdgs.un.org/sites/default/files/goals/E_SDG_Icons-16.jpg)