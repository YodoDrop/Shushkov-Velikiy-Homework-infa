from aho_corasick import AhoCorasick
from collections import defaultdict

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




def window(res):
    pair_list = []
    for i in res:
        for l in res[i]:
            pair_list.append((l, i))
    pair_list.sort()

    need_n = len(res)
    count = defaultdict(int)
    have = 0

    left = 0
    best = float('inf')
    best_range = None

    for right in range(len(pair_list)):
        word_r = pair_list[right][1]
        if count[word_r] == 0:
            have += 1
        count[word_r] += 1

        while have == need_n:
            pos_r = pair_list[right][0]
            pos_l = pair_list[left][0]

            if pos_r - pos_l < best:
                best = pos_r - pos_l
                best_range = (pos_l, pos_r)

            word_l = pair_list[left][1]
            count[word_l] -= 1

            if count[word_l] == 0:
                have -= 1
            left += 1

    return best_range








