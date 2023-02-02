number_characters = int(input())
sum_of_the_characters = 0
for char in range(number_characters):
    command = input()
    sum_of_the_characters += ord(command)

print(f"The sum equals: {sum_of_the_characters}")
