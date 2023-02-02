def tribonacci_func(n):
    for _ in range(n):
        next_num = sum(our_list)
        print(next_num, end=' ')
        our_list.append(next_num)
        our_list.pop(0)


n = int(input())
our_list = [1, 0, 0]
tribonacci_func(n)