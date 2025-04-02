def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, i, swap_index)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quick_sort(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort(my_list, left, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, right)
    return my_list


my_list = [12, 11, 15, 10, 9, 1, 2, 3, 13, 14, 4, 5, 6, 7, 8]
print(quick_sort(my_list, 0, 14))

