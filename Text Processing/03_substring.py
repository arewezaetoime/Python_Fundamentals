string_to_remove = input()
string_to_edit = input()

while string_to_remove in string_to_edit:
    string_to_edit = string_to_edit.replace(string_to_remove, '')
print(string_to_edit)