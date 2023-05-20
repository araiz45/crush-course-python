# # print("Today is a good day I am good")
# fruits = ["mango", "banana", "stewberry", "graps"]
# print(fruits)
# print(type(fruits), len(fruits))


# print("peach" in fruits)
# if "mango" in fruits:
#     print("mongo is present")
# print(fruits[4])
# print("mango" in fruits)
# print(fruits[1:3])

# sentence = "hello world I am good and from karachi"
# print(list(sentence))

# List methods in python


# color = ['red', 'green', 'blue', 'white']
# color.append('indigo')
# print(color)

# fruits = ['apple', 'mango', 'banana','orange','milon']
# fruits.insert(0, 'mango')
# fruits.insert(45, "me")
# print(fruits)
# fruits.remove("mango")
# print(fruits)
# # fruits.remove("hello")
# print(fruits)
# # fruits.pop('mango')
# fruits.pop(1)   
# print(fruits)
# fruits[1] = "Kiwi"
# print(fruits)

# tuples in python 
# fruits = ('mango','banana','orange','strewberry')
# def convert_seconds(seconds):
#     hours = seconds// 3600
#     minutes = (seconds - hours * 3600)//60
#     remaining_seconds = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_seconds

# result = convert_seconds(5000)
# print(type(result))
# print(result)
# hours , minutes, seconds = result
# print(hours, minutes, seconds)
# hours, minutes, seconds = convert_seconds(1000)
# print(hours, minutes, seconds)
# animals = ['zebra', 'eagle','rino','dog', 'cat']
# char = 0
# for animal in animals:
#     char += len(animals)
#     print(char)


# print('total characters : {}, Average length: {}'.format(char, char/len(animals)))
# # print(char/len(animals))



# winners = ['asley', 'dylen', 'rease']
# for index, person in enumerate(winners):
#     print("{} - {}".format(index+1, person))

def ful_emails(people):
    result = []
    for email, name in people:
        result.append("{} < {} >".format(name, email))    
    return result

# print(ful_emails([("rehan@rehan.com", "rehan"), ("zain@zainbaig.com", "zain"), ("nabeera@nabeera.com", "nabeera")]))


# animals = ['zebra', 'snake', 'unicorn', 'griffin', 'dragon']
# for img, real in animals:
#     print(img, real)