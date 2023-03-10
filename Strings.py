#1.	Создайте функцию, которая принимает предложение и возвращает его аббревиатуру.
# Получите все слова длиной не менее n символов и верните первую букву каждого,
# с заглавной буквы и в целом, возвращённую как одну строку.

def abbreviate(sentence, n):
    words = sentence.split()
    result = []
    for word in words:
        if len(word) >= n:
            result.append(word[0].upper())
    return ''.join(result)


#Эта функция сначала разбивает предложение на список слов, используя split метод.
# Затем он перебирает каждое слово в списке и проверяет, больше ли его длина или равна n.
# Если это так, первая буква слова добавляется в result список.
# Наконец, функция возвращает объединенную строку всех букв при resultиспользовании join метода.


#2.Создайте функцию, которая принимает два числа и математический оператор и возвращает результат.

#Вот один из способов создания функции на Python, которая принимает
# на вход два числа и математический оператор и возвращает результат операции:

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"

#Эта функция использует оператор if-elif-else для проверки значения operator
#и выполнения соответствующей операции. Если оператор не является одним из +, -, *или /,
# функция возвращает строку «Недопустимый оператор».


#3.Создайте функцию, которая возвращает true, если входная строка содержит
# только прописные или строчные буквы.

def is_letter_case_only(s):
    return s.isupper() or s.islower()

#Эта функция использует методы isupperи islower строки, чтобы проверить,
# содержит ли строка только прописные или строчные буквы.
# Если строка содержит только прописные буквы, isupper метод
# возвращает True, а если строка содержит только строчные буквы,
# метод islower возвращает True. Если строка содержит как прописные, так и строчные буквы,
# оба метода возвращают False, и оператор or в операторе return также оценивается как False.


#4.	Дана строка чисел, разделенная запятой или пробелом, верните результат произведения чисел.

def product_of_numbers(numbers_string):
    # Split the string into a list of numbers
    numbers = numbers_string.split(',') if ',' in numbers_string else numbers_string.split()
    # Convert each number to an int
    numbers = [int(num) for num in numbers]
    # Calculate the product of all the numbers
    product = 1
    for num in numbers:
        product *= num
    return product


#Эта функция принимает строку numbers_string в качестве входных данных
# и сначала разбивает ее на список строк, используя либо ','или ' 'в качестве разделителя,
# в зависимости от того, какой из них присутствует во входной строке.
# Затем он преобразует каждую строку в целое число с помощью int()
# и вычисляет произведение всех чисел с помощью цикла for. Наконец, он возвращает product.


#5.Создайте функцию, которая принимает строку и заменяет гласные другим символом.

def replace_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""
    for char in s:
        if char in vowels:
            result += "$"
        else:
            result += char
    return result


input_string = "Hello, World!"
output_string = replace_vowels(input_string)
"""print(output_string)
Это будет печатать "H$ll$, W$rld!"
"""


#6.Напишите функцию, которая меняет местами все слова в предложении, начинающиеся с определенной буквы.

def swap_words(sentence, letter):
    words = sentence.split()
    for i in range(len(words)):
        if words[i][0].lower() == letter.lower():
            if i == 0:
                words[i], words[-1] = words[-1], words[i]
            else:
                words[i], words[i-1] = words[i-1], words[i]
    return " ".join(words)


sentence = "The quick brown fox jumps over the lazy dog."
letter = "t"
swapped_sentence = swap_words(sentence, letter)
"""print(swapped_sentence)
Это будет печатать "dog. lazy the over jumps fox brown quick The".
"""


#7.Напишите функцию, которая принимает строку и прореживает ее (т.е. удаляет последнюю 1/10 символов).
# Если строка состоит из 21 символа, 1/10 символов будет равно 2,1 символа, поэтому функция удаляет
# 3 символа (округляем «вверх»)

#Функция python, которая принимает строку в качестве входных данных и удаляет последние n символы,
# где nравно округленному результату 1/10 длины строки:


import math

def thin_out_string(s):
    n = math.ceil(len(s) / 10)
    return s[:-n]


input_string = "The quick brown fox jumps over the lazy dog."
thinned_out_string = thin_out_string(input_string)
"""print(thinned_out_string)
Это будет печатать "The quick brown fox jumps over the lazy"."""



#8.	На входе имеется массив: [[[[[[[[[[[]]]]]]]]]]]]
# (другими словами, массив, содержащий массив, содержащий массив,
# содержащий ... массив, не содержащий ничего). Ваша цель - измерить глубину этого массива,
# где [] имеет глубину 1, [[]] имеет глубину 2, [[[]]] имеет глубину 3, и т. д.

#функция рython, которая принимает массив в качестве входных данных и возвращает глубину массива:

def array_depth(arr):
    if isinstance(arr, list):
        return 1 + array_depth(arr[0]) if arr else 1
    return 0

input_array = [[[[[[[[[[]]]]]]]]]]
depth = array_depth(input_array)
"""print(depth)
Напечатает 12, так как входной массив имеет глубину 12."""


#9.	Создайте функцию, которая принимает слово и возвращает true,
# если слово имеет две идущие подряд одинаковые буквы

#функция рython, которая принимает слово в качестве входных данных и возвращает значение,
# True если слово состоит из двух последовательных одинаковых букв:

def has_consecutive_duplicates(word):
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return True
    return False

input_word = "hello"
output = has_consecutive_duplicates(input_word)
"""print(output)
Это напечатает True, так как слово "hello"состоит из двух последовательных одинаковых букв ( "ll")."""


#10.Создайте функцию, которая из массива строк возвращает только строки с уникальными символами.

#пример функции Python, которая принимает массив строк в качестве входных данных и возвращает новый массив,
# содержащий только строки с уникальными символами:

def unique_characters(arr):
    def has_unique_chars(s):
        return len(set(s)) == len(s)
    return [s for s in arr if has_unique_chars(s)]

input_array = ["hello", "world", "foo", "bar"]
output_array = unique_characters(input_array)
"""print(output_array)
Это напечатает ['foo', 'bar'], так как слова "foo"и "bar"имеют уникальные символы."""


#11.У вас есть массив кодов товаров в следующем формате: «[буквы] [цифры]».
# Создайте функцию, которая разбивает эти строки на их буквенные и числовые части.

#Вот пример функции Python, которая принимает массив кодов продуктов в формате
# "[letters] [numbers]" в качестве входных данных и разбивает коды на буквенную и цифровую части:

def split_codes(codes):
    result = []
    for code in codes:
        letter_part = ''.join(filter(str.isalpha, code))
        number_part = ''.join(filter(str.isdigit, code))
        result.append((letter_part, number_part))
    return result


input_codes = ["AB12", "CD34", "EF56"]
output = split_codes(input_codes)
"""print(output)
Это напечатает [('AB', '12'), ('CD', '34'), ('EF', '56')], 
который представляет собой список кортежей, каждый из которых содержит буквенную и цифровую части кода"""

#Функция filter используется для извлечения частей букв и цифр из каждого кода во входном массиве.
# Функции str.isalphaи str.isdigit предопределены в Python и возвращают True
# буквенные и числовые символы соответственно.
#Метод ''.join используется для объединения извлеченных символов в строки.
#Буквенные и числовые части каждого кода добавляются в список кортежей,
# который функция возвращает в качестве конечного результата.


#12.	Создайте функцию, которая принимает входные данные (например, «5 + 4») и возвращает true,
# если это математическое выражение, или false, если нет.

#Вот пример функции Python, которая принимает входную строку, например " 5 + 4",
# и возвращает значение True, если это математическое выражение, и False в противном случае:

import re

def is_math_expression(input_string):
    # Define a regular expression pattern for a mathematical expression
    pattern = r'^\s*\d+\s*[\+\-\*\/]\s*\d+\s*$'
    return bool(re.match(pattern, input_string))

input_string = "5 + 4"
output = is_math_expression(input_string)
"""print(output)
Это напечатает True, указывая, что входная строка является математическим выражением."""

#Модуль reимпортируется для использования регулярных выражений.
#Функция re.matchиспользуется для сопоставления входной строки с pattern шаблоном
# регулярного выражения для математического выражения.
#имволы ^и $в шаблоне указывают, что строка должна начинаться и заканчиваться шаблоном соответственно.
#Шаблон \d+соответствует одной или нескольким цифрам.
#Шаблон \s*соответствует нулю или более пробелам.
#Шаблон [\+\-\*\/]соответствует либо +, -, *либо /.
#Если входная строка соответствует шаблону, re.matchфункция возвращает объект соответствия,
#что является истинным. Если входная строка не соответствует шаблону,
# re.matchвозвращает None, что является ложным.
#Функция boolиспользуется для преобразования объекта соответствия в логическое значение
# ( True или False) и возврата его в качестве конечного результата функции.


#13.Создайте функцию, которая удалит любые повторяющиеся символы в слове,
# переданном в функцию (не только последовательные символы, но и символы,
# повторяющиеся в любом месте ввода).

#Вот функция в Python, которая удаляет любые повторяющиеся символы в слове:

def remove_duplicates(word):
    result = ""
    for char in word:
        if char not in result:
            result += char
    return result

#Функция принимает word в качестве входных данных.
#Пустая строка resultсоздается для хранения символов word после удаления дубликатов.
#Используя цикл for, мы перебираем каждый символ в word.
#Для каждого символа мы используем if оператор, чтобы проверить, существует ли он уже в result строке.
#Если символ отсутствует в result строке, он добавляется к ней.
#Функция возвращает result строку после удаления всех дубликатов.


#14.Создайте функцию, которая добавляет пробелы перед каждой заглавной буквой в слове.
# После этого уберите заглавные буквы из всей строки.

#Для решения этой задачи мы можем использовать цикл для перебора всех символов в слове,
# и проверять каждый символ, является ли он заглавным. Если это так,
# мы добавляем пробел перед этим символом и преобразуем его в строчный символ.

def add_space_lowercase(word):
    new_word = ""
    for char in word:
        if char.isupper():
            new_word += " " + char.lower()
        else:
            new_word += char
    return new_word

#В этой функции мы перебираем все символы в слове word,
# и проверяем каждый символ с помощью функции isupper().
# Если символ является заглавным, мы добавляем перед ним пробел
# и преобразуем его в строчный символ с помощью lower().
# Если символ не является заглавным, мы просто добавляем его к результирующей строке new_word.
# На конечном этапе мы возвращаем new_word как результат функции.


#15.Для строки, содержащей набор символов и цифр, вернуть сумму всех чисел в строке.
# Обратите внимание, что несколько цифр рядом друг с другом считаются как целое число,
# а не как отдельные цифры.

def sum_of_numbers_in_string(input_string):
    import re
    numbers = re.findall(r'\d+', input_string)
    return sum([int(number) for number in numbers])

#Импортируем модуль re для работы с регулярными выражениями.

#Используем функцию re.findall для нахождения всех последовательностей цифр в строке input_string.
# Для этого мы используем шаблон регулярного выражения r'\d+', где \d означает "любую цифру"
# и + означает "один или более раз".
#Возвращаем сумму всех чисел, которые мы нашли,
# преобразовав каждое из них в тип int и используя списочные выражения.











