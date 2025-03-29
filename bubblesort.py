def bubblesort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


my_list = [3, 2, 1, 6, 4, 5, 9, 7, 8]
print(bubblesort(my_list))
