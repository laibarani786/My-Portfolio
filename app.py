import streamlit as st

st.set_page_config(page_title="Laiba Rani — Portfolio", layout="wide")

st.title("Laiba Rani")
st.subheader("Technical & AI Specialist — Python • Streamlit • Data • Research")

# About Section
st.header("About Me")
st.write("""
Hi, I’m **Laiba**! I work as a Technical & AI Specialist and I love technical research.  
I enjoy exploring new technologies and creating smart, simple, and user-friendly solutions.  
I have experience with AI-powered apps, data dashboards, and automation tools.
""")

# Skills
st.header("Skills")
skills = [
    "Python programming",
    "Artificial Intelligence (AI)",
    "Machine Learning & Deep Learning",
    "Streamlit app development",
    "Data analysis & visualization",
    "Technical research & innovation",
    "API integration",
    "Web deployment",
    "Automation & problem solving"
]
st.write(", ".join(skills))

# Projects
st.header("Projects")
projects = {
    "Salary Prediction App": "Streamlit app that predicts salary using a trained model. Includes CSV upload and interactive controls.",
    "Customer Churn Analysis": "Data analysis dashboard showing churn prediction, visualizations and feature importance.",
    "IMDb Sentiment BiRNN": "Sentiment analysis model with Streamlit frontend allowing users to test reviews in real time.",
    "Custom Data Dashboard": "Interactive dashboard for exploratory data analysis and visual storytelling."
}
for proj, desc in projects.items():
    st.subheader(proj)
    st.write(desc)

# Contact Section
st.header("Contact")
st.write("Email: [laibarani7663@gmail.com](mailto:laibarani7663@gmail.com)")
st.write("Location: Pakistan")
st.write("GitHub: [github.com/laibarani](https://github.com/laibarani)")
st.write("Fiverr: [fiverr.com/laibarani476](https://www.fiverr.com/laibarani476)")
st.write("WhatsApp: [+92 313 9095330](https://wa.me/923139095330)")

# Optional: Simple contact form (doesn't send email, just UI)
with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send Message")
    if submitted:
        st.success(f"Thanks {name}, your message has been received!")

