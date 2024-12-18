# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # множество
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Примечания:
# Самостоятельно составлять (вручную) словарь не нужно (только изначально пустой).
result = {}  # создаем пустой словарь (dict)
# Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
# Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
students = list(students)  # преобразуем множество в список т.к. множество не упорядочено
students.sort()  # сортируем список по возрастанию (sort)
# добавляем ключи и значения в словарь используя sum и len
result[students[0]] = sum(grades[0])/len(grades[0])
result[students[1]] = sum(grades[1])/len(grades[1])
result[students[2]] = sum(grades[2])/len(grades[2])
result[students[3]] = sum(grades[3])/len(grades[3])
result[students[4]] = sum(grades[4])/len(grades[4])
print(result)
#Результат {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}