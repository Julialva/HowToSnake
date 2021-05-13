import string

def personal_crypt(some_dict):
    for char in string.ascii_uppercase:
        crypto_key_char = (str(input("What letter should replace {}: ".format(char)))).lower()
        some_dict[char] = crypto_key_char
    return some_dict

def encrypt(some_string,some_dict,second=False):
    some_string = list(some_string)
    print(some_string)
    print(some_dict)
    new_string=[]
    for char in some_string:
        if (char.upper() in list(some_dict.keys()) and second==False):
            new_string.append(some_dict[char.upper()])
        elif (char.lower() in list(some_dict.keys()) and second==True):
            new_string.append(some_dict[char.lower()])
    new_string = ''.join(new_string)
    print(new_string)
    return new_string

def decrypt(new_string,some_dict):
    values = list(some_dict.values())
    keys = list(some_dict.keys())

    some_other_dict={}
    value_counter = 0
    for item in values:
        some_other_dict[str(values[value_counter])] = keys[value_counter]
        value_counter = value_counter + 1
    value_counter = 0
    coisa = encrypt(new_string,some_other_dict,second=True)
    return coisa

print('Hello friend, I am a encryptor, what should I encrypt?\n')
big_string = string.ascii_uppercase + string.digits + string.punctuation + string.whitespace
some_dict = {}
for char in big_string:
    some_dict[char] = char  
some_dict = personal_crypt(some_dict)
play_again = 'y'
while play_again == 'y': 
    some_string = str(input("Gimme a new string to encrypt my friend: "))
    new_string = encrypt(some_string,some_dict)
    dec = decrypt(new_string,some_dict)
    print('Your phrase was encrypted as: {0} , and then decrypted as {1}'.format(new_string,dec))
    play_again = (str(input('Would you like to continue encrypting?[y/n]: ' ))).lower()