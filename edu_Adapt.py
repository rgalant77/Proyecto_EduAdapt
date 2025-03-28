import streamlit as st
import google.generativeai as genai

# Configurar la API Key de Gemini
API_KEY = "TU_API_KEY_AQUI"
genai.configure(API_KEY_GEMINI=st.secrets["API_KEY_GEMINI"])

def generar_plan_estudio(edad, nivel, intereses):
    prompt = (f"Genera un plan de estudio personalizado para un estudiante de {edad} años, "
              f"en nivel {nivel}, con intereses en {intereses}. El plan debe ser detallado y estructurado.")
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text

# Interfaz de Streamlit
st.title("EduAdapt - Plan de Estudio Personalizado")
st.write("Usamos IA para adaptar el aprendizaje a cada estudiante")

# Entrada del usuario
edad = st.number_input("Edad del estudiante", min_value=3, max_value=100, value=10)
nivel = st.selectbox("Nivel académico", ["Preescolar", "Primaria", "Secundaria", "Universidad"])
intereses = st.text_area("Intereses del estudiante", "Matemáticas, Ciencia, Historia")

if st.button("Generar Plan de Estudio"):
    with st.spinner("Generando plan de estudio..."):
        plan_estudio = generar_plan_estudio(edad, nivel, intereses)
        st.subheader("Plan de Estudio Personalizado")
        st.write(plan_estudio)
