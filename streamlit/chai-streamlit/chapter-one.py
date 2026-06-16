import streamlit as st

# st.title("Hello Chai App")
# st.subheader("Brewed with streamlit")
# st.text("Welcome to your first Interactive app")
# st.write("Choose your fav. variety of chai")

# chai = st.selectbox("Your fav chai: ", ["Masala Chai", "Lemon Tea", "Adrak Chai", "Kesar chai"])
# st.write(f"You choose {chai}. Excellent choice")

# st.success("Your chai has been brewed")

st.title("Hello Chai App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first Interactive app")
st.write("Choose your fav. variety of coding language")

chai = st.selectbox("Your fav chai: ", ["C", "C++", "JAVA", "PYTHON", "Rust"])
st.write(f"You choose {chai}. Excellent choice")

st.success("Your chai has been brewed")