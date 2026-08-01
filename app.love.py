import streamlit as st
from google import genai

# -----------------------------
# Configure Gemini API
# --------------------------

GOOGLE_API_KEY= st.secrets["GEMINI_API_KEY"]
lient = genai.Client(api_key=GOOGLE_API_KEY)



st.set_page_config(page_title="❤️ AI Love Compatibility Checker", page_icon="❤️")

st.title("❤️ AI Love Compatibility Checker")
st.write("Enter your details below and let AI generate a fun compatibility report!")

# -----------------------------
# User Inputs
# -----------------------------
your_name = st.text_input("Your Name")

partner_name = st.text_input("Partner's Name")

your_age = st.number_input("Your Age", min_value=18, max_value=100, step=1)

partner_age = st.number_input("Partner's Age", min_value=18, max_value=100, step=1)

relationship = st.selectbox(
    "Relationship Status",
    [
        "Crush ❤️",
        "Dating 💕",
        "Best Friends 😊",
        "Married 💍",
        "Just Curious 😄"
    ]
)

your_hobby = st.text_input("Your Favourite Hobby")

partner_hobby = st.text_input("Partner's Favourite Hobby")

# -----------------------------
# Button
# -----------------------------
if st.button("❤️ Check Compatibility"):

    if your_name == "" or partner_name == "":
        st.warning("Please enter both names.")
    else:

        prompt = f"""
You are a fun relationship coach.

Create a playful compatibility report.

Important:
- This is only for entertainment.
- Do not claim scientific accuracy.
- Generate a compatibility score between 50 and 100.
- Keep it under 200 words.

Details:

Person 1:
Name: {your_name}
Age: {your_age}
Hobby: {your_hobby}

Person 2:
Name: {partner_name}
Age: {partner_age}
Hobby: {partner_hobby}

Relationship:
{relationship}

Output format:

❤️ Compatibility Score: XX%

💕 Strengths:
- ...

🌹 Challenges:
- ...

💡 Advice:
- ...

✨ Romantic Quote:
"""

        with st.spinner("Checking compatibility... ❤️"):

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )

        st.success("Compatibility Report Ready!")
        st.write(response.text)

st.markdown("---")
st.caption("⚠️ This app is for entertainment purposes only and does not measure real relationship compatibility.")
