s = input("Enter a string: ")
alphabet = {}
count = 0

def expand_dict(ch):
    if alphabet.get(ch) is None:
        alphabet[ch] = 1
    else:
        alphabet[ch] += 1

for i in s:
    if i.isalpha():
        count += 1
        expand_dict(i.lower())

maxCh = ''
maxCount = 0
for i in alphabet:
    if alphabet[i] > maxCount:
        maxCh = i
        maxCount = alphabet[i]
    elif alphabet[i] == maxCount:
        maxCh = min(i, maxCh)


print("The number of alphabetic letters in \""+ s +"\" is \"{}\".".format(count))
print("The most frequent alphabetic letter in \""+ s +"\" is \""+ maxCh +"\".")
