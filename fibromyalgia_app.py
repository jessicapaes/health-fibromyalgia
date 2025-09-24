import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json

# Page configuration
st.set_page_config(
    page_title="Fibromyalgia Diagnostic Assessment",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    .score-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #667eea;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .diagnostic-result {
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        font-size: 1.2em;
        font-weight: bold;
    }
    .meets-criteria {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        border: 2px solid #ff6b6b;
    }
    .not-meets-criteria {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border: 2px solid #4ecdc4;
    }
    .body-diagram {
        border: 2px solid #ddd;
        border-radius: 10px;
        padding: 1rem;
        background: white;
    }
    .stCheckbox > label {
        font-size: 14px !important;
    }
</style>
""", unsafe_allow_html=True)

def calculate_wpi_score(pain_areas):
    """Calculate Widespread Pain Index score"""
    return len([area for area in pain_areas if area != "None of these areas"])

def calculate_ss_score_2a(fatigue, waking, cognitive):
    """Calculate Symptom Severity Score Part 2a"""
    return fatigue + waking + cognitive

def calculate_ss_score_2b(symptoms_count):
    """Calculate Symptom Severity Score Part 2b based on symptom count"""
    if symptoms_count == 0:
        return 0
    elif 1 <= symptoms_count <= 10:
        return 1
    elif 11 <= symptoms_count <= 24:
        return 2
    else:
        return 3

def evaluate_diagnostic_criteria(wpi_score, ss_score):
    """Evaluate if patient meets fibromyalgia diagnostic criteria"""
    # Criterion 1a: WPI ≥ 7 AND SS ≥ 5
    criterion_1a = wpi_score >= 7 and ss_score >= 5
    
    # Criterion 1b: WPI 3-6 AND SS ≥ 9
    criterion_1b = 3 <= wpi_score <= 6 and ss_score >= 9
    
    return criterion_1a or criterion_1b

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>🏥 New Clinical Fibromyalgia Diagnostic Criteria Assessment</h1>
        <p>Based on the Fibromyalgia Network Clinical Diagnostic Criteria</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar with instructions
    st.sidebar.markdown("## 📋 Instructions")
    st.sidebar.markdown("""
    **When answering questions, consider:**
    - How you felt in the **past week**
    - While taking your current therapies
    - Exclude pain from other known illnesses
    
    **Assessment Components:**
    1. Widespread Pain Index (WPI)
    2. Symptom Severity Score (SS)
    3. Diagnostic Criteria Evaluation
    """)
    
    # Initialize session state
    if 'assessment_complete' not in st.session_state:
        st.session_state.assessment_complete = False
    
    # Create form for the assessment
    with st.form("fibromyalgia_assessment"):
        st.subheader("Part 1: Widespread Pain Index (WPI)")
        st.markdown("""
        **The WPI measures how many body areas have pain (0-19 total areas):**
        - Higher score = pain in more body regions
        - Score of 7+ suggests widespread pain pattern
        
        **Check each area you have felt pain in over the past week:**
        """)
        
        # Create two main columns for Part 1
        col1, col2 = st.columns([3, 2])
        
        with col1:
            # Pain area options
            pain_areas_options = [
                "Shoulder girdle, left", "Shoulder girdle, right",
                "Upper arm, left", "Upper arm, right",
                "Lower arm, left", "Lower arm, right",
                "Hip (buttock) left", "Hip (buttock) right",
                "Upper leg left", "Upper leg right",
                "Lower leg left", "Lower leg right",
                "Jaw left", "Jaw right",
                "Chest", "Abdomen", "Neck",
                "Upper back", "Lower back",
                "None of these areas"
            ]
            
            # Create checkboxes in 4 columns for more compact layout
            pain_cols = st.columns(4)
            selected_pain_areas = []
            
            for i, area in enumerate(pain_areas_options):
                with pain_cols[i % 4]:
                    if st.checkbox(area, key=f"pain_{i}"):
                        selected_pain_areas.append(area)
        
        with col2:
            # Show simple but effective pain area summary
            st.markdown("### Pain Area Summary")
            
            # Group areas by body region
            regions = {
                "🧠 Head/Neck": ['Neck', 'Jaw left', 'Jaw right'],
                "💪 Arms & Shoulders": [
                    'Shoulder girdle, left', 'Shoulder girdle, right',
                    'Upper arm, left', 'Upper arm, right', 
                    'Lower arm, left', 'Lower arm, right'
                ],
                "🫁 Torso": ['Chest', 'Abdomen', 'Upper back', 'Lower back'],
                "🦵 Hips & Legs": [
                    'Hip (buttock) left', 'Hip (buttock) right',
                    'Upper leg left', 'Upper leg right',
                    'Lower leg left', 'Lower leg right'
                ]
            }
            
            total_pain_areas = 0
            for region, areas in regions.items():
                pain_count = sum(1 for area in areas if area in selected_pain_areas and area != "None of these areas")
                total_areas = len(areas)
                percentage = (pain_count / total_areas * 100) if total_areas > 0 else 0
                
                # Display region summary
                st.markdown(f"**{region}**")
                if pain_count > 0:
                    st.progress(percentage / 100)
                    st.markdown(f"🔴 {pain_count}/{total_areas} areas with pain ({percentage:.0f}%)")
                    total_pain_areas += pain_count
                else:
                    st.markdown(f"⚪ No pain in this region (0/{total_areas})")
                st.markdown("")  # Add spacing
            
            # Overall summary
            st.markdown("---")
            st.markdown("**📊 Overall Summary:**")
            st.metric("Total Pain Areas", f"{total_pain_areas}/19", 
                     delta=f"WPI Score: {total_pain_areas}")
            
            # Show selected areas in expandable section
            if selected_pain_areas and "None of these areas" not in selected_pain_areas:
                with st.expander("📋 View All Selected Pain Areas"):
                    for area in selected_pain_areas:
                        if area != "None of these areas":
                            st.write(f"🔴 {area}")
            
            # Add helpful tip
            st.info("💡 **Tip:** A WPI score of 7+ suggests widespread pain pattern")
        
        st.markdown("---")
        
        # Part 2a: Symptom Severity
        st.subheader("Part 2a: Symptom Severity Score (SS)")
        st.markdown("""
        **The SS Score measures how severe your symptoms are (0-12 total):**
        - Part 2a: Core symptoms severity (0-9) - fatigue, sleep, thinking
        - Part 2b: Additional symptoms count (0-3) - how many other symptoms you have
        - Higher score = more severe or numerous symptoms
        
        **Indicate your level of symptom severity over the past week:**
        """)
        
        severity_options = [
            "0 = No problem",
            "1 = Slight or mild problems; generally mild or intermittent", 
            "2 = Moderate; considerable problems; often present and/or at a moderate level",
            "3 = Severe: pervasive, continuous, life disturbing problems"
        ]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("**Fatigue**")
            fatigue_score = st.radio("", severity_options, key="fatigue", format_func=lambda x: x.split(' = ')[0] + " - " + x.split(' = ')[1])
            fatigue_value = int(fatigue_score.split(' = ')[0])
        
        with col2:
            st.markdown("**Waking unrefreshed**")
            waking_score = st.radio("", severity_options, key="waking", format_func=lambda x: x.split(' = ')[0] + " - " + x.split(' = ')[1])
            waking_value = int(waking_score.split(' = ')[0])
        
        with col3:
            st.markdown("**Cognitive symptoms**")
            cognitive_score = st.radio("", severity_options, key="cognitive", format_func=lambda x: x.split(' = ')[0] + " - " + x.split(' = ')[1])
            cognitive_value = int(cognitive_score.split(' = ')[0])
        
        st.markdown("---")
        
        # Part 2b: Other Symptoms
        st.subheader("Part 2b: Other Symptoms")
        st.markdown("""
        **Additional symptoms contribute to your SS score:**
        - 0 symptoms = 0 points | 1-10 symptoms = 1 point
        - 11-24 symptoms = 2 points | 25+ symptoms = 3 points
        
        **Check each of the following OTHER SYMPTOMS that you have experienced over the past week:**
        """)
        
        other_symptoms = [
            "Muscle pain", "Irritable bowel syndrome", "Fatigue/tiredness", "Thinking or remembering problem",
            "Muscle Weakness", "Headache", "Pain/cramps in abdomen", "Numbness/tingling",
            "Dizziness", "Insomnia", "Depression", "Constipation",
            "Pain in upper abdomen", "Nausea", "Nervousness", "Chest pain",
            "Blurred vision", "Fever", "Diarrhea", "Dry mouth",
            "Itching", "Wheezing", "Raynauld's (fingers/toes turn white/blue in cold)", "Hives/welts",
            "Ringing in ears", "Vomiting", "Heartburn", "Oral ulcers",
            "Loss/change in taste", "Seizures", "Dry eyes", "Shortness of breath",
            "Loss of appetite", "Rash", "Sun sensitivity", "Hearing difficulties",
            "Easy bruising", "Hair loss", "Frequent urination", "Painful urination", "Bladder spasms"
        ]
        
        # Display symptoms in 4 columns
        symptom_cols = st.columns(4)
        selected_symptoms = []
        
        for i, symptom in enumerate(other_symptoms):
            with symptom_cols[i % 4]:
                if st.checkbox(symptom, key=f"symptom_{i}"):
                    selected_symptoms.append(symptom)
        
        # Submit button
        st.markdown("---")
        submitted = st.form_submit_button("🔍 Calculate Assessment Results", type="primary")
    
    # Process results when form is submitted
    if submitted:
        st.session_state.assessment_complete = True
        
        # Calculate scores
        wpi_score = calculate_wpi_score(selected_pain_areas)
        ss_2a_score = calculate_ss_score_2a(fatigue_value, waking_value, cognitive_value)
        ss_2b_score = calculate_ss_score_2b(len(selected_symptoms))
        total_ss_score = ss_2a_score + ss_2b_score
        
        # Store results in session state
        st.session_state.wpi_score = wpi_score
        st.session_state.ss_score = total_ss_score
        st.session_state.ss_2a_score = ss_2a_score  
        st.session_state.ss_2b_score = ss_2b_score
        st.session_state.pain_areas = selected_pain_areas
        st.session_state.symptoms = selected_symptoms
        st.session_state.meets_criteria = evaluate_diagnostic_criteria(wpi_score, total_ss_score)
    
    # Display results if assessment is complete
    if st.session_state.assessment_complete:
        st.markdown("---")
        st.markdown("## 📊 Assessment Results")
        
        # Display scores in cards
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class="score-card">
                <h3 style='color: #667eea; margin-bottom: 0;'>WPI Score</h3>
                <h1 style='color: #333; margin-top: 0;'>{}/19</h1>
                <p><strong>Widespread Pain Index</strong><br>
                <small>Counts how many body areas have pain</small></p>
            </div>
            """.format(st.session_state.wpi_score), unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="score-card">
                <h3 style='color: #667eea; margin-bottom: 0;'>SS Score 2a</h3>
                <h1 style='color: #333; margin-top: 0;'>{}/9</h1>
                <p><strong>Core Symptoms Severity</strong><br>
                <small>Fatigue + Sleep + Thinking problems</small></p>
            </div>
            """.format(st.session_state.ss_2a_score), unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="score-card">
                <h3 style='color: #667eea; margin-bottom: 0;'>SS Score 2b</h3>
                <h1 style='color: #333; margin-top: 0;'>{}/3</h1>
                <p><strong>Additional Symptoms</strong><br>
                <small>Based on count of other symptoms</small></p>
            </div>
            """.format(st.session_state.ss_2b_score), unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class="score-card">
                <h3 style='color: #667eea; margin-bottom: 0;'>Total SS Score</h3>
                <h1 style='color: #333; margin-top: 0;'>{}/12</h1>
                <p><strong>Combined Severity Score</strong><br>
                <small>SS 2a + SS 2b = Total symptom burden</small></p>
            </div>
            """.format(st.session_state.ss_score), unsafe_allow_html=True)
        
        # Diagnostic criteria result
        st.markdown("### 🎯 Diagnostic Criteria Assessment")
        
        criteria_class = "meets-criteria" if st.session_state.meets_criteria else "not-meets-criteria"
        criteria_text = "MEETS" if st.session_state.meets_criteria else "DOES NOT MEET"
        criteria_emoji = "✅" if st.session_state.meets_criteria else "❌"
        
        st.markdown(f"""
        <div class="diagnostic-result {criteria_class}">
            {criteria_emoji} Patient {criteria_text} the New Fibromyalgia Diagnostic Criteria
        </div>
        """, unsafe_allow_html=True)
        
        # Detailed explanation
        st.markdown("#### Diagnostic Criteria Breakdown:")
        
        wpi = st.session_state.wpi_score
        ss = st.session_state.ss_score
        
        st.markdown(f"""
        **Criterion 1a:** WPI ≥ 7 AND SS ≥ 5
        - Your WPI: {wpi} ({'✅' if wpi >= 7 else '❌'} {'≥ 7' if wpi >= 7 else '< 7'})
        - Your SS: {ss} ({'✅' if ss >= 5 else '❌'} {'≥ 5' if ss >= 5 else '< 5'})
        - Criterion 1a: {'✅ MET' if wpi >= 7 and ss >= 5 else '❌ NOT MET'}
        
        **Criterion 1b:** WPI 3-6 AND SS ≥ 9  
        - Your WPI: {wpi} ({'✅' if 3 <= wpi <= 6 else '❌'} {'3-6' if 3 <= wpi <= 6 else 'outside 3-6 range'})
        - Your SS: {ss} ({'✅' if ss >= 9 else '❌'} {'≥ 9' if ss >= 9 else '< 9'})
        - Criterion 1b: {'✅ MET' if 3 <= wpi <= 6 and ss >= 9 else '❌ NOT MET'}
        """)
        
        # Visualizations
        col1, col2 = st.columns(2)
        
        with col1:
            # Score comparison chart
            fig_scores = go.Figure()
            
            fig_scores.add_trace(go.Bar(
                name='Your Scores',
                x=['WPI Score', 'SS Score 2a', 'SS Score 2b', 'Total SS'],
                y=[st.session_state.wpi_score, st.session_state.ss_2a_score, 
                   st.session_state.ss_2b_score, st.session_state.ss_score],
                marker_color=['#667eea', '#764ba2', '#f093fb', '#f5576c']
            ))
            
            fig_scores.add_trace(go.Bar(
                name='Maximum Possible',
                x=['WPI Score', 'SS Score 2a', 'SS Score 2b', 'Total SS'],
                y=[19, 9, 3, 12],
                marker_color=['rgba(102,126,234,0.3)', 'rgba(118,75,162,0.3)', 
                             'rgba(240,147,251,0.3)', 'rgba(245,87,108,0.3)']
            ))
            
            fig_scores.update_layout(
                title="Assessment Scores Breakdown",
                barmode='group',
                height=400
            )
            
            st.plotly_chart(fig_scores, use_container_width=True)
        
        with col2:
            # Pain areas distribution
            if st.session_state.pain_areas and "None of these areas" not in st.session_state.pain_areas:
                pain_categories = {
                    'Upper Body': 0, 'Lower Body': 0, 'Core': 0, 'Head/Neck': 0
                }
                
                for area in st.session_state.pain_areas:
                    if 'arm' in area.lower() or 'shoulder' in area.lower():
                        pain_categories['Upper Body'] += 1
                    elif 'leg' in area.lower() or 'hip' in area.lower():
                        pain_categories['Lower Body'] += 1
                    elif 'chest' in area.lower() or 'abdomen' in area.lower() or 'back' in area.lower():
                        pain_categories['Core'] += 1
                    elif 'jaw' in area.lower() or 'neck' in area.lower():
                        pain_categories['Head/Neck'] += 1
                
                fig_pain = px.pie(
                    values=list(pain_categories.values()),
                    names=list(pain_categories.keys()),
                    title="Pain Distribution by Body Region",
                    color_discrete_sequence=['#667eea', '#764ba2', '#f093fb', '#f5576c']
                )
                fig_pain.update_layout(height=400)
                
                st.plotly_chart(fig_pain, use_container_width=True)
            else:
                st.info("No pain areas selected for visualization")
        
        # Additional information  
        st.markdown("---")
        st.markdown("### 📋 Assessment Summary")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Pain Areas Selected:**")
            if st.session_state.pain_areas:
                for area in st.session_state.pain_areas:
                    if area != "None of these areas":
                        st.markdown(f"• {area}")
            else:
                st.markdown("• None selected")
        
        with col2:
            st.markdown(f"**Other Symptoms Selected:** ({len(st.session_state.symptoms)} total)")
            if st.session_state.symptoms:
                # Show first 10 symptoms, then indicate if there are more
                for symptom in st.session_state.symptoms[:10]:
                    st.markdown(f"• {symptom}")
                if len(st.session_state.symptoms) > 10:
                    st.markdown(f"• ... and {len(st.session_state.symptoms) - 10} more")
            else:
                st.markdown("• None selected")
        
        # Export functionality
        st.markdown("---")
        st.markdown("### 💾 Export Results")
        
        # Create export data
        export_data = {
            "assessment_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "wpi_score": st.session_state.wpi_score,
            "ss_2a_score": st.session_state.ss_2a_score,
            "ss_2b_score": st.session_state.ss_2b_score,
            "total_ss_score": st.session_state.ss_score,
            "meets_diagnostic_criteria": st.session_state.meets_criteria,
            "pain_areas": st.session_state.pain_areas,
            "other_symptoms": st.session_state.symptoms
        }
        
        # JSON download
        json_str = json.dumps(export_data, indent=2)
        st.download_button(
            label="📄 Download Results (JSON)",
            data=json_str,
            file_name=f"fibromyalgia_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json"
        )
        
        # CSV download
        results_df = pd.DataFrame([{
            'Assessment Date': export_data['assessment_date'],
            'WPI Score': export_data['wpi_score'],
            'SS 2a Score': export_data['ss_2a_score'], 
            'SS 2b Score': export_data['ss_2b_score'],
            'Total SS Score': export_data['total_ss_score'],
            'Meets Criteria': export_data['meets_diagnostic_criteria'],
            'Pain Areas Count': len([a for a in export_data['pain_areas'] if a != "None of these areas"]),
            'Other Symptoms Count': len(export_data['other_symptoms'])
        }])
        
        csv_str = results_df.to_csv(index=False)
        st.download_button(
            label="📊 Download Results (CSV)",
            data=csv_str,
            file_name=f"fibromyalgia_assessment_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
            mime="text/csv"
        )
        
        # Reset button
        if st.button("🔄 Start New Assessment", type="secondary"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.experimental_rerun()
    
    # Footer with disclaimer
    st.markdown("---")
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 1rem; border-radius: 10px; margin-top: 2rem;'>
        <h4>⚠️ Important Medical Disclaimer</h4>
        <p><strong>This survey is not meant to substitute for a diagnosis by a medical professional.</strong></p>
        <p>Patients should not diagnose themselves. Always consult your medical professional for advice and treatment. 
        This assessment is intended to give insight into research on diagnostic criteria and symptom severity measurement for fibromyalgia.</p>
        <p><em>Based on: Wolfe F, et al. Arthritis Care Res DOI 10.1002/acr.20140. Fibromyalgia Network.</em></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()