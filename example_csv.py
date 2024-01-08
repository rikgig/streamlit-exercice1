import streamlit as st
from example_csv_functions import binary_to_text, read_word_dictionary_from_csv, show_screen

def main():
    nb_entries = st.session_state.get('nb_entries', 0)
    initialized = st.session_state.get('initialized',False) 
    aList = st.session_state.get('aList')

    if not aList:
        aList = []
        st.session_state['aList'] = aList

    uploaded_file = st.file_uploader("Upload CSV file with word pairs (French, Spanish)", type="csv")

    if not initialized:
        st.session_state['aList'] = aList
        if uploaded_file:
            data = binary_to_text(uploaded_file)
            words_dictionary = read_word_dictionary_from_csv(data)
            aList = list(words_dictionary.keys()).copy()
            st.session_state['aList'] = aList
            st.session_state['initialized'] = True

    st.title("French to Spanish Quiz")
    questions_asked = st.session_state.get('questions_asked', 0)

    st.write("\nLet's start the quiz!\n")

    nb_entries = show_screen(st,nb_entries)
    st.session_state['nb_entries'] = nb_entries


if __name__ == "__main__":
    main()
