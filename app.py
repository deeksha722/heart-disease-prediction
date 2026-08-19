import streamlit as st
import pandas as pd
import joblib


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="Cardio AI",
    page_icon="❤️",
    layout="wide"
)


# =========================================================
# LIGHT THEME + UI DESIGN
# =========================================================

st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

/* Main container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: #d6336c;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 19px;
    color: #64748b;
    margin-bottom: 35px;
}

/* Section headings */
.section-title {
    font-size: 24px;
    font-weight: 700;
    color: #2563eb;
    margin-top: 20px;
    margin-bottom: 15px;
}

/* Input labels */
label {
    font-weight: 600 !important;
    color: #334155 !important;
}

/* Number inputs */
.stNumberInput input {
    background-color: white !important;
    color: #1e293b !important;
    border: 1px solid #cbd5e1 !important;
}

/* Select boxes */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: white !important;
    color: #1e293b !important;
    border: 1px solid #cbd5e1 !important;
}

/* Predict button */
.stButton > button {
    width: 100%;
    height: 60px;
    border-radius: 12px;
    border: none;
    background-color: #d6336c;
    color: white;
    font-size: 21px;
    font-weight: 700;
    margin-top: 25px;
}

.stButton > button:hover {
    background-color: #b82d5c;
    color: white;
}

/* Result cards */
.result-high {
    background-color: #fff1f2;
    border-left: 7px solid #e11d48;
    border-radius: 12px;
    padding: 25px;
    margin-top: 25px;
    text-align: center;
}

.result-low {
    background-color: #ecfdf5;
    border-left: 7px solid #059669;
    border-radius: 12px;
    padding: 25px;
    margin-top: 25px;
    text-align: center;
}

.result-title {
    font-size: 28px;
    font-weight: 800;
    color: #1e293b;
}

.result-text {
    font-size: 18px;
    color: #475569;
    margin-top: 10px;
}

/* Info cards */
.info-card {
    background-color: white;
    border-radius: 12px;
    padding: 20px;
    border: 1px solid #e2e8f0;
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD MODEL AND ENCODERS
# =========================================================

model = joblib.load("heart_disease_rf_model.pkl")

label_encoders = joblib.load("label_encoders.pkl")

onehot_encoder = joblib.load("onehot_encoder.pkl")


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">❤️ CARDIO AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Heart Disease Prediction System</div>',
    unsafe_allow_html=True
)


# =========================================================
# PATIENT INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Patient Information</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=50
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col3:
    heart_rate = st.number_input(
        "Heart Rate",
        min_value=0,
        max_value=250,
        value=75
    )


# =========================================================
# CLINICAL MEASUREMENTS
# =========================================================

st.markdown(
    '<div class="section-title">🩺 Clinical Measurements</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    cholesterol = st.number_input(
        "Cholesterol",
        min_value=0,
        max_value=500,
        value=200
    )

with col2:
    blood_pressure = st.number_input(
        "Blood Pressure",
        min_value=0,
        max_value=250,
        value=120
    )

with col3:
    blood_sugar = st.number_input(
        "Blood Sugar",
        min_value=0,
        max_value=500,
        value=120
    )


# =========================================================
# LIFESTYLE
# =========================================================

st.markdown(
    '<div class="section-title">🏃 Lifestyle</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    exercise_hours = st.number_input(
        "Exercise Hours",
        min_value=0.0,
        max_value=24.0,
        value=4.0
    )

with col2:
    stress_level = st.number_input(
        "Stress Level",
        min_value=0,
        max_value=10,
        value=5
    )

with col3:
    smoking = st.selectbox(
        "Smoking",
        ["Current", "Former", "Never"]
    )


# =========================================================
# MEDICAL HISTORY
# =========================================================

st.markdown(
    '<div class="section-title">🧬 Medical History</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    family_history = st.selectbox(
        "Family History",
        ["No", "Yes"]
    )

with col2:
    diabetes = st.selectbox(
        "Diabetes",
        ["No", "Yes"]
    )

with col3:
    obesity = st.selectbox(
        "Obesity",
        ["No", "Yes"]
    )

with col4:
    exercise_induced_angina = st.selectbox(
        "Exercise Induced Angina",
        ["No", "Yes"]
    )


# =========================================================
# ADDITIONAL INFORMATION
# =========================================================

st.markdown(
    '<div class="section-title">❤️ Additional Information</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    alcohol_intake = st.selectbox(
        "Alcohol Intake",
        ["Heavy", "Moderate", "Unknown"]
    )

with col2:
    chest_pain_type = st.selectbox(
        "Chest Pain Type",
        [
            "Asymptomatic",
            "Atypical Angina",
            "Non-anginal Pain",
            "Typical Angina"
        ]
    )


# =========================================================
# PREDICT BUTTON
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)

predict_button = st.button(
    "🔍 ANALYZE HEART HEALTH"
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    # -----------------------------------------------
    # Label Encoding
    # -----------------------------------------------

    gender_encoded = label_encoders[
        "Gender"
    ][gender]

    family_history_encoded = label_encoders[
        "Family History"
    ][family_history]

    diabetes_encoded = label_encoders[
        "Diabetes"
    ][diabetes]

    obesity_encoded = label_encoders[
        "Obesity"
    ][obesity]

    exercise_angina_encoded = label_encoders[
        "Exercise Induced Angina"
    ][exercise_induced_angina]


    # -----------------------------------------------
    # One Hot Encoding
    # -----------------------------------------------

    categorical_input = pd.DataFrame({
        "Smoking": [smoking],
        "Alcohol Intake": [alcohol_intake],
        "Chest Pain Type": [chest_pain_type]
    })

    encoded_input = onehot_encoder.transform(
        categorical_input
    )

    encoded_input_df = pd.DataFrame(
        encoded_input,
        columns=onehot_encoder.get_feature_names_out(
            [
                "Smoking",
                "Alcohol Intake",
                "Chest Pain Type"
            ]
        )
    )


    # -----------------------------------------------
    # Create input dataframe
    # -----------------------------------------------

    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender_encoded],
        "Cholesterol": [cholesterol],
        "Blood Pressure": [blood_pressure],
        "Heart Rate": [heart_rate],
        "Exercise Hours": [exercise_hours],
        "Family History": [family_history_encoded],
        "Diabetes": [diabetes_encoded],
        "Obesity": [obesity_encoded],
        "Stress Level": [stress_level],
        "Blood Sugar": [blood_sugar],
        "Exercise Induced Angina": [
            exercise_angina_encoded
        ]
    })


    # -----------------------------------------------
    # Combine all features
    # -----------------------------------------------

    input_data = pd.concat(
        [input_data, encoded_input_df],
        axis=1
    )


    # -----------------------------------------------
    # Match training feature order
    # -----------------------------------------------

    input_data = input_data[
        model.feature_names_in_
    ]


    # -----------------------------------------------
    # Prediction
    # -----------------------------------------------

    prediction = model.predict(
        input_data
    )[0]

    probability = model.predict_proba(
        input_data
    )[0]

    risk_probability = probability[1] * 100


    # -----------------------------------------------
# Display result
# -----------------------------------------------

st.markdown("---")

if prediction == 1:

    st.error(
        "⚠️ HEART DISEASE RISK DETECTED"
    )

    st.write(
        "The model predicts a higher likelihood "
        "of heart disease."
    )

    st.metric(
        "Model Probability",
        f"{risk_probability:.2f}%"
    )

else:

    st.success(
        "💚 LOW HEART DISEASE RISK"
    )

    st.write(
        "The model predicts a lower likelihood "
        "of heart disease."
    )

    st.metric(
        "Model Probability",
        f"{risk_probability:.2f}%"
    )
st.markdown(
    """
    <div class="footer">
        ❤️ Cardio AI | Machine Learning Project
    </div>
    """,
    unsafe_allow_html=True
)