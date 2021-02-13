'''
a = 2
b = 0.5
print(a + b)

name = 'Yulia'
print(f'Привет {name}!')

v = int(input('Введите число от 1 до 10: '))
print(v + 10)

name = input('Введите ваше имя: ')
print(f'Привет, {name}! Как дела?')

a = float('1')
b = int(float('2.5'))
c = bool(1)
d = bool('')
e = bool(0)
print(a, b, c, d, e)

numbers = [3, 5, 7, 9, 10.5]
print(numbers)
numbers.append('Python')
print(len(numbers))
print(numbers[0])
print(numbers[-1])
print(numbers[1:5])
del numbers[-1]
'''

dic = {
    "city": "Moscow",
    "temperature": "20",
}
print(dic["city"])
tmp = int(dic["temperature"]) - 5
dic["temperature"] = str(tmp)
print(dic)
print(dic.get("country"))
print(dic.get("country", "Russia"))
dic["date"] = "27.05.2019"
print(dic)
print(len(dic))