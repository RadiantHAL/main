import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()
random.shuffle(key)
encrypting=""
decrypting=""

#
while True:
    print("****************")
    print("Encrypting for 1 ")
    print("Decrypting for 2 ")
    print("****************")
    choice=int(input("Enter your choice 1/2 "))
    if choice==1:
        encoding = input("Enter you word to Encryption : ")
        for i in encoding:
            indexs=chars.index(i)
            encrypting+=key[indexs]
        print(encrypting)
    elif choice==2:
        decoding=input("Enter you word to Decryption :")
        for i in decoding:
            indexs=key.index(i)
            decrypting+=chars[indexs]
        print(decrypting)
    else:
        break
