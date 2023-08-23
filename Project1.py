# Multipele choice for Hash coding and Decoding
print("<<-------Make a Choices---->>")
print("1. Make massage to Hash code. ")
print("2. Make Hash Code to Decode.")
print("<<-------Make a Choices---->>")

# make a choice for code or decode
coding = int(input("Enter the choice (1-2) : "))
if coding == 1:
    code = True
elif coding == 2:
    code = False
else:
    print("Wrong number")

# Area of Hash Coding
if code:
    st = input("Enter Massage for Hash coding: ")
    words = st.split(" ")
    newWord = []
    for word in words:
         if len(word) >= 3:
             r1 = "kjsaahspmn"
             r2 = "jhdiuabavv"
             stnew = r1 + word[1:] + word[0] + r2
             newWord.append(stnew)
         else:
             newWord.append(word[::-1])
    print("\n<<---------Hash Code--------->>")
    print(" ".join(newWord))
    print("<<---------Hash Code--------->>")

# Area of Decoding
else:
    st = input("Enter Massage for Decoding: ")
    words = st.split(" ")
    newWord = []
    for word in words:
        if len(word) >= 3:
            stnew = word[10:-10]
            stnew = stnew[-1] + stnew[:-1]
            newWord.append(stnew)
        else:
            newWord.append(word[::-1])
    print("\n<<---------Decoded--------->>")
    print(" ".join(newWord))
    print("<<---------Decoded--------->>")
