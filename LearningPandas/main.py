import pandas
# dict comprehension

dataframe= pandas.read_csv("nato_phonetic_alphabet.csv")
#print( dataframe)
phonetic_dict= { value.letter:value.code  for (key, value ) in dataframe.iterrows()}
#print (phonetic_dict)
word = input("Enter a word:").upper()
try:
    letters =[phonetic_dict[char] for char in word]
except:
    print("Sorry, only letters in the alphabets please.")
else:
    print(letters)