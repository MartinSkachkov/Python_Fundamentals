def anagram_check(word, word_list):
    if len(word) != len(word_list):
        return 'No'

    for i in range(len(word)):
        if (word[i] not in word_list) or (word_list[i] not in word):
            return 'No'

    return 'Yes'


word = input()
n = int(input())
words = []

for _ in range(n):
    words.append(input())

for w in words:
    print(anagram_check(word, w))
