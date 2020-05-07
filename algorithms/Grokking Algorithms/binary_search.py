# recursive implementation of binary search
def binary_search(list_1,number,left,right):
    if left > right:  #если первое число в массиве больше последнего то ошибка
        return False
    else:
        mid = (left+right)//2   #находим среднее число в массиве т.е. число, которое посередине
        if number == list_1[mid]: #если число которое мы ищем равно среднему числу то программа его вернет
            return mid
        if number > list_1[mid]: #если число которое мы ищем больше среднего то вызвать
                                 #функцию повторно,но left будет равно mid+1 т.е. число справа от mid
            return binary_search(list_1,number,mid + 1,right)
        else:
            return binary_search(list_1,number,left,mid - 1) #иначе вызываем функцию повторно, но в этом случае меняется
                                                             #right на mid-1 т.е. на число которое стоит слева от mid
list_1 = [4,7,8,14,29,64,85,210,297,412,556,978]
left = 0
number = 556
right = len(list_1) - 1
x = binary_search(list_1,number,left,right)
if x == False:
    print("Not found")
else:
    print("Number",number,"found!")



# iterative implementation of binary search
def binary_search(my_list,number):
    left = 0 #первый число в массиве
    right = len(my_list) - 1 #последнее число в массиве
    mid = (left + right) // 2 #среднее число в массиве
    while mid != number: #запускаем цикл и он будет работать до тех пор
                         #пока среднее число не будет равно искомому числу
        mid = (left + right) // 2
        if left > right: #если слева крайнее число будет больше числа крайнего справа то будет False
            return False
        if number == my_list[mid]:#если число которое мы ищем равно среднему числу то вернуть его
            return number
        if my_list[mid] > number:#если среднее число больше искомого то крайнее правое число
                                 #будет равняться mid-1 то есть соседнему слева числу mid
            right = mid - 1
        if my_list[mid] < number:#если среднее число меньше искомого то левое крайнее число
                                 #будет равняться mid+1 то есть соседнему справа числу mid
            left = mid + 1
my_list = [4, 7, 8, 14, 29, 64, 85, 210, 297, 412, 556, 978]
number = 210
x = binary_search(my_list, number)
if x == False:
    print("Not found")
else:
    print("Number", number , "found!")




