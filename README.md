# 🏥 Fibromyalgia Diagnostic Assessment App

A comprehensive, interactive web application for conducting fibromyalgia assessments based on the **New Clinical Fibromyalgia Diagnostic Criteria** from the Fibromyalgia Network.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Medical Disclaimer](#-medical-disclaimer)
- [Technical Details](#-technical-details)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### 🎯 **Core Assessment Tools**
- **Widespread Pain Index (WPI)** calculation with 19 body regions
- **Symptom Severity Score (SS)** with 3 core symptoms + 41 additional symptoms
- **Interactive body diagram** visualization showing pain areas in real-time
- **Automatic diagnostic criteria evaluation** following official medical standards

### 🎨 **Advanced User Interface**
- **Professional medical-grade design** with custom CSS styling
- **Responsive layout** that works on desktop, tablet, and mobile
- **Interactive visualizations** using Plotly for charts and body diagrams
- **Real-time score updates** as you complete the assessment

### 📊 **Data Analytics & Visualization**
- **Score breakdown charts** comparing individual scores to maximum possible
- **Pain distribution analysis** by body regions (pie charts)
- **Comprehensive results dashboard** with visual diagnostic criteria evaluation
- **Historical comparison capabilities**

### 💾 **Export & Data Management**
- **JSON export** for detailed medical records
- **CSV export** for spreadsheet analysis
- **Timestamped assessments** for tracking over time
- **Session persistence** - never lose your progress

### 🔒 **Medical Compliance**
- **Official diagnostic criteria** implementation (Wolfe F, et al. Arthritis Care Res)
- **Professional medical disclaimer** following healthcare guidelines
- **Privacy-focused design** - all data stays local, no cloud storage

## 🎬 Demo

### Main Assessment Interface
- Interactive checkboxes for 19 pain areas
- Real-time body diagram updates
- Severity scales (0-3) for core symptoms
- Comprehensive symptom checklist (41 items)

### Results Dashboard
- Professional score cards showing WPI and SS scores
- Visual diagnostic criteria evaluation
- Interactive charts and visualizations
- Export functionality for medical records

## 🛠 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Quick Start

1. **Clone or download the repository:**
   ```bash
   git clone <repository-url>
   cd fibromyalgia-assessment-app
   ```

2. **Install required packages:**
   ```bash
   pip install streamlit plotly pandas
   ```

3. **Run the application:**
   ```bash
   streamlit run fibromyalgia_app.py
   ```

4. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

### Alternative Installation (Virtual Environment Recommended)

```bash
# Create virtual environment
python -m venv fibro_env

# Activate virtual environment
# On Windows:
fibro_env\Scripts\activate
# On macOS/Linux:
source fibro_env/bin/activate

# Install packages
pip install streamlit plotly pandas

# Run the app
streamlit run fibromyalgia_app.py
```

## 🚀 Usage

### Step-by-Step Assessment Process

#### **Part 1: Widespread Pain Index (WPI)**
1. Review the interactive body diagram
2. Check all body areas where you've experienced pain in the past week
3. Watch the body diagram update in real-time
4. Your WPI score (0-19) is calculated automatically

#### **Part 2a: Core Symptom Severity**
1. Rate three core symptoms on a 0-3 scale:
   - Fatigue
   - Waking unrefreshed
   - Cognitive symptoms
2. Use the detailed descriptions for accurate rating

#### **Part 2b: Additional Symptoms**
1. Check all additional symptoms experienced in the past week
2. 41 symptoms organized in easy-to-scan columns
3. Automatic scoring based on symptom count

#### **Results & Analysis**
1. Click "Calculate Assessment Results" to process your responses
2. View comprehensive results dashboard with:
   - Individual and total scores
   - Diagnostic criteria evaluation
   - Visual analytics and charts
   - Pain distribution analysis

#### **Export Your Results**
1. Download results in JSON format for detailed records
2. Download CSV format for spreadsheet analysis
3. Results include timestamp and full assessment data

### Key Features Explained

#### **Interactive Body Diagram**
- Real-time visualization of selected pain areas
- Color-coded markers (red = pain areas, blue = no pain)
- Hover information showing body region names
- Professional medical diagram layout

#### **Diagnostic Criteria Evaluation**
The app evaluates two criteria paths:
- **Criterion 1a:** WPI ≥ 7 AND SS ≥ 5
- **Criterion 1b:** WPI 3-6 AND SS ≥ 9

Clear visual indication of which criteria are met.

#### **Score Calculations**
- **WPI Score:** Count of pain areas (0-19)
- **SS 2a Score:** Sum of three core symptoms (0-9)  
- **SS 2b Score:** Based on additional symptom count (0-3)
- **Total SS Score:** SS 2a + SS 2b (0-12)

## ⚠️ Medical Disclaimer

**IMPORTANT: This application is for educational and research purposes only.**

- This survey is **NOT** meant to substitute for a diagnosis by a medical professional
- Patients should **NOT** diagnose themselves using this tool
- **Always consult your medical professional** for advice and treatment
- This assessment provides insight into research on diagnostic criteria and symptom severity measurement
- Results should be discussed with qualified healthcare providers

*Based on: Wolfe F, et al. Arthritis Care Res DOI 10.1002/acr.20140 [Epub ahead of print] February 23, 2010. Fibromyalgia Network.*

## 🔧 Technical Details

### Architecture Overview

```
fibromyalgia_app.py
├── UI Components
│   ├── Custom CSS styling
│   ├── Streamlit layout (columns, forms, sidebar)
│   └── Interactive widgets
├── Assessment Logic
│   ├── WPI calculation
│   ├── SS score calculation
│   └── Diagnostic criteria evaluation
├── Visualizations
│   ├── Interactive body diagram (Plotly)
│   ├── Score comparison charts
│   └── Pain distribution analysis
└── Data Export
    ├── JSON export functionality
    ├── CSV export functionality
    └── Session state management
```

### Key Technologies

- **Streamlit:** Web app framework for Python
- **Plotly:** Interactive visualization library
- **Pandas:** Data manipulation and analysis
- **Custom CSS:** Professional medical interface styling

### Code Structure Highlights

```python
# Main components breakdown:
def create_interactive_body_diagram(pain_areas)  # Interactive body visualization
def calculate_wpi_score(pain_areas)             # WPI calculation logic  
def calculate_ss_score_2a(fatigue, waking, cognitive)  # Core symptoms
def calculate_ss_score_2b(symptoms_count)       # Additional symptoms
def evaluate_diagnostic_criteria(wpi, ss)       # Medical criteria evaluation
def main()                                      # Main application logic
```

### Performance Features

- **Session state management** for data persistence
- **Efficient form handling** with Streamlit forms
- **Responsive design** for multiple device types
- **Local data processing** - no external API calls required

### Browser Compatibility

- Chrome 80+ ✅
- Firefox 75+ ✅  
- Safari 13+ ✅
- Edge 80+ ✅

## 🎓 Educational Use

This app is perfect for:

### **Medical Education**
- Healthcare students learning fibromyalgia diagnostic criteria
- Medical professionals training on assessment tools
- Research demonstrations and presentations

### **Programming Education** 
- **Streamlit development** - comprehensive example of advanced features
- **Data visualization** - Plotly integration and custom charts
- **Form handling** - complex medical forms with validation
- **Session state management** - persistent data across interactions
- **Professional UI design** - medical-grade interface patterns

### **Code Learning Points for Beginners**
```python
# Session state for remembering data
if 'assessment_complete' not in st.session_state:
    st.session_state.assessment_complete = False

# Forms for grouping inputs
with st.form("form_name"):
    # All inputs here
    submitted = st.form_submit_button("Submit")

# Custom CSS for professional styling
st.markdown("""<style>...</style>""", unsafe_allow_html=True)

# Interactive Plotly charts
fig = go.Figure()
fig.add_trace(go.Scatter(...))
st.plotly_chart(fig)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### **Bug Reports**
- Use the GitHub Issues tab
- Include steps to reproduce
- Include screenshot if applicable

### **Feature Requests**
- Suggest new medical assessment features
- UI/UX improvements
- Additional export formats

### **Code Contributions**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### **Development Setup**
```bash
# Clone your fork
git clone <your-fork-url>
cd fibromyalgia-assessment-app

# Create development environment
python -m venv dev_env
source dev_env/bin/activate  # or dev_env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run fibromyalgia_app.py --server.runOnSave true
```

## 📁 Project Structure

```
fibromyalgia-assessment-app/
│
├── fibromyalgia_app.py      # Main application file
├── README.md                # This file
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License
│
├── assets/                  # Static assets (if any)
│   └── images/
│
├── data/                    # Sample data or templates
│   └── sample_export.json
│
└── docs/                    # Additional documentation
    ├── medical_criteria.md
    └── technical_guide.md
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### **MIT License Summary:**
- ✅ Commercial use allowed
- ✅ Modification allowed  
- ✅ Distribution allowed
- ✅ Private use allowed
- ❗ No warranty provided
- ❗ Authors not liable for damages

## 🙏 Acknowledgments

- **Fibromyalgia Network** for the official diagnostic criteria
- **Dr. Frederick Wolfe et al.** for the research foundation (Arthritis Care Res DOI 10.1002/acr.20140)
- **Streamlit team** for the amazing web app framework
- **Plotly team** for interactive visualization tools

## 📞 Support

### **For Technical Issues:**
- GitHub Issues: Report bugs and technical problems
- Email: [your-email@domain.com]

### **For Medical Questions:**
- **Consult your healthcare provider** - this app does not provide medical advice
- Fibromyalgia Network: (800) 853-2929 or www.fmnetnews.com

### **For Educational Use:**
- Include attribution when using in educational settings
- Cite the original medical research when presenting results

---

**Made with ❤️ for the fibromyalgia community and medical education**

*This application demonstrates advanced Streamlit development techniques while serving a real medical education purpose. Perfect for learning interactive web app development with Python!*
