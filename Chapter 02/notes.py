language = "python"

first_letter = language[0]
last_letter = language[5]
print(first_letter, last_letter)  # p, n

print("string length:", len(language))

text = "Q&A"
print(ord(text[0]))  # char -> ascii
print(chr(81))  # ascii -> char

new_text = "Python Language"
first_word = new_text[0:6]  # Python
second_word = new_text[7:]  # Language
third_word = new_text[7:14]  # Languag

template = "country: {}, city: {}, population: {}"
print(template.format("BUL", "Sofia", 75))

first_name = "Jane"
last_name = "Smith"
print(f"Hello, I'm {first_name} {last_name}!")

# input винаги извлича стринг
a = input("a=")  # 5
b = input("b=")  # 6
print("sum of a & b:", a + b)  # 56

x = int(input("x="))  # 5
y = int(input("y="))  # 6
print("sum of a & b:", x + y)  # 11

# from test
"""
x = 10
y = "20"
print(x + y) # TypeError: unsupported operand
"""
