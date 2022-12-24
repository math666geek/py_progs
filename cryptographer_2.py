a = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц',
     'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
b = [0.062, 0.014, 0.038, 0.013, 0.025, 0.072, 0.007, 0.016, 0.062, 0.010, 0.028, 0.035, 0.026, 0.053, 0.090, 0.023,
     0.040, 0.045, 0.053, 0.021, 0.002, 0.009, 0.004, 0.012, 0.006, 0.003, 0.014, 0.016, 0.014, 0.002, 0.006, 0.018,
     0.175]
text = ''
with open('text_for_prog.txt', 'r', encoding="utf-8") as file:
    for line in file:
        text = text + line
exceptions = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.', '_', '-', '=', '+', '?', '!', '&', '\n', ':',
              '\xa0', '«', '»', '–', ';']
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
        s_2[i] = round(f, 3)
    else:
        continue
print(s_2)


def get_nearest_value(f, b):
    left = 0
    right = len(b)
    while (right - left > 1):
        i = left + (right - left) // 2
        if f < b[i]:
            right = i
        else:
            left = i
    a = min([(abs(f - b[j]), b[j], j) for j in (i - 1, i, i + 1)])
    return a[1:3]


print(get_nearest_value(f, b))
