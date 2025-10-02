import streamlit as st
import string
import secrets
from streamlit_copy_to_clipboard import st_copy_to_clipboard

# --- App Configuration ---
st.set_page_config(page_title="Password Generator", page_icon="🔐", layout="centered")

# --- Password Generation Logic ---
def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_symbols):
    """Generates a cryptographically secure random password based on user criteria."""
    
    # Build the set of possible characters based on user choices
    character_set = ""
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_lowercase:
        character_set += string.ascii_lowercase
    if include_numbers:
        character_set += string.digits
    if include_symbols:
        character_set += string.punctuation
        
    # Handle the case where no character type is selected
    if not character_set:
        return None

    # Use secrets.choice for a secure random selection
    password = ''.join(secrets.choice(character_set) for _ in range(length))
    return password

# --- Streamlit User Interface ---
st.title("🔐 Secure Password Generator")
st.markdown("Create strong, random passwords to protect your accounts online.")

# --- User Input Widgets ---
length = st.slider(
    "Password Length", 
    min_value=8, 
    max_value=64, 
    value=16, 
    help="Choose how many characters your password should have."
)

st.subheader("Include Character Types:")
col1, col2 = st.columns(2)
with col1:
    include_uppercase = st.checkbox("Uppercase (A-Z)", value=True)
    include_numbers = st.checkbox("Numbers (0-9)", value=True)
with col2:
    include_lowercase = st.checkbox("Lowercase (a-z)", value=True)
    include_symbols = st.checkbox("Symbols (!@#$)", value=True)

# --- Password Generation and Display ---
if st.button("Generate Password", type="primary"):
    # Generate the password using the function
    password = generate_password(
        length, 
        include_uppercase, 
        include_lowercase, 
        include_numbers, 
        include_symbols
    )

    if password:
        st.success("Here is your new password:")
        # Use st.code for a clean, monospaced display
        st.code(password, language="text")
        # Add the copy to clipboard button
        st_copy_to_clipboard(password, "Copy to Clipboard")
    else:
        st.error("Error: Please select at least one character type to generate a password.")
