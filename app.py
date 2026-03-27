import streamlit as st
from app.infra.aws.bedrock_client import BedrockClient

# 1. Configuração da página
st.set_page_config(page_title="Prompt Refinement Lab", layout="wide")

st.title("🧪 Prompt Refinement Lab")
st.markdown("Veja como a qualidade do prompt altera drasticamente a resposta da IA.")


# 2. Instanciação do client
# (Idealmente, utilize st.cache_resource se a inicialização do client for custosa)
@st.cache_resource
def get_client():
    return BedrockClient()


client = get_client()

# 3. Formulário de Input (Evita reloads a cada tecla digitada)
with st.form("prompt_form"):
    user_prompt = st.text_area(
        "Digite um prompt base:", placeholder="Ex: explique redes neurais", height=100
    )
    submitted = st.form_submit_button("Refinar e Executar", type="primary")

# 4. Fluxo de Execução
if submitted:
    if not user_prompt.strip():
        st.warning("⚠️ Digite um prompt válido antes de executar.")
        st.stop()

    # Feedback de progresso unificado
    with st.status("Processando requisições no Bedrock...", expanded=True) as status:
        st.write("1. Refinando o prompt original...")
        refined_prompt = client.refine_prompt(user_prompt)

        st.write("2. Invocando modelo com prompt original...")
        original_response = client.invoke(user_prompt)

        st.write("3. Invocando modelo com prompt refinado...")
        refined_response = client.invoke(refined_prompt)

        status.update(
            label="Execução concluída com sucesso!", state="complete", expanded=False
        )

    st.divider()

    # 5. Apresentação (Layout Controlado)
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔴 Abordagem Original")
        # Prompt em destaque usando um box colorido
        st.info(f"**Prompt:**\n\n{user_prompt}")

        st.markdown("**Resposta:**")
        # Container com altura fixa: o segredo para não quebrar o layout
        with st.container(height=500, border=True):
            st.write(original_response)

    with col2:
        st.subheader("🟢 Abordagem Refinada")
        st.success(f"**Prompt Refinado:**\n\n{refined_prompt}")

        st.markdown("**Resposta:**")
        with st.container(height=500, border=True):
            st.write(refined_response)
