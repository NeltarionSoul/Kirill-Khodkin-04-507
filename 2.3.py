s = input()

palindrome = s[::-1] == s

mirror_dict = {
    'A': 'A',
    'M': 'M',
    '1': '1',
    '8': '8',
    'H': 'H',
    'I': 'I',
    'O': 'O',
    'T': 'T',
    'U': 'U',
    'V': 'V',
    'W': 'W',
    'X': 'X',
    'Y': 'Y',
    'E': '3',
    'J': 'L',
    'S': '2',
    'Z': '5',
    '3': 'E',
    '2': 'S',
    '5': 'Z'
}

mirror_s = ''
for character in s:
    if character in mirror_dict:
        mirror_s += mirror_dict[character]
    else:
        mirrored = False
        break
mirrored = mirror_s[::-1] == s

if mirrored and palindrome:
    print(s + 'is a mirrored palindrome.')
elif mirrored:
    print(s + 'is a mirrored string.')
elif palindrome:
    print(s + 'is a regular palindrome.')
else:
    print(s + 'is not a palindrome')