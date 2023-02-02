body_parts = []

for times in range(3):
    part = input()
    body_parts.append(part)

meerkat = body_parts
meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)
