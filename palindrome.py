# user_input = str(input("What is the your word: "))


#extened slice syntax
#slice[start:stop:step]
#colon instead of an index number will assume "start" for first color "end" for second colon
#if step is negative it will run in reverse
# reverse_word = user_input[::-1])
#
# def is_palindrome(reverse_word):
#     if(reverse_word == user_input):
#         return("{0} is a palindrome!".format(user_input))
#     else:
#         return("{0} is NOT a palindrome!".format(user_input))
# print(is_palindrome(reverse_word))

#or

user_input2 = str(input("What is the your word: "))


def backwards_user_input(user_input2):
    #defining the variable to store the concatenated letters
    reversed_word = ""
    for index in range(len(user_input2) - 1, -1, -1):
        #adding the letters to the variable beginning from the last index
        reversed_word = reversed_word + user_input2[index]
    return reversed_word

backwards = backwards_user_input(user_input2)


def palindrome(user_input2):
    if (user_input2 == backwards):
        print('palindrome')
    else:
        print("not a palindrome")

palindrome(user_input2)
