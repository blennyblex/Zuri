# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):


    word = word.lower().replace(" ", "")
    anagram = anagram.lower().replace(" ", "")


    if len(word) == len(anagram):
        if sorted(word) == sorted(anagram):
            return True
        else:
            return False
        
    else:
        return False


print(find_anagrams("below", "elbow"))


