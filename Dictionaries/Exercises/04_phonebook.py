# add_contact = input().split('-')
# number_people_search = int(input())
phonebook = {}
add_contact = input().split('-')
while len(add_contact) > 1:
    person = add_contact[0]
    number = add_contact[1]
    if person not in phonebook.keys():
        phonebook[person] = number
    phonebook[person] = number
    add_contact = input().split('-')

for _ in range(int(add_contact[0])):
    searched_person = input()
    if searched_person in phonebook.keys():
        print(f"{searched_person} -> {phonebook[searched_person]}")
    else:
        print(f"Contact {searched_person} does not exist.")
