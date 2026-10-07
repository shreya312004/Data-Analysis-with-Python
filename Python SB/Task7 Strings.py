"Module:- Strings"
"Description :- This program demonstrates the basic string operation"

Name = (input('enter the name: '))
reverse_name = Name[ :: -1]
print('\n----reverse string----')
print(f'Original String : {Name}')
print(f'revered string : {reverse_name}')

"Description: Count of vowel and consonants"

String = (input('enter the Name '))

vowels = "aeiouAEIOU"
vowels_counts = 0
consonants_counts = 0

for letter in String:

    if letter in vowels: 
        vowel_counts += 1
    else:
        consonants_counts += 1
print('\n----Vowels and Consonants count----')
print(f"string           : {String}")
print(f'total vowels     : {vowel_counts}')
print(f'total consonants : {consonants_counts}')

"Description :- this program demonstrates the split and joint operation"

Sentence = (input('enter a sentence : '))

words = Sentence.split()
print('\n----splitted sentence----')
print(f'splitted Sentence : {words}')

#Joined = Semtence.joint()
Joined = " ".join(words)
print('\n-----Joined Sentence-----')
print(f'joined sentence : {Joined}')

"Description:- Basic String Operaions"

text = (input("enter the text :"))

print('\n--------Basic String Operation--------')
print(f'Upper Case            : {text.upper()} ')
print(f'Lower Case            : {text.lower()}')
print(f'Tittle Case           : {text.title()}')
print(f'Capitalize            : {text.capitalize()}')
print(f'Length                : {len(text)}')
print(f"starts with 'p '      : {text.startswith('p')}")
print(f"Ends with 'n '         : {text.endswith('n')}")
