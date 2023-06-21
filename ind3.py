sentence = "The quick brown fox jumps over the lazy dog"
new_sentence = ""

for i in range(len(sentence)):
    if i % 2 == 0 or sentence[i] != "o":
        new_sentence += sentence[i]

        print(new_sentence)