def loading_bar(integer):
    if integer == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    return f"{integer}% [{'%' * (integer // 10)}{'.' * (10 - (integer // 10))}]\nStill loading..."


single_integer = int(input())
print(loading_bar(single_integer))