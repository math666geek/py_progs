a={ 'fine':['прекрасный','отличный'],
    'fire':['пламя','пожар']}
word=input('')
for key in a.keys():
    for item in a[key]:
        if item==word:
            print(key)
    
