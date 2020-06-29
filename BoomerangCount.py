def count_boomers(lst):
    boomer_list = []
    for i in range(2, len(lst)):
        if lst[i - 2] == lst[i] and lst[i - 1] != lst[i]: boomer_list.append(lst[i - 2:i + 1])
    return boomer_list, len(boomer_list)
    
print(count_boomers([1, 5, 1, 5, 5, 6, 5, 3, -1, -2, 3, 2, 3]))
print(count_boomers([5, 5, 5, 1, 5, 7, 6, 5, 7, 3, 7]))
print(count_boomers([1, 1]))
print(count_boomers([1, 1, 1]))
print(count_boomers([1, 5, 1]))