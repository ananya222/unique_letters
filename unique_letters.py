def find_unique_letters(sentence):
    sentence=sentence.lower()
    characters=[]
    for i in range(ord('a'),ord('z')):
        for n in range(0,len(sentence)):
            if(chr(i)==sentence[n]):
                characters.append(chr(i))
    return set(characters)

sentence='World is round'
characters=find_unique_letters(sentence)
print(characters)
