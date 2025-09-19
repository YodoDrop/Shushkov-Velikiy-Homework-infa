vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
consonants = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ", "ь", "ъ"]

with open('text2n10', 'r', encoding="utf-8") as f:
    t = "".join(f.readlines()).strip()

a = []
i = 0
while i < len(t):
    if t[i] in vowels:
        if (i == 0 or t[i-1] in consonants or t[i-1] == ' ') and (i == len(t)-1 or t[i+1] not in vowels or t[i+1] == ' '):
            a.append([i + 1, t[i]])
    i += 1

k = list(t)
for p, v in reversed(a):
    k.insert(p, f"с{v}")

result = ''.join(k)
print(result)



