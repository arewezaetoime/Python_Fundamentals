factor = int(input())
factor_save = [factor]
count = int(input())
lst = []
for num in range(count):
    new_num = factor
    lst.append(int(new_num))
    factor += factor_save[0]
print(lst)