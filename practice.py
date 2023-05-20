# def ful_emails(people):
#     result = []
#     for email, name in people:
#         result.append("{} < {} >".format(name, email))    
#     return result

# print(ful_emails([("rehan@rehan.com", "rehan"), ("zain@zainbaig.com", "zain"), ("nabeera@nabeera.com", "nabeera")]))




# def skip_elements(elements):
# 	result = []
# 	for x,y in enumerate(elements):
# 		if x % 2 ==0:
# 		    result.append("{}".format(y))
	
# 	return result



# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']




# def multiples_function(number):
# 	multiples = []
# 	for x in range(1, 11):
# 		multiples.append(x * number)
# 	return multiples
# answers = input("Enter Table Number")
# print(multiples_function(int(answers)))


# multiples = [ x * 8 for x in range(1, 11)]
# print(multiples)
# 
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

