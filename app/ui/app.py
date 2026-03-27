import streamlit as st
from app.infra.aws.bedrock_client import BedrockClient


st.set_page_config(page_title="Prompt Refinement Lab", layout="wide")

st.title("🧪 Prompt Refinement Lab")
st.markdown("Veja como a qualidade do prompt altera drasticamente a resposta da IA.")

client = BedrockClient()

user_prompt = st.text_area(
    "Digite um prompt:", placeholder="Ex: explique redes neurais"
)

if st.button("Executar"):
    if not user_prompt.strip():
        st.warning("Digite um prompt válido.")
        st.stop()

    with st.spinner("Refinando prompt..."):
        refined_prompt = client.refine_prompt(user_prompt)

    with st.spinner("Executando modelo..."):
        original_response = client.invoke(user_prompt)
        refined_response = client.invoke(refined_prompt)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Prompt Original")
        st.code(user_prompt)

        st.subheader("Resposta")
        st.write(original_response)

    with col2:
        st.subheader("Prompt Refinado")
        st.code(refined_prompt)

        st.subheader("Resposta")
        st.write(refined_response)
