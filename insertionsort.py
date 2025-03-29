def insertionsort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while my_list[j] > temp and j > -1:
            my_list[j+1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


my_list = [3, 2, 1, 6, 4, 5, 9, 7, 8]
print(insertionsort(my_list))
