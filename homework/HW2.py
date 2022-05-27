# 1.	Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

list1 = [1,2,3,4,5,6,7]
def ex1(new_list): 
    sum = 0
    i = 0
    while i<=(len(new_list)-1):
        sum += new_list[i]
        i+=2
    print (sum)
ex1(list1)

#2.	Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

list2 = [10, 4, 11, 3, 5,6]
list3 = [10, 2, 1, 5, 10]

def ex2(old_list):
    new_list = []
    i=0
    len_list = len(old_list)-1
    while (i<=len_list/2):
        new_list.append(old_list[i]*old_list[len_list-i])
        i+=1
    print (new_list)


ex2(list2)
ex2(list3)

# 3.	В заданном списке вещественных чисел найдите разницу между 
# максимальным и минимальным значением дробной части элементов. 
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print()
list4 = [12.2, 41.2, 2.45, 4.03, 4.01, 45.9 ]
def ex3(old_list):
    max = 0
    min = old_list[0]
    ost = 0
    for n in old_list:
        ost = n - int(n)
        if ost<min:
            min = ost
        if ost>max:
            max = ost
    print(max)
    print(min)
    print(max-min)
ex3(list4)

# 4.	Написать программу преобразования десятичного числа в двоичное
print()


def ex4(number):
    new_number = ""
    rec_number = number
    def rec(rec_number):
        if rec_number/2<2:
            new_number.insert(0, rec_number/2)
            return new_number
        else: 
            new_number+=str(rec_number%2)
            return rec(rec_number/2)
    print (rec(rec_number))


ex4(6)


    


    









