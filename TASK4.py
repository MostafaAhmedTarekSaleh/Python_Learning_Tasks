#Word Frequency Counter

#Can also be carried out much faster using the Counter class from the "collections" module :)

"""
Sample paragraph:
Nory was a Catholic Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic,
and her father was a Catholic because his mother was  Catholic, or had been
"""


def word_counts(origin_str):

    word_list = origin_str.split()
    counts_list = []
    word_dict = {}

    # Must remove duplicate words from word_list , creating a dictionary does just that

    word_dict = dict.fromkeys(word_list)



    for key in word_dict:
        counter = 0
        for i in range(len(word_list)):
            if word_list[i] == key:
                counter+=1
        counts_list.append(counter)


    word_dict.update(zip(word_dict,counts_list))

    return word_dict

user_paragraph = input("Input the paragraph to be analysed:\n")
result = word_counts(user_paragraph)

ranking= 0
print("\n\nThe 5 most common words:")

for word in sorted(result, key=result.get, reverse=True):
    if ranking in range(5):
        print(f"\nWord: {word}\t\tFrequency:{result[word]}")
        ranking += 1

        