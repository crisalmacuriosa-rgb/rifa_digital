import streamlit as st

st.title("Rifa Digital 🎟️")

# Lista de números disponíveis na rifa (exemplo 1 a 50)
numeros_disponiveis = list(range(1, 51))

# Estado para armazenar números comprados e pagos
if "comprados" not in st.session_state:
    st.session_state.comprados = {}

st.write("### Escolha um número disponível:")

# Mostrar os números disponíveis (não comprados)
numeros_livres = [num for num in numeros_disponiveis if num not in st.session_state.comprados]

numero_escolhido = st.selectbox("Número:", numeros_livres)

if st.button("Comprar número"):
    # Registrar o número comprado com pagamento pendente
    st.session_state.comprados[numero_escolhido] = False
    st.success(f"Número {numero_escolhido} reservado para você. Por favor, finalize o pagamento.")

st.write("---")

# Mostrar os números comprados e status de pagamento
st.write("### Números comprados:")

if len(st.session_state.comprados) == 0:
    st.info("Nenhum número comprado ainda.")
else:
    for num, pago in st.session_state.comprados.items():
        status = "Pago ✅" if pago else "Pendente 💰"
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write(f"Número {num}")
        with col2:
            if not pago:
                if st.button(f"Registrar pagamento do número {num}"):
                    st.session_state.comprados[num] = True
                    st.success(f"Pagamento registrado para o número {num}!")

st.write("---")

# Link para compartilhar no WhatsApp
app_url = st.secrets.get("app_url", "https://seuapp.streamlit.app")  # Você pode trocar pelo link do seu app quando subir

mensagem = f"Oi! Estou participando da rifa digital. Confira o app aqui: {app_url}"

link_whatsapp = f"https://api.whatsapp.com/send?text={mensagem.replace(' ', '%20')}"

st.markdown(f"[Compartilhar no WhatsApp]({link_whatsapp})", unsafe_allow_html=True)
