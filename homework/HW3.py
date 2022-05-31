
import math



# Найти НОК двух чисел


def ex1(number1, number2):
  
    if (number1==number2): 
        print ("Числа равны и сами являются НОК")
        return

    elif (number1>number2):
        NOD = number2
        temp1 = number1
        temp2 = number2

    elif (number1<number2):
        NOD = number1
        temp1 = number1
        temp2 = number2
    
    while(temp1%NOD!=0 or temp2%NOD!=0):
        NOD-=1
    NOK = number1/NOD*number2
    print(NOK)

    
ex1(4, 1)


# Вычислить число Пи c заданной точностью d
# Пример: при d = 0.001,  c= 3.141. 

def ex2(d):
    number_pi = math.pi
    new_number_pi = math.floor(number_pi/d)*d
    print(new_number_pi)

ex2(0.001)


# Составить список простых множителей натурального числа N


def ex3(N):
    div = 2
    spisok = [ ]
    while(N!=1):
        if (N%div==0):
            N/=div
            spisok.append(div)
        else: div+=1
      
    print(spisok)

ex3(58)



# Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

spisok_elementov_re = [1, 2, 3, 5, 1, 5, 3, 10]

def ex4(spisok_elementov):
    new_spisok_elementov = []
    for i in spisok_elementov:
        if i not in new_spisok_elementov:
            new_spisok_elementov.append(i)

    print(new_spisok_elementov)

ex4(spisok_elementov_re)
        


