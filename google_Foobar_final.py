import string

def split(word): #Splitting words into characters
    return [char for char in word]

command = raw_input("Enter the command: ")

all_characters = string.ascii_letters + string.punctuation + string.whitespace
reversed_all_characters = list(reversed(all_characters))

lowercases = split(string.ascii_lowercase)
reversed_lowercases = list(reversed(lowercases))

original_command = "This is the original command: "

for char in command:
    if char in string.ascii_lowercase:
        num = reversed_lowercases.index(char)
        original_command += lowercases[num]
    else:
        original_command += char

print (original_command)






