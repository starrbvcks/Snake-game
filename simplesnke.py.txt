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
print(f"num of words:{num_of_words}")