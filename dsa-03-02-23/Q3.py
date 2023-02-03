'''
Write a program that encodes a word into Piglatin. To translate word into a Piglatin word,
convert the word into uppercase and then place the first vowel of the original word as the start of the new word
along with the remaining alphabets. The alphabets present before the vowel being shifted towards the end
followed by “AY”. Sample input (1) : London, Sample output (1) : ONDONLAY
Sample input (2) : Olympics, Sample output (2) : OLYMPICSAY'''

print("Enter a string to encode a word into Piglatin: ")
st = input()
st = st.upper()

vowel = ""
letters_before_vowel = ""
index_of_vowel = 0

for i in range(0, len(st)):
    if st[i] == 'A' or st[i] == 'E' or st[i] == 'I' or st[i] == 'O' or st[i] == 'U':
        vowel = st[i]
        index_of_vowel = i
        break
    letters_before_vowel += st[i]

piglatin = vowel
for j in range(index_of_vowel + 1, len(st)):
    piglatin += st[j]

piglatin += letters_before_vowel + "AY"

print(piglatin)
