from aho_corasick import AhoCorasick


def inp():
    text = input()
    string = input()
    templ = [""]
    for i in string:
        if i == "?":
            templ.append("")
            continue
        templ[-1] += i
    return text, templ

txt, tmpl = inp()

aho = AhoCorasick()
aho.build_trie(tmpl)

inp_dict = aho.find(txt)
nid = len(tmpl)

ans = []

offsets = []
cur = 0
for s in tmpl:
    offsets.append(cur)
    cur += len(s) + 1
L = cur - 1

need = sum(1 for s in tmpl if s)

if need == 0:
    ans = list(range(len(txt) - L + 1))
else:
    str_to_offsets = {}
    for i, s in enumerate(tmpl):
        if not s:
            continue
        str_to_offsets.setdefault(s, []).append(offsets[i])

    votes = {}
    for s, positions in inp_dict.items():
        if s not in str_to_offsets:
            continue
        for pos in positions:
            for off in str_to_offsets[s]:
                start = pos - off
                if 0 <= start <= len(txt) - L:
                    votes[start] = votes.get(start, 0) + 1

    ans = sorted(start for start, c in votes.items() if c == need)

print(*ans)