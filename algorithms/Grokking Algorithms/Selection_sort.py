def selection_sort(my_list):
    for i in range(len(my_list)):#диапазон нашего цикла весь весь массив
        min = i #число i будет считаться минимумом т. е. нулевой индекс далее будет меняться
        for j in range(i , len(my_list)): #j индексы чисел с которыми мы сравниваем i-ый индекс
            if my_list[j] < my_list[min]:
                min = j#при выполнении условия минимумом будет j

        temp_ver = my_list[i]#временная переменная которая будет хранить число которое сравнивали со всеми остальными
        my_list[i] = my_list[min]
                                #далее значения пременных будут меняться
        my_list[min] = temp_ver


x = [45, 2, 32, 41, 56, 8, 7, 123, 654]
selection_sort(x)
print(x)

