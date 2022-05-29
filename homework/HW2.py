import math
import random

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
        ost = n - math.floor(n)
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
    while number>1:
        new_number=str(int(number%2))+new_number
        number=int(number/2)
      
    
    print (str(number)+new_number)

    

ex4(121)
print()


 # Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.
   
def extra1(number):
    new_number = 0
    count = 1
    while(number>0):
        
        if round(number%10)==1: new_number+=count
        number=round(number/10)
        count*=2

    print(new_number)

extra1(1101)
print()


    


#2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:

# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру, 
# которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь 
# угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, скажите им, 
# сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена. Следите за количеством 
# догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.



def extra2():
    
    count = 0
    random4 = random.randint(1000, 9999)
    print(random4)
    12356
    merker = 1
    cows = 0
    bulls = 0
    while merker:
        print()
        print("Введите число:")
        print(f"У Вас {bulls} быков и {cows} коров")
        
        number = int(input())

        if (number>9999 or number<1000): print("Вы ввели неверное число")

        elif (number==random4):
            count+=1
            print("Вы угадали!")
            print(f"Попыток {count}")
            print(f"Всего быков {bulls}")
            print(f"Всего коров {cows}")
            merker = 0

        else:                                                                
            str_number = str(number)                                         
            str_random = str(random4)                                          
            str_cows_bulls = ""
            cows = 0
            bulls = 0
            for n in range(4):
                if (str_number[n] == str_random[n]):
                    cows+=1
                    str_cows_bulls+=" cow "
                elif (str_number[n] != str_random[n] and str_number[n] in str_random):
                    bulls+=1
                    str_cows_bulls+=" bull "
                else: str_cows_bulls+= " * "
            count+=1
            print(str_cows_bulls)
            


#extra2()

# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

def extra3():
    
    sum = 0
    n1 = 0
    n2 = 1
    number_Fib = 0

    while(number_Fib<=4000000): 
        
        number_Fib = n1+n2
        n1 = n2
        n2 = number_Fib
        print (number_Fib)
        if (round(number_Fib%2)==0):
            sum+=n2

    else: print (sum)

extra3()



#4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

print()
def extra4():

    new_number = 600851475143
    n = 2
    b = 1
    while (b):
        number = new_number
        biggest_n = 2
        a = 1
        while (a):
            if (number == biggest_n):
                a = 0 
                b = 0
            if (number%biggest_n!=0):
                biggest_n+=1
            else: 
                new_number = number/biggest_n
                a = 0
            
    print(biggest_n)       
        
extra4()
        

