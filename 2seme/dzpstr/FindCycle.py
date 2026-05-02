from aho_corasick import AhoCorasick

text = input()

aho = AhoCorasick()

string = input()
string_len = len(string)

count = 0

CycleString = []

for i in range(string_len):
    CycleString.append(str((string[string_len-1-i:] + string[:-1-i])))

aho.build_trie(CycleString)

count = 0

res = aho.find(text)
print(res)

for i in res.keys():
    count += len(res[i])

print(count)