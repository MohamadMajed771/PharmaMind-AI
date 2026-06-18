import streamlit as st
from services.drug_ai_service import analyze_drug
from services.drug_validator import find_drug_match, drug_names

st.set_page_config(
    page_title="PharmaMind AI",
    page_icon="💊",
    layout="wide"
)

st.markdown("""
<style>
.big-title {
    font-size: 46px;
    font-weight: 800;
}
.subtitle {
    font-size: 20px;
    color: #555;
    margin-bottom: 20px;
}
.info-card {
    background-color: #F8FAFC;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #E5E7EB;
}
.warning-card {
    background-color: #FFF7E6;
    padding: 15px;
    border-radius: 12px;
    border-left: 5px solid #F59E0B;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">💊 PharmaMind AI</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A local AI drug information assistant for pharmacy students</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="warning-card">
<strong>Educational use only.</strong> Always verify dosing, contraindications, and interactions with official drug references.
</div>
""", unsafe_allow_html=True)

st.divider()

drug_name = st.text_input(
    "Search for a drug",
    placeholder="Type any drug name, example: Paracetamol, Zeta, Amoxicillin"
)

if st.button("🔍 Analyze Drug", use_container_width=True):
    if not drug_name.strip():
        st.warning("Please enter or select a drug name.")
        st.stop()

    matched_drug = find_drug_match(drug_name)

    if matched_drug is None:
        st.error("Drug not found.")
        st.info(f'No close drug name was found for "{drug_name}". Please check the spelling.')
        st.stop()

    if matched_drug.lower() != drug_name.lower():
        st.warning(f'No exact match found for "{drug_name}". Using closest match: "{matched_drug}".')

    with st.spinner("Generating pharmacist-level monograph..."):
        data = analyze_drug(matched_drug)

    st.success("Analysis completed.")

    st.markdown(f"## {data.get('drug_name', matched_drug)}")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="info-card">
        <strong>Generic Name</strong><br>
        {data.get("generic_name", "N/A")}
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="info-card">
        <strong>Drug Class</strong><br>
        {data.get("drug_class", "N/A")}
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="info-card">
        <strong>Therapeutic Category</strong><br>
        {data.get("therapeutic_category", "N/A")}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("### Quick Summary")
    st.info(data.get("quick_summary", "No summary available."))

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📘 Overview",
        "💉 Dosing",
        "⚠️ Safety",
        "🔄 Interactions",
        "🗣️ Counseling",
        "🎓 Exam Focus"
    ])

    with tab1:
        st.subheader("Brand Names")
        st.write(data.get("brand_names", "N/A"))

        st.subheader("Indications")
        st.write(data.get("indications", "N/A"))

        st.subheader("Mechanism of Action")
        st.write(data.get("mechanism", "N/A"))

        st.subheader("Pharmacokinetics")
        st.write(data.get("pharmacokinetics", "N/A"))

    with tab2:
        st.subheader("Adult Dose")
        st.write(data.get("adult_dose", "N/A"))

        st.subheader("Pediatric Dose")
        st.write(data.get("pediatric_dose", "N/A"))

        st.subheader("Renal Dose Adjustment")
        st.write(data.get("renal_adjustment", "N/A"))

        st.subheader("Hepatic Dose Adjustment")
        st.write(data.get("hepatic_adjustment", "N/A"))

    with tab3:
        st.subheader("Contraindications")
        st.write(data.get("contraindications", "N/A"))

        st.subheader("Warnings and Precautions")
        st.write(data.get("warnings", "N/A"))

        st.subheader("Common Side Effects")
        st.write(data.get("common_side_effects", "N/A"))

        st.subheader("Serious Side Effects")
        st.write(data.get("serious_side_effects", "N/A"))

        st.subheader("Toxicity and Overdose")
        st.write(data.get("toxicity_overdose", "N/A"))

    with tab4:
        st.subheader("Drug-Drug Interactions")
        st.write(data.get("drug_interactions", "N/A"))

        st.subheader("Drug-Food Interactions")
        st.write(data.get("food_interactions", "N/A"))

        st.subheader("Pregnancy and Lactation")
        st.write(data.get("pregnancy_lactation", "N/A"))

        st.subheader("Monitoring Parameters")
        st.write(data.get("monitoring", "N/A"))

    with tab5:
        st.subheader("Patient Counseling Points")
        st.write(data.get("counseling", "N/A"))

        st.subheader("Pharmacist Clinical Pearls")
        st.write(data.get("clinical_pearls", "N/A"))

    with tab6:
        st.subheader("High-Yield Exam Points")
        st.write(data.get("exam_focus", "N/A"))