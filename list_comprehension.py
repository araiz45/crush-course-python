# List comprehesion

# multiples =  []
# for x in range(1,11):
#     multiples.append(x*7)

# print(multiples) # This is difficult way
# output : [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]


# The easy way

# multiples = [x * 7 for x in range(1, 11)]
# print(multiples)

#output : [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# This will print same output

# List Comprehentions
# let us creates a new list based on sequences or ranges


# Example no 2 
# languages = ['ruby', 'python', 'java', 'javaScript', 'swift', 'c++', 'c', 'typescript', 'mojo', 'rust', 'css', 'kotlin', 'ruby', 'julia']
# lenghts = [len(language) for language in languages]
# print(lenghts)
# this program will print length of the string which named in javascript
#output : [4, 6, 4, 10, 5, 3, 1, 10, 4, 4, 3, 6, 4, 5]

# using if statement in range 
# z = [x for x in range(1, 101) if x % 2 == 0]
# print(z)
# output : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 
#86, 88, 90, 92, 94, 96, 98, 100]
# Practice in the course

# def odd_numbers(n):
# 	return [x for x in range(1, n+1) if x % 2 != 0]

# print(odd_numbers(5))  # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
# print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
# print(odd_numbers(1))  # Should print [1]
# print(odd_numbers(-1)) # Should print []