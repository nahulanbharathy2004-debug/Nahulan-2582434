import streamlit as st
from src.llm_engine import generate_explanation
from src.visual_engine import generate_diagram

# Setup the page layout
st.set_page_config(page_title="Smart Doubt Resolver", page_icon="🧠", layout="wide")

st.title("🧠 Smart Doubt Resolver")
st.markdown("Enter your academic doubt below to get a detailed explanation and a generated visual diagram.")

# Create the input box
user_query = st.text_input("What would you like to learn about today?")

# Create the submit button
if st.button("Resolve"):
    if user_query:
        # Create two columns side-by-side for the output
        col1, col2 = st.columns(2)
        
        with col1:
            st.header("📝 Explanation")
            with st.spinner("Generating text explanation via Ollama..."):
                explanation = generate_explanation(user_query)
                st.write(explanation)
                
        with col2:
            st.header("🎨 Diagram")
            with st.spinner("Generating visual via Stable Diffusion..."):
                image = generate_diagram(user_query)
                if image:
                    st.image(image, caption=f"Visual representation of: {user_query}")
                else:
                    st.error("Failed to generate diagram.")
    else:
        st.warning("Please enter a question first!")
