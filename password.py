import re
import streamlit as st
import random       # randommly generate password
import string       # The string module contains constants for different sets of characters, which are useful when creating a strong password.

st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")

st.header("✨ ✨ 🔐 Password Strength Meter ✨ ✨ ")

st.markdown("<br>", unsafe_allow_html=True) # Adds a simple line break.

def check_password_strength (password) :

    score = 0

    # Length Check
    if len(password) >= 8 :
        score += 1
    else: 
        st.write("❌ Password must be at least 8 characters long.")

    # check uppercase & lowercase letters
    if  re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else: 
        st.write("❌ Include both uppercase and lowercase letters.")


    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        st.write("❌ Add at least one number (0-9).")
 
    # Special Character Check
    if re.search(r'[!@#$%^&*()]', password):
        score += 1
    else:
        st.write("❌ Include at least one special character ([!@#$%^&*().")
    
    # Strength Rating
    if score == 4 :
        st.write("Feedback: ✅ Strong Passward")
    elif score == 3 :
         st.write("Feedback: ⚠️ Moderate Password - Consider enhancing your security features!")
    else:
        st.write("Feedback: ❌ Weak Password - Please Improve it using the suggestions above.")

    # Generate Stronge Password
def generate_strong_password():

    length = 8

        # Combine uppercase, lowercase, digits, and special characters
    all_password_character = string.ascii_letters + string.digits + "!@#$%^&*()"

    #                   random.choice() function is used to randomly select an item from a given sequence (in this case, the all_characters string). 
    password = "".join(random.choice(all_password_character) for i in range(length))
            # .join(), they are combined into a single string (e.g., 'Ad1@').
    return password


# Get user input
password = st.text_input(":blue[Please Enter your Password: ]")
st.markdown("<br>", unsafe_allow_html=True) # Adds a simple line break.


col1, col2 = st.columns(2)

# Button for checking password strength
with col1 :
    if st.button("💪 Check Password Strength") :
        check_password_strength(password)


# Button for suggesting a strong password
with col2 :
    if st.button(" 🔥 Suggest Strong Password"):
        suggested_password = generate_strong_password()
        st.write(f"Suggested Strong Password: {suggested_password}")



# Custom background color using CSS
st.markdown("""
    <style>
    body {
        background-color: #87CEEB;
          
    }
    .stApp {    
        background-color: #87CEEB;
        color:blue
    
    }
    </style>
""", unsafe_allow_html=True)