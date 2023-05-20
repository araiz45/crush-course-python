# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate newfilenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.
# newfilenames = []
# for x in filenames :
#     # print(x[-3:])
#     if x[-3:] == "hpp":
#         new_string = x.replace("hpp", "h")
#         # print(new_string)
#         newfilenames.append(new_string)
#         # continue
#     else:
#         newfilenames.append(x)

        

# print(newfilenames) 
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"



def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split(" ")
  for word in words:
    # Create the pig latin word and add it to the list

    if word[0] == 'e' or word[0] == 'o' or word[0] == 'u':
      say += word + "ay "
    else:
      say += word[1:] + word[0]
      say += "ay"
      say += " "
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"