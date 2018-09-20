user_input = str(input("What is the your word: "))


#extened slice syntax
#slice[start:stop:step]
#colon instead of an index number will assume "start" for first color "end" for second colon
#if step is negative it will run in reverse
reverse_word = user_input[::-1])

def is_palindrome(reverse_word):
    if(reverse_word == user_input):
        return("{0} is a palindrome!".format(user_input))
    else:
        return("{0} is NOT a palindrome!".format(user_input))
print(is_palindrome(reverse_word))
