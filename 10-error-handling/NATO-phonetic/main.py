import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {
    row["letter"]:row["code"] 
    for (index, row)
    in alphabet_data_frame.iterrows()
}

word = input("Enter a word: ").upper()

def generate_phonetic():
    try:
        output_list = [
            alphabet_dict[letter]
            for letter
            in word
        ]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_phonetic()
    else:
        print(output_list)
        
generate_phonetic()
