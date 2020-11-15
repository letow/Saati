# numpy для работы с матрицами
import numpy as np
cr_amount = int(input("Введите кол-во критериев: "))
# просто итератор
i = 1
#создание матрицы 
matr = np.eye(cr_amount)
# цикл для заполнения матрицы
for q in range(i, cr_amount+1):
  for p in range(i+1, cr_amount+1):
    matr[q-1][p-1] = round(float(input("Введите сравнение критерия {0}-{1}: ".format(q, p))), 3)
    matr[p-1][q-1] = round((matr[q-1][p-1])**(-1), 2)
  i += 1
# создание списка весовых коэффициентов
sum_matr = [round(sum(j),2) for j in matr]
# вывод списка
for k in sum_matr:
  print(round(k/sum(sum_matr), 2), end=' ')
