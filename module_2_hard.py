import random as r


def get_password(num):
    password = ""
    temp = []
    for i in range(1, num):
        for j in range(1, num):
            if i == j:  # исключение совпадающих чисел
                continue
            if [j, i] in temp:  # исключение повторяющихся пар
                continue
            if num % (i + j) == 0:
                password += str(i) + str(j)
                temp.append([i, j])
    return password


number = r.randint(3, 20)
# for number in range(3, 21):  # вариант с циклом для всех чисел из пула (сняв комментарий, не забудьте проставить отступы строкам внизу)
print(number)
code = get_password(number)
print(code)
