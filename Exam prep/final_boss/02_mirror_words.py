import re
text_string = input()
pattern = re.compile(r"([@#])(?P<word>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1")
groups = re.finditer(pattern, text_string)
mirror_results = []
matches_found = []
for g in groups:
    if g['word'] == g['word2'][::-1]:
        mirror_results.append(f"{g['word']} <=> {g['word2']}")
        matches_found.append(g)
    else:
        matches_found.append(g)
if len(mirror_results) > 0:
    print(f"{len(matches_found)} word pairs found!\nThe mirror words are:\n{', '.join(mirror_results)}")
elif len(matches_found) > 0 and len(mirror_results) == 0:
    print(f'{len(matches_found)} word pairs found!\nNo mirror words!')
else:
    print('No word pairs found!\nNo mirror words!')
