#Дано целое число. Если оно является положительным, то прибавить к нему 20,
# в противном случае вычесть из него 5.

a = input('Введи целое число') # Ввод данных
while type(а) != int: # обработка исключений
 try:
  а = int(а)
 except ValueError:
  print("Неправильно ввели!")
  а = input('Введите целое число')
if a > 0:
  a = a + 20
else:
  a = a - 5
print(a)