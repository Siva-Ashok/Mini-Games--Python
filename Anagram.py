
#ANAGRAM CODE

word1=list(input().lower())
word2=list(input().lower())
print("word1 is:",word1)
print("word2 is:",word2)


if len(word1)!=len(word2):
            print("Given word is n\'t  anagram")
else:
    word1.sort()
    word2.sort()
    if word1==word2:
        print("Given word is anagram")
    else:
        print("Given word is n\'t  anagram")
