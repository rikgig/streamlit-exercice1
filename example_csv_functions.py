import csv
from io import StringIO


def binary_to_text(binary_file):

    # bytes_data = binary_file.read()

    # try:        
    #     encoding = 'utf-8'
    #     s=str(bytes_data,encoding)
    # except:
    #     encoding = 'utf-16-le' 
    #     s=str(bytes_data,encoding)

    # data = io.StringIO(s)        
    # return data
    data = StringIO(binary_file.getvalue().decode("utf-8"))
    return data

def read_word_dictionary_from_csv(file):
    word_dict = {}
    with file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 0:
                pronoun, spanish, french, details, five, six, seven = row
                word_dict[spanish.strip()] = french.strip()
    return word_dict

def show_screen(st, nb_entries):
    aList = st.session_state.get('aList', None)
    
    if nb_entries < 5 and len(aList) > 0:
        french_word = aList.pop()
        # french_word = aList[nb_entries]
        st.session_state['aList'] = aList

        user_input = st.text_input(f"Translate '{french_word}':")
        print("User input return: " +user_input)
        if user_input:  
            print("User input read: " +user_input)
            st.write(user_input)
            nb_entries += 1
            print(f"List size: {len(aList)}" )
        else:
            print("fill the text!")    
    else:
        st.write("DONE!")
    return nb_entries

