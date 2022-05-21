#Main program
WORDS=[]
print("To stop the program type: stop")
word=input("Word: ")
WORDS.append(word)
print("> "+str(word))
while word != "stop":
    word=input("Word: ")
    WORDS.append(word)
    print("> "+str(word))
print("All the words you entered: "+str(WORDS[:]))
