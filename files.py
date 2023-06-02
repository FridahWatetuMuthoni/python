try:
    with open("text.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print("file not found")
    print(e)
finally:
    print(file.closed)


text = "Yoooooooooooooooooooh man \nThis is some text\nHave a good one\n"
try:
    with open("test.txt", "w") as file:
        file.write(text)
except FileNotFoundError as e:
    print(e)

text2 = "Just using the append method to append some text without overwritting the file\n"
try:
    with open("test.txt", "a") as file:
        file.write(text2)
except FileNotFoundError as e:
    print(e)