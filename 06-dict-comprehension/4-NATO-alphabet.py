import pandas

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet_data_frame)

# for (index, row) in alphabet_data_frame.iterrows():
#     print(row["letter"])
#     print(row["code"])

#TODO Create a dict of NATO phonetic alphabet

alphabet_dict = {
    row["letter"]:row["code"] 
    for (index, row)
    in alphabet_data_frame.iterrows()
}

#TODO Create a list of NATO phonetic alphabet based on Input
word = input("Enter a word: ")
word_upper = [
    letter.upper()
    for letter
    in word
]
# print(word_upper)

output_list = [
    alphabet_dict[letter]
    for letter
    in word_upper
]
print(output_list)



# word_dict = {
#     letter:code 
#     for (letter, code) 
#     in alphabet_dict.items() 
#     if letter in word_upper
# }

# print(word_dict)