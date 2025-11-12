# LEVEL UP! Bonus Challenge
# Challenge: Count Word Frequency in a Text File

# word_frequency.py
# Challenge: Count Word Frequency in a Text File

def count_word_frequency(filename):
    

    word_counts = {}
    with open(filename, "r") as file:
        text = file.read().lower()  
        for ch in ".,!?;:":
            text = text.replace(ch, "")
        words = text.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    return word_counts



print(count_word_frequency("sample.txt"))
