import streamlit as st

# Electron configuration for atoms 1-118
electron_config = {
    1: "1s1",
    2: "1s2",
    3: "1s2 2s1",
    4: "1s2 2s2",
    5: "1s2 2s2 2p1",
    6: "1s2 2s2 2p2",
    7: "1s2 2s2 2p3",
    8: "1s2 2s2 2p4",
    9: "1s2 2s2 2p5",
    10:"1s2 2s2 2p6",
    11:"1s2 2s2 2p6 3s1",
    12:"1s2 2s2 2p6 3s2",
}

st.title("Electron Configuration")
st.write("Select an atomic number:")

atomic_number = st.selectbox("Atomic Number", list(electron_config.keys()))

st.write("Electron Configuration:")
st.write(electron_config[atomic_number])