import streamlit as st
import time

st.set_page_config(page_title="GCI Rater", layout="centered")

st.title("GCI Rating System")

# --- Specimen Details ---
specimen_name = st.text_input("Enter the name of the specimen (person to be rated):")
agree = st.checkbox("I agree to fairly imagine the person and reconsider each rating carefully for unbiased results.")

if not agree:
    st.warning("Please check the box above to continue.")
    st.stop()

# --- Outer Factors ---
st.header("Outer Factors")
outer_factors = {
    "Skin Tone (evenness, relative to rater's taste)": st.slider("Skin Tone", 0, 20, 10),
    "Lower Face (lips, jaw)": st.slider("Lower Face", 0, 20, 10),
    "Body Shape": st.slider("Body Shape", 0, 20, 10),
    "Hair & Grooming": st.slider("Hair & Grooming", 0, 20, 10),
    "Style & Dress Sense": st.slider("Style & Dress Sense", 0, 20, 10),
}

# --- 15-second pause after outer factors ---
st.info("Take a moment to reconsider your ratings and visualize carefully.")
with st.spinner("Reconsidering outer factors..."):
    time.sleep(15)

# --- Inner Factors ---
st.header("Inner Factors")
inner_factors = {
    "Communication": st.slider("Communication", 0, 20, 10),
    "Humor": st.slider("Humor", 0, 20, 10),
    "Confidence & Maturity": st.slider("Confidence & Maturity", 0, 20, 10),
    "Social Behavior": st.slider("Social Behavior", 0, 20, 10),
    "Attitude (down-to-earth)": st.slider("Attitude", 0, 20, 10),
}

# --- 15-second pause after inner factors ---
st.info("Take a moment to reconsider your inner ratings as well.")
with st.spinner("Reconsidering inner factors..."):
    time.sleep(15)

# --- R-Factor ---
st.header("R-Factor (Rawness Level)")
r_score = st.slider("Give a raw score (0 to 5, fractional allowed)", 0.0, 5.0, 2.0, step=0.1)

# Determine R codename and percentage change
if r_score < 0.5:
    r_code, change = "Sati Savitri", 0.25
elif r_score < 1.5:
    r_code, change = "Virgin", 0.20
elif r_score < 2.5:
    r_code, change = "Nibbi", 0.00
elif r_score < 3.5:
    r_code, change = "Leony", -0.10
elif r_score < 4.5:
    r_code, change = "Munni Badnam", -0.23
else:
    r_code, change = "Gangubai Tier", -0.29

# --- Final Calculation ---
total_outer = sum(outer_factors.values())
total_inner = sum(inner_factors.values())

raw_score = 0.4 * total_outer + 0.6 * total_inner
final_score = raw_score * (1 + change)
final_score /= 10  # Normalize to a 0–10 scale

# --- Display Result ---
st.success(f"{final_score:.2f} GCI - {r_code}")

st.caption("This rating is a fictional metric for observation and fun only. Not to be taken seriously.")
