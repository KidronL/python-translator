from translate import Translator

t = Translator(to_lang="es")

#A function to open and read the file, then translate the contents and write them to a new file. The try block is used to handle errors
try:
    with open("test.txt", "r") as my_file:
        text = my_file.read()
        translation = t.translate(text)
        with open("translated.txt", "w") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print("File not found")
        