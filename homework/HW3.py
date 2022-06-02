
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

    else:
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
        else: 
            div+=1
      
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




# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 


def ex5():
    data = open("New_doc.txt", "r+")

    data.close

ex5()


# 6 Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение 
# в виде числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа, 
# которое должно быть закодировано отдельно, начиная с самой левой цифры. Таким образом, 1990 отображается 
# "MCMXC" (1000 = M, 900 = CM, 90 = XC), а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). Римская цифра для 1666, 
# "MDCLXVI", использует каждую букву в порядке убывания.
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21

rim_num = "MDCLXVI"
def extra_6(rim_num):
    rim_dict =  {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    arab_number = 0
    i = 0
    while(i<len(rim_num)-1):    # Я так понял внутри цикла Фор итератор и шаг в время выполнения цикла менять нельзя?
        
        if rim_dict[rim_num[i]]>=rim_dict[rim_num[i+1]]:
            arab_number+=rim_dict[rim_num[i]]
            print(arab_number)
            i+=1
           
        else:
             arab_number+=rim_dict[rim_num[i+1]]-rim_dict[rim_num[i]]
             i+=2
             print(arab_number)

    if (i==len(rim_num)-1): 
        arab_number+=rim_dict[rim_num[len(rim_num)-1]]

    print(arab_number)

extra_6(rim_num)






    





        


