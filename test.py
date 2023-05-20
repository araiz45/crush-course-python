# def format_address(address_string):


#     house_number = ""
#     street_name = ""


#     # Separate the house number from the street name.
#     address_parts = address_string.split()
    
#     for address_part in address_parts:
#        # Complete the if-statement with a string method.  
#        if address_part.isnumeric():
#          house_number = address_part

#        else:
#          street_name += address_part + " "
#         #  print(address_part)
#     # Remove the extra space at the end of the last "street_name".
#     # street_name = street_name.split()
 
#     # Use a string method to return the required formatted string.
#     return "House number {} on the street named {}".format(house_number, street_name)


# print(format_address("123 Main Street"))
# # Should print: "House number 123 on a street named Main Street"


# print(format_address("1001 1st Ave"))
# # Should print: "House number 1001 on a street named 1st Ave"


# print(format_address("55 North Center Drive"))
# # Should print "House number 55 on a street named North Center Drive"



# genre = "transcendental"
# print(genre[:-8])
# print(genre[-7:9])


# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)


# speed_limits = {"street": 35, "highway": 65, "school": 15}
# print(speed_limits["highway"])






# def count_numbers(text):
#   # Initialize a new dictionary.
#   dictionary = {}
#   # Complete the for loop to iterate through each "text" character.
#   i = 0
#   for strings in text:
#     # Complete the if-statement using a string method to check if the
#     # character is a number.
#     if strings.isnumeric():
#       # Complete the if-statement using a logical operator to check if 
#       # the number is not already in the dictionary.
#       # print(strings, i)
#       if strings not in dictionary:
#            # Use a dictionary operation to add the number as a key
#            # and set the initial count value to zero.
#            dictionary[strings] = 0
           
#       # Use a dictionary operation to increment the number count value 
#       # for the existing key.
#       dictionary[strings] += 1
#   return dictionary

# print(count_numbers("1001000111101"))
# # Should be {'1': 7, '0': 6}

# print(count_numbers("Math is fun! 2+2=4"))
# # Should be {'2': 2, '4': 1}

# print(count_numbers("This is a sentence."))
# # Should be {}

# print(count_numbers("55 North Center Drive"))
# # Should be {'5': 2}


















# def combine_lists(list1, list2):


#   combined_list = [] # Initialize an empty list variable
#   list1.reverse() # Reverse the order of "list1"
#   list2.extend(list1) # Combine the two lists 
#   combined_list = list2
#   return combined_list  
  
# Jaimes_list = ["Alma", "Chika", "Benjamin", "Jocelyn", "Oakley"]
# Drews_list = ["Minna", "Carol", "Gunnar", "Malena"]


# print(combine_lists(Jaimes_list, Drews_list))
# # Should print ['Minna', 'Carol', 'Gunnar', 'Malena', 'Oakley', 'Jocelyn', 'Benjamin', 'Chika', 'Alma']
# animal = "Hippopotamus"
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])



# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)



teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
teacher_names.values()
print(teacher_names.values())