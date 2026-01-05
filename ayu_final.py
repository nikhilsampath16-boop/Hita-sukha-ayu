import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AyuBalance",
    page_icon="🌿",
    layout="wide"
)

# ---------------- DARK MODE STYLE ----------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: #EAEAEA;
}
.block-container {
    padding-top: 1.5rem;
}
img {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align:center;'>🌿 AyuBalance</h1>
<p style='text-align:center; color:#A0A0A0;'>
Hita & Sukha Ayu – Wellbeing & Happiness Analyzer<br>
<i>Indian Knowledge System</i>
</p>
""", unsafe_allow_html=True)

st.divider()

# ---------------- LAYOUT ----------------
left, right = st.columns([1.7, 1])

with left:
    st.subheader("Lifestyle & Mental Wellbeing Assessment")

    # ---- YES / NO QUESTIONS (4) ----
    st.markdown("### Daily Discipline (Yes / No)")

    q1 = st.radio("1. Do you maintain regular sleep and wake-up timings?", ["Yes", "No"])
    q2 = st.radio("2. Do you eat meals at proper and fixed times?", ["Yes", "No"])
    q3 = st.radio("3. Do you consciously control screen/mobile usage?", ["Yes", "No"])
    q4 = st.radio("4. Do you practice ethical behaviour and self-discipline?", ["Yes", "No"])

    st.divider()

    # ---- SCALE QUESTIONS (6) ----
    st.markdown("### Self-Evaluation (1 = Very Poor, 10 = Excellent)")

    q5 = st.slider("5. Quality of sleep", 1, 10, 6)
    q6 = st.slider("6. Physical activity / yoga consistency", 1, 10, 5)
    q7 = st.slider("7. Mental calmness and emotional balance", 1, 10, 6)
    q8 = st.slider("8. Stress management ability", 1, 10, 5)
    q9 = st.slider("9. Focus and clarity in studies/work", 1, 10, 6)
    q10 = st.slider("10. Overall satisfaction with life", 1, 10, 6)

with right:
    st.image(
        "https://images.unsplash.com/photo-1506126613408-eca07ce68773",
        width=220,
        caption="Balance of Body and Mind"
    )
    st.image(
        "https://images.unsplash.com/photo-1499209974431-9dddcece7f88",
        width=220,
        caption="Discipline leads to Happiness"
    )

# ---------------- EVALUATION ----------------
st.divider()

if st.button("🌼 Evaluate My Wellbeing"):
    total_score = 0
    issues = []

    # ---- YES / NO QUESTIONS (4 × 10 = 40) ----
    yn_answers = [q1, q2, q3, q4]
    yn_labels = [
        "Irregular sleep routine",
        "Poor eating discipline",
        "Excessive screen usage",
        "Lack of ethical self-control"
    ]

    for ans, label in zip(yn_answers, yn_labels):
        if ans == "Yes":
            total_score += 10
        else:
            issues.append(label)

    # ---- SCALE QUESTIONS (6 × 10 = 60) ----
    scale_values = [q5, q6, q7, q8, q9, q10]
    scale_labels = [
        "Sleep quality",
        "Physical activity",
        "Mental calmness",
        "Stress handling",
        "Focus & clarity",
        "Life satisfaction"
    ]

    for val, label in zip(scale_values, scale_labels):
        total_score += val
        if val < 5:
            issues.append(label)

    # ---- FINAL SCORE (OUT OF 100) ----
    percentage = total_score

    # ---------------- RESULT ----------------
    st.subheader("Your Wellbeing Result")

    if percentage >= 75:
        st.success("🌸 SUKHA AYU – A balanced, disciplined and happy life")
    elif percentage >= 45:
        st.warning("🌼 MADHYAMA AYU – Moderate wellbeing, improvement required")
    else:
        st.error("🌱 ASUKHA AYU – Lifestyle imbalance affecting happiness")

    st.metric("Overall Wellbeing Score", f"{percentage} / 100")

    # ---------------- DIAGNOSIS ----------------
    st.subheader("What is Lacking in You")

    if issues:
        for item in sorted(set(issues)):
            st.write(f"• {item}")
    else:
        st.write("• No major lifestyle imbalance detected")

    # ---------------- IMPROVEMENTS ----------------
    st.subheader("What You Should Improve & What It Will Lead To")

    improvement_map = {
        "Irregular sleep routine": "Fix sleep timing → better energy, memory and mood",
        "Poor eating discipline": "Regular meals → improved digestion and emotional stability",
        "Excessive screen usage": "Reduce screen time → reduced stress and improved focus",
        "Physical activity": "Daily movement/yoga → improved physical and mental health",
        "Mental calmness": "Meditation/mindfulness → emotional balance",
        "Stress handling": "Stress control → long-term peace",
        "Focus & clarity": "Improved focus → productivity and confidence",
        "Life satisfaction": "Balanced lifestyle → inner contentment"
    }

    shown = False
    for issue in set(issues):
        for key in improvement_map:
            if key in issue:
                st.write(f"• {improvement_map[key]}")
                shown = True

    if not shown:
        st.write("• Continue maintaining your current healthy lifestyle")

    # ---------------- OUTCOME ----------------
    st.subheader("Expected Outcome After Improvement")
    st.write("""
    ✔ Improved physical wellbeing  
    ✔ Emotional stability  
    ✔ Reduced stress and anxiety  
    ✔ Better focus and productivity  
    ✔ Sustainable happiness (Sukha Ayu)
    """)

# ---------------- FOOTER ----------------
st.divider()
st.caption("AyuBalance • Dark Mode Streamlit App • Based on Hita & Sukha Ayu (Indian Knowledge Systems)")
