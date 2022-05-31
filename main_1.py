# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(first_word, second_word):
    
    # first_word = input("Pls enter your first word: ")
    # second_word = input("Pls enter your second word: ")

    first_word = first_word.lower().replace(" ", "")
    second_word = second_word.lower().replace(" ", "")


    if len(first_word) == len(second_word):
        if sorted(first_word) == sorted(second_word):
            return True
        else:
            return False
        
    else:
        return False


print(find_anagrams("hello", "check"))


