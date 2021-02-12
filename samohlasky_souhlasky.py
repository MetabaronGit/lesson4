sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
result = dict(vowels = 0, consonants = 0)

for char in sentence:
    if char.lower() in "aeiouy":
        result["vowels"] += 1
    elif char.lower() in "bcdfghjklmnpqrstvwxz":
        result["consonants"] += 1

print("No. consonants: {0} | No. vowels: {1}".format(result["consonants"], result["vowels"]))


# vzorové řešení
# -------------------------------------------
vowels = 'aeiouy'
#2
counts = {'cons':0,'vows':0}
#3
for char in sentence:
    #4
    if not char.isalpha():
        continue
    #5
    if char.lower() in vowels:
        counts['vows'] += 1
    else:
        counts['cons'] += 1
#6
print('No. consonants: ' + str(counts['cons']) + ' | No. vowels: ' + str(counts['vows']))