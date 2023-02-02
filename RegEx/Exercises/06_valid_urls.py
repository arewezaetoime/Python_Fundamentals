import re
pattern = r'(w{3}\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)'
valid_urls = []
current_input = input()
while current_input:
    match = re.search(pattern, current_input)
    if match:
        valid_urls.append(match.group(0))
    current_input = input()

for url in valid_urls:
    print(url)