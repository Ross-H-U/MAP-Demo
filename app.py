import streamlit as st

st.title("Mean Arterial Pressure (MAP) Calculator")

st.write("This calculator computes the Mean Arterial Pressure (MAP) based on systolic and diastolic blood pressures.")

sbp = st.number_input("Enter Systolic Blood Pressure (SBP) in mmHg:", min_value=0, step=1)
dbp = st.number_input("Enter Diastolic Blood Pressure (DBP) in mmHg:", min_value=0, step=1)

if st.button("Calculate MAP"):
    if sbp > 0 and dbp > 0:
        map_value = dbp + (sbp - dbp) / 3
        st.success(f"Mean Arterial Pressure (MAP) = {map_value:.2f} mmHg")
    else:
        st.warning("Please enter valid SBP and DBP values.")
