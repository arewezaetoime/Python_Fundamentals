import re
first_pattern = r'[star]'
second_pattern = r'@([a-zA-Z]+).?[^\@\-\!\:\>]*?:(\d+)[^\@\-\!\:\>]*?!([AD])![^\@\-\!\:\>]*?->(\d+)'

number_of_ciphers = int(input())
ciphers = []
attacked_planets = []
destroyed_planets = []
if number_of_ciphers in range(0, 100):
    for _ in range(number_of_ciphers):
        current_cipher = input()
        count = re.findall(first_pattern, current_cipher, re.IGNORECASE)
        decrypted_cipher = ''
        for letter in current_cipher:
            current_letter = ord(letter) - len(count)
            decrypted_cipher += chr(current_letter)
        ciphers.append(decrypted_cipher)
if ciphers:
    for planet in ciphers:
        planet_verification = re.search(second_pattern, planet)
        if planet_verification:
            if planet_verification.group(3) == 'A':
                attacked_planets.append(planet_verification.group(1))
            if planet_verification.group(3) == 'D':
                destroyed_planets.append(planet_verification.group(1))
print(f"Attacked planets: {len(attacked_planets)}")
for _ in sorted(attacked_planets):
    print(f"-> {_}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for _ in sorted(destroyed_planets):
    print(f"-> {_}")