import streamlit as st

def main():
    max_sequence_len = 50
    st.title('Previsão de Próximas Palavras')
    input_text = st.text_input('Digite uma sequencia de texto:')

if __name__ == "__main__":
    main()
