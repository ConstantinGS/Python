
# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 
print()     
def ex5():
    data = open("new_text_file_1.txt", "r" )
    for line in data:
        print(line)
    data.close() 

ex5()


