inp = input()
k = list(inp)

def poly(s):
    for i in range(len(s)):
        if s[i]==s[len(s)-1-i]:
            a = 1
        else:
            a = 0
            break
    return a

def mir(b):
    mirror_dict = {
        'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O',
        'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
        'Y': 'Y', '1': '1', '8': '8',
        'E': '3', '3': 'E',
        'J': 'L', 'L': 'J',
        'S': '2', '2': 'S',
        'Z': '5', '5': 'Z'
    }
    for c in b:
        if c in mirror_dict:
            a = 1
        else:
            a = 0
            break
    return a

if mir(k)==1 and poly(k)==1:
    print(f"{inp} is a mirrored palindrome")
elif mir(k)==0 and poly(k)==1:
    print(f"{inp} is a regular palindrome.")
elif mir(k)==1 and poly(k)==0:
    print(f"{inp} is a mirrored string.")
elif mir(k)==0 and poly(k)==0:
    print(f"{inp} is not a palindrome.")










