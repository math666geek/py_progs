text = ''
with open('text_for_prog.txt', 'r', encoding="utf-8") as file:
    for line in file:
        text = text + line
exceptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '_', '-', '=', '+', '?', '!', '&', '\n', ':', '\xa0', '«', '»', '–', ';']
text = text.lower()
for item in exceptions:
    text = text.replace(item, '')
s_2 = {}
for i in text:
    c = 0
    f = 0
    if i not in s_2:
        c = text.count(i)
        f = c / len(text)
        s_2[i] = f
    else:
        continue
print(s_2)
