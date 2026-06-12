def get_input_text():
    text = input("Type your sentence \n")
    return text
   
def split_words(text):    
    words = text.split()
    return words

def count_words(words):
    return len(words)



text = get_input_text()
words = split_words(text)
print(f"words: {words}")

num_of_words = count_words(words)
<<<<<<< HEAD
print(f"num of words:{num_of_words}")
=======
print(f"num of words:{num_of_words}")
>>>>>>> 0428c6629cc10af4aa8c3680fe607bd355c441be
