text=''
with open('output_text_cipher.txt', 'r', encoding="utf-8") as file:
    for line in file:
        text = text + line
text = text.lower()
s_2={}
for i in text:
    c=0
    f=0
    if i not in s_2:
        c = text.count(i)
        f=c/len(text)
        s_2[i]=f
    else:
        continue
print(s_2)
