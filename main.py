import streamlit as st
import time

st.set_page_config(page_title="GCI Rater", page_icon="✨")
st.title("GCI Rater")

# State Management
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "outer_score" not in st.session_state:
    st.session_state.outer_score = None
if "inner_score" not in st.session_state:
    st.session_state.inner_score = None
if "name" not in st.session_state:
    st.session_state.name = ""

# R level info
r_level_names = {
    0: "Sati Savitri",
    1: "Virgin",
    2: "Nibbi",
    3: "Leony",
    4: "Munni Badnam",
    5: "Gangubai Tier"
}

r_level_percent = {
    0: 0.25,
    1: 0.20,
    2: 0.00,
    3: -0.10,
    4: -0.23,
    5: -0.29
}

# Stage 0: Enter Name and Read Instructions
if st.session_state.stage == 0:
    st.session_state.name = st.text_input("Enter the name of the specimen")
    agree = st.checkbox("I agree to fairly imagine the person and reconsider the points before rating")
    if st.button("Start") and st.session_state.name and agree:
        st.session_state.stage = 1
        st.experimental_rerun()

# Stage 1: Outer Rating
elif st.session_state.stage == 1:
    st.subheader("Outer Rating")
    st.session_state.outer_score = st.slider("Give outer score (look, body, skin tone, features etc.)", 0, 100)
    if st.button("Next (Reconsider Outer)"):
        st.markdown("### Reconsider: Think again!")
        with st.spinner("Reevaluating outer in 15 seconds..."):
        st.session_state.stage = 2
        st.experimental_rerun()

# Stage 2: Inner Rating
elif st.session_state.stage == 2:
    st.subheader("Inner Rating")
    humor = st.slider("Humor (jokes, mimicry, facial expressions, fun)", 0, 100)
    communication = st.slider("Communication (voice, speech, vibe, depth, clarity)", 0, 100)
    attitude = st.slider("Attitude (humility, nature, vibe, maturity)", 0, 100)
    inner_avg = (humor + communication + attitude) / 3
    st.session_state.inner_score = inner_avg
    if st.button("Next (Reconsider Inner)"):
        st.markdown("### Reconsider: Reflect again!")
        with st.spinner("Reevaluating inner in 15 seconds..."):
        st.session_state.stage = 3
        st.experimental_rerun()

# Stage 3: R Level and Final Calculation
elif st.session_state.stage == 3:
    st.subheader("R-Level (Rawness)")
    r_value = st.slider("Give rawness score (0 to 5, fractional allowed)", 0.0, 5.0, step=0.1)

    # Determine code name and percentage
    r_floor = int(r_value)
    r_level_name = r_level_names[r_floor if r_value < r_floor + 0.5 else min(r_floor + 1, 5)]
    r_percent = r_level_percent[r_floor if r_value < r_floor + 0.5 else min(r_floor + 1, 5)]

    if st.button("Show Final Result"):
        outer_component = 0.4 * st.session_state.outer_score
        inner_component = 0.6 * st.session_state.inner_score
        raw_result = outer_component + inner_component
        final_result = raw_result * (1 + r_percent)
        gci_score = round(final_result / 10, 2)

        st.success(f"**{gci_score} GCI {r_level_name}**")
        st.balloons()
