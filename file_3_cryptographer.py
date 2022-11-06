a = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
b = ['г', 'и', 'к', 'т', 'ч', 'ь', 'б', 'ж', 'л', 'р', 'х', 'ъ', 'я', 'д', 'й', 'о', 'у', 'ш', 'э', 'в', 'з', 'м', 'с',
     'ц', 'ы', 'а', 'е', 'к', 'п', 'ф', 'щ', 'ю', ' ']
text = ''
stroka = ''
print('1-зашифровать собщение')
print('2-расшифровать собщение')
mode = int(input('Введите режим работы: '))
with open('tolstoy.txt', 'r', encoding="utf-8") as file:
    for line in file:
        text = text + line
text=text.lower()
myfile_2 = open('output_text_cipher.txt', 'w', encoding="utf-8")
if mode == 1:
    for item in text:
        if item in a:
            index_of_item = a.index(item)
            stroka = stroka + b[index_of_item]
        else:
            stroka=stroka+item
    myfile_2.write(stroka)
    myfile_2.close()

if mode == 2:
    for item in text:
        index_of_item = b.index(item)
        stroka = stroka + b[index_of_item]
    myfile_2.write(stroka)
    myfile_2.close()

if mode > 2 or mode < 1:
    myfile_2.write('неизвестный режим работы')
    myfile_2.close()
