# The Impact of Employee Cybersecurity Awareness on the Overall Security of Small Hotels

## Project Overview

This research project investigates how employee cybersecurity awareness impacts the overall security posture of small hotels. Conducted at Breda University of Applied Sciences in partnership with DigiWerkplaats, this study addresses the critical gap between cybersecurity knowledge and practice in small and medium-sized hospitality enterprises.

**Duration:** September 2, 2024 - November 1, 2024  
**Institution:** Breda University of Applied Sciences (BUas)  
**Partner Organization:** DigiWerkplaats Breda

## Research Question

**Main Question:** How does employee cybersecurity awareness impact the overall security of small hotels?

**Sub-questions:**
1. Do the personal opinions of employees affect their approach to cybersecurity concerns?
2. Does the presence of an in-house IT specialist improve the cybersecurity awareness of hotel employees?
3. Does the frequency of cybersecurity training affect employee adherence to cybersecurity practices in small hotels?
4. Do the employees' ages correlate with their level of cybersecurity awareness?
5. How do small hotels educate their employees on cybersecurity practices?

## Key Findings

### Training Effectiveness
- **Moderate positive correlation (r = 0.456)** between training frequency and security protocol adherence
- Optimal training frequency: **Quarterly or biannual sessions**
- Interactive, scenario-based training significantly improves engagement and retention

### Role-Specific Insights
- Employees with IT-related roles demonstrate higher adherence levels
- Role-specific training proves more effective than generalized approaches
- Relevance to daily tasks strongly influences practical application

### Demographic Analysis
- **No significant difference** in cybersecurity awareness across age groups
- Supports development of universal training programs
- Age and gender show minimal impact on security awareness

## Methodology

### Mixed-Methods Approach

**Quantitative Data Collection:**
- Online surveys via Qualtrics
- Variables measured: age, confidence levels, training frequency, perceived impact
- Data encoding for statistical analysis

**Qualitative Data Collection:**
- Structured interviews (in-person or via Microsoft Teams)
- Audio recordings (mp3 format) with consent
- AI-powered transcription with manual verification
- Thematic coding and analysis

**Analysis Tools:**
- Python with scikit-learn
- Jupyter Notebooks
- Statistical correlation analysis

## Repository Structure

```
Policy_Research_for_SMEs/
├── README.md                            # Project documentation
├── Poster.png                           # Research poster/infographic
├── Future_research.pdf                  # Identified research directions
├── Policy_paper_Cybersecurity.pdf       # Final policy recommendations
├── Research_proposal.pdf                # Initial research design
├── DMP/                                 # Data Management Plan folder
│   ├── A FAIR Checklist.pdf            # FAIR data principles compliance
│   ├── BUas Research Ethics.pdf        # Ethics review documentation
│   ├── Codebook.md                     # Variable descriptions and encoding
│   ├── Data_storage_protocol.docx      # File naming and folder structure
│   ├── Informed Consent Form.docx      # Participant consent documentation
│   ├── NWO_DMP_Data_Mangament_plan.pdf # Comprehensive data management plan
│   ├── Privacy and GDPR Checklist.pdf  # GDPR compliance documentation
│   └── Research Information Letter.pdf # Study overview for participants
└── Data/                                # Research data folder
    ├── Interview(audio)/                # Raw interview recordings
    │   ├── Interview 1.mp3
    │   ├── Interview 2.mp3
    │   ├── Interview 3.mp3
    │   ├── Interview 4.mp3
    │   └── Interview 5.mp3
    ├── Interview(transcript)/           # Interview transcripts (PDF)
    │   └── Interview_Transcript_Cybersecurity_Practices_in_....pdf (5 files)
    ├── Analyzed_qualitative_data.pdf    # Thematic analysis results
    ├── cleaned_survey.xlsx              # Processed survey data
    ├── Data_preparation.ipynb           # Data cleaning and preparation notebook
    └── FINAL-Cybersecurity-employee_September 30...xlsx  # Raw survey responses
```

## Data Management & Ethics Documentation

### Compliance Framework

This research adheres to strict ethical standards and data protection regulations as required by Breda University of Applied Sciences and Dutch research integrity guidelines.

**Key Documentation in DMP Folder:**

1. **A FAIR Checklist** - Ensures data is Findable, Accessible, Interoperable, and Reusable
   - Persistent identifiers assigned to datasets and metadata
   - Data provided in open formats (CSV, JSON) for cross-platform compatibility
   - Metadata follows Dublin Core and DataCite standards
   - Clear usage licenses (Creative Commons) for data reuse

2. **BUas Research Ethics Review Application** - Comprehensive ethics review documentation
   - Risk assessment categorization: MEDIUM
   - Informed consent procedures for all participants
   - Privacy safeguards and data protection measures
   - No vulnerable populations or medical procedures involved

3. **NWO Data Management Plan** - Detailed data lifecycle management
   - Storage: BUas institutional networked research storage (0-10 GB)
   - Security: Default institutional measures with encryption
   - Retention: Minimum 10 years per institutional policy
   - Access: Research team and mentors only during active research

4. **Privacy and GDPR Checklist** - European data protection compliance
   - Legal basis: Informed consent from all participants
   - Risk level: Low (no sensitive medical/financial data)
   - Data anonymization before analysis
   - Two-factor authentication for data access
   - Participants' right to withdraw at any time

5. **Codebook** - Complete variable documentation
   - 22 quantitative variables with encoding schemes
   - 9 qualitative themes from interview analysis
   - Ordinal, nominal, and continuous variable specifications
   - Survey and interview question mapping

6. **Data Storage Protocol** - Standardized file naming and organization
   - Version control system (V<x> format)
   - Date format: DD-MM-YYYY
   - Naming convention: `<version>_<date>_<names>.<extension>`
   - Clear folder structure for interviews, surveys, and analysis

7. **Informed Consent Form** - Participant rights and study information
   - Purpose: Investigate cybersecurity awareness impact
   - Voluntary participation with right to withdraw
   - Confidentiality and anonymization guarantees
   - GDPR-compliant data handling

8. **Research Information Letter** - Study details for participants
   - Duration: September 30 - November 25, 2024
   - Eligibility: Ages 18-65, hotel employees or hospitality students
   - No costs, risks, or compensation involved
   - Contact information for questions or complaints

### Data Protection Measures

**During Research:**
- Encrypted storage on BUas institutional systems
- Access restricted to research team (5 students + supervisor)
- Two-factor authentication where available
- No third-party data processing

**After Research:**
- Personal identifiers replaced with anonymous IDs
- Age, occupation, and non-identifying data retained for analysis
- Full anonymization before public release
- Participant names and contact information permanently deleted

### Ethics Approval

**Review Status:** Approved by BUas Research Ethics Review Board
- Application submitted: September 27, 2024
- Risk category: MEDIUM (due to personal data collection)
- Consultation with data management support: Myrthe Buckens (September 17, 2024)
- Compliance verified with Netherlands Code of Conduct for Research Integrity (2018)

### Participant Rights

All research participants were informed of their rights:
- Full transparency about data collection and usage
- Voluntary participation without penalty for withdrawal
- Access to their own data upon request
- Right to have data deleted if withdrawn before analysis completion
- Anonymous presentation of all findings in publications

## Data Description

### Qualitative Data

**Interview Audio Files** (`Data/Interview(audio)/`)
- 5 audio recordings in MP3 format
- Structured interviews with hotel employees
- Recorded with participant consent
- Average duration: [duration information]

**Interview Transcripts** (`Data/Interview(transcript)/`)
- 5 PDF transcripts corresponding to audio recordings
- AI-powered transcription with manual verification
- Anonymized participant information
- Coding applied for thematic analysis

**Thematic Analysis** (`Data/Analyzed_qualitative_data.pdf`)
The qualitative analysis identified four major themes from employee interviews:

1. **Infrequency and Basic Nature of Training**
   - Training limited to onboarding or annual refreshers
   - Covers foundational topics (phishing, passwords, basic data protection)
   - Lacks coverage of advanced practices (MFA, encryption, sophisticated threats)
   - Knowledge diminishes over time without regular updates

2. **Limited Interactivity and Engagement**
   - Passive delivery format (online videos, brief presentations)
   - Perceived as "check-the-box" compliance task
   - Low retention and motivation
   - Employees prefer hands-on, scenario-based learning

3. **Lack of Role-Specific Relevance**
   - Generic content not tailored to specific job functions
   - Night-shift employees face unique security challenges
   - Front-desk staff need specialized data protection guidance
   - Disconnect between training and daily responsibilities

4. **Self-Directed Learning and Need for Ongoing Updates**
   - Employees supplement with personal research
   - Inconsistent knowledge levels across staff
   - Desire for standardized, management-driven updates
   - Need for regular refreshers on emerging threats

### Quantitative Data

**Raw Survey Data** (`Data/FINAL-Cybersecurity-employee_September 30...xlsx`)
- Online survey responses collected via Qualtrics
- Variables: age, confidence levels, training frequency, perceived impact
- Exported in Excel format for initial review

**Cleaned Survey Data** (`Data/cleaned_survey.xlsx`)
- Processed and validated survey responses
- Missing data handled
- Data encoded for statistical analysis
- Ready for analysis in Python/Jupyter

**Data Preparation Notebook** (`Data/Data_preparation.ipynb`)
- Jupyter notebook documenting data cleaning steps
- Variable recoding and transformation
- Data quality checks and validation
- Reproducible preprocessing pipeline

### Key Quantitative Findings

- **Training-Adherence Correlation:** Moderate positive correlation (r = 0.456)
- **Optimal Training Frequency:** Quarterly or biannual sessions
- **Role Impact:** IT-related roles show higher adherence
- **Demographics:** No significant age or gender differences in awareness

## Key Recommendations

### For Small Hotels

1. **Implement Regular Training**
   - Schedule cybersecurity training every 3-6 months
   - Balance engagement and knowledge retention
   - Avoid training fatigue through optimal spacing

2. **Enhance Interactivity**
   - Incorporate scenario-based exercises
   - Simulate real-world cybersecurity threats
   - Tailor content to specific roles (front desk, night shift, management)

3. **Foster Security Culture**
   - Provide visible leadership support
   - Issue regular reminders about best practices
   - Integrate security naturally into daily workflows

4. **Universal Training Approach**
   - Standardize training for each role
   - Ensure foundational knowledge for all employees
   - Focus on inclusivity regardless of demographics

5. **Consider Third-Party Providers**
   - Explore cost-effective external training solutions
   - Leverage industry best practices
   - Address resource limitations

## Data Management

### Storage and Security
- **Platform:** BUas institutional research storage
- **Security:** Default institutional measures with encryption
- **Retention:** Minimum 10 years per institutional policy
- **Access:** Limited to research team and mentors

### Privacy and GDPR Compliance
- All personal data anonymized before analysis
- Informed consent obtained from all participants
- Participants can withdraw at any time
- Compliance verified via Privacy and GDPR Checklist

### Data Availability
- Survey and interview data available upon project completion
- Personal information anonymized or excluded
- Public domain license for research reuse
- Contact research team for data requests

## Future Research Directions

1. **Longitudinal Studies** - Track training effectiveness over extended periods
2. **Cost-Benefit Analysis** - Evaluate ROI of cybersecurity investments
3. **Emerging Technologies** - Assess impact of IoT devices and AI-driven threat detection
4. **Gamification Methods** - Explore innovative training approaches (VR, mobile apps)
5. **Cross-Cultural Studies** - Compare cybersecurity norms across regions
6. **Organizational Culture** - Investigate leadership and policy impact
7. **Behavioral Metrics** - Measure actual behavior beyond self-reported awareness

## Acknowledgments

- **DigiWerkplaats** - Project partner and industry collaboration
- **BUas Research Ethics Review Board** - Ethics guidance
- **Participating Hotels and Employees** - Research participants

## License

This project documentation is available under a public domain license. Research data available upon request with appropriate anonymization measures.

## Citation

If you use this research or data, please cite:

```
Mokhonko, A., Musaelans, A., Wang, G., Meijer, N., & Paskalev, P. (2024). 
The Impact of Employee Cybersecurity Awareness on the Overall Security of Small Hotels. 
Breda University of Applied Sciences.
```

---

**Last Updated:** October 30, 2024  
**Version:** 1.0