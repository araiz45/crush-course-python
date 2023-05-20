# x = {}
# print(type(x))

#excelant

file_count = {'jpg': 12, 'png':13, 'cvv': 12}
print(file_count['jpg'])
print('jpg' in file_count)
print('html' in file_count)
file_count['html'] = 34
print(file_count)
file_count['jpg'] = 2
print(file_count)
del file_count['html']
print(file_count)


mr = {'rehan': 'baig', 'zain' : 'baig', 'rehan': 'zahid'}
print(mr)

file_count = {'jpg': 2, 'csv': 3, 'png': 34}
for extentions in file_count :
    print(extentions)

for ext, amount in file_count.items():
    print("There are {} files of {} extention".format(amount, ext))


print(file_count.keys())
print(file_count.values())


for values in file_count.values():
    print(values)



def count_letter(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1

    return result


print(count_letter("aaaa"))
# print(count_letter("Hello Brothers and sisters this me and i am going to jungle to make my life easy and content any one have question"))