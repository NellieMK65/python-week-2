"""
Have the function CodelandUsernameValidation(str) take the str parameter
being passed and determine if the string is a valid username according to
the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true,
otherwise return the string false.
"""

def CodelandUsernameValidation(input_string):

  # code goes here
  #check the length if input string
  username_length= len(input_string)
  first_char = input_string[0]
  last_char = input_string[-1]

  if username_length <= 4 or username_length >= 25:
    return 'False'
  #checking if the first character is a letter
  if not first_char.isalpha():
    return 'False'
  #a for loop to iterate the characters in the input string
  #check if the characters are alphanumeric or '_'
  for char in input_string:
    if not (char.isalpha() or char.isdigit() or char=='_'):
      return 'False'
  #checking if the last character is an '_'
  if last_char == '_':
      return 'False'
  else:

    return 'True'

# keep this function call here
print(CodelandUsernameValidation(input()))
