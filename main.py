import streamlit as st

st.set_page_config(page_title="GCI Rater", layout="centered")

st.title("🔍 GCI Rater")

# Specimen Info
specimen_name = st.text_input("Enter Specimen's Name")
show_instructions = st.checkbox("Show Instructions")
if show_instructions:
    st.info("Imagine the person clearly and rate fairly after reconsidering for unbiased results.")

st.markdown("---")

# OUTER FACTORS
st.header(" Outer Factors")
st.caption("(Sliders show values out of 10. Internally weighted differently.)")

def slider(label, max_val):
    return st.slider(label, 0.0, 10.0, step=0.1)

# Define outer subfactors (UI shows /10, backend uses custom weight)
outer_weights = {
    "Face": 12,
    "Lower Face (Lips + Jaw)": 12,
    "Body Shape": 12,
    "Skin": 8,
    "Posture": 8,
    "Walking & Style": 8,
    "Expressions in Situations": 8
}

outer_scores = {}
for label in outer_weights:
    outer_scores[label] = slider(label, 10)

imperfection = st.slider("Imperfection Overall (−12 to 0)", -12.0, 0.0, step=0.1)

st.markdown("---")

# INNER FACTORS
st.header("Inner Factors")
inner_weights = {
    "Working Intelligence": 20,
    "Social Intelligence": 20,
    "Conversational Intelligence": 20,
    "Femininity": 20,
    "Nature (Caring vs Selfish)": 20
}

inner_scores = {}
for label in inner_weights:
    inner_scores[label] = slider(label, 10)

st.markdown("---")

# R-FACTOR
st.header("R-Factor")
r_value = st.slider("Rate from 0 (Pure) to 5 (Extremely Exposed)", 0.0, 5.0, step=0.1)

# R-level mapping and effect
r_levels = [
    (0.0, 0.99, "SatiSavitri", +0.20),
    (1.0, 1.99, "Virgin", +0.20),
    (2.0, 2.49, "CucumberExp", +0.04),
    (2.5, 3.49, "Leony tier", -0.17),
    (3.5, 4.49, "CertifiedSlut", -0.24),
    (4.5, 5.0, "Gangubai tier", -0.30),
]

r_code, r_modifier = None, 0
for low, high, code, mod in r_levels:
    if low <= r_value <= high:
        r_code, r_modifier = code, mod
        break

# CALCULATIONS
outer_total = sum((outer_scores[key] / 10) * outer_weights[key] for key in outer_weights)
outer_total += imperfection  # Deduct imperfection
outer_total = max(0, outer_total)  # Prevent negative outer score

inner_total = sum((inner_scores[key] / 10) * inner_weights[key] for key in inner_weights)

final_raw = 0.4 * outer_total + 0.6 * inner_total
final_modified = final_raw * (1 + r_modifier)
final_display = round(final_modified / 10, 2)  # Final GCI out of 10

if specimen_name:
    st.markdown("---")
    st.subheader("📊 Final GCI Rating")
    st.success(f"**{final_display} GCI {r_code}** for {specimen_name}")
