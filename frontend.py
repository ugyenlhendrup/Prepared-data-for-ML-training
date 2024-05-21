import streamlit as st
import pickle

def all_zero(arr):
    for element in arr:
        if element != 0:
            return False
    return True

# Load the model
with open('svm_model.sav', 'rb') as f:
    loaded_modelRFG = pickle.load(f)

# Title with logos
col1, col2, col3 = st.columns([1, 4, 1])
with col1:
    st.image("rublogo.jpeg.png", use_column_width=True)
with col2:
    st.markdown("<h3 style='text-align: center; color: black; line-height:0.5'>Leakage Detector</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: black;'>Use of ML for Detection and Localization of Leakage in Water Distribution Network-CST<br>Civil Engineering Department</h5>", unsafe_allow_html=True)
with col3:
    st.image("collegelogo.jpeg.png", use_column_width=True)

# List to store user inputs
user_inputs = []
labels = ['Tank Level', 'Junc IP1', 'Junc IP2', 'Junc IP3', 'Junc IP4', 'Junc IP5', 'Junc PZ1', 'Junc PZ2', 'Junc PZ3', 'Junc PZ4']

col1, col2 = st.columns(2)

with col1:
    for i in range(0, 5):
        user_input = st.number_input(label=f"Enter Input for {labels[i]}", step=1., format="%.2f")
        user_inputs.append(float(user_input))
with col2:
    for i in range(5, 10):
        user_input = st.number_input(label=f"Enter Input for {labels[i]}", step=1., format="%.2f")
        user_inputs.append(float(user_input))

# Button to trigger output
if st.button("Predict Leakage"):
    # Display all collected inputs
    if all_zero(user_inputs):
        st.write(f"All the values are zero!! change the values!!")
    else:
        st.header("Result")
        ans = loaded_modelRFG.predict([[user_inputs[7], user_inputs[6], user_inputs[0], user_inputs[8], user_inputs[9], user_inputs[2], user_inputs[1], user_inputs[3], user_inputs[4], user_inputs[5]]])
        st.write(f"Leakage at: {ans[0]}")

st.subheader("Project Members")
st.text("Project Guide: Dr. Sangey Pasang")
st.text("Project Member: Ugyen Lhendrup")
st.text("Project Member: Yeshey Tshogyel")
st.text("Project Member: Mindu Dorji")
#python -m streamlit run frontend.py