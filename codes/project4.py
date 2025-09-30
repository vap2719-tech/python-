alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N',
          'O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encription(plain_text,shift_key):  #hello  h=7
    cipher_text=" "
    for char in plain_text:
       if char in alphabet:
          position=alphabet.index(char)
          new_position=(position+int(shift_key))%26
          cipher_text +=alphabet[new_position]
       else:
          cipher_text += char
    print(f"here is the text after encription:{cipher_text}")
   
def decription(cipher_text,shift_key):  #hello  h=7
    plain_text=" "
    for char in cipher_text:
       if char in alphabet:
          position=alphabet.index(char)
          new_position=(position-int(shift_key))%26
          plain_text +=alphabet[new_position]
       else:
          plain_text += char
    print(f"here is the text after decription:{plain_text}")
   

wanna_end=False
while not wanna_end:
    what_to_do=input("type 'encript' for encription,type'decript' for decription:\n")
    text=input("enter your text:\n ").lower()
    shift=input("enter shift kay:\n")
    if what_to_do=="encript":
       encription(plain_text=text,shift_key=shift)
    elif what_to_do=="decript":
       decription(cipher_text=text,shift_key=shift)
       play_again=input("type 'yes' to continue,type 'no' exit.\n")
       if play_again=='no':
          wanna_end=True
    print("have a nice day! bye..")