words = input().split(' ')
palindrome = input()
palindrome_list = []
word_list = []
counter = 0
for word in words:
    reverse_word = word.split()
    reverse_word.reverse()
    reverse_word = ''.join(reverse_word)
    if word == reverse_word:
        palindrome_list.append(word)
print(f"{palindrome_list}")
result = [x for x in palindrome_list if x == palindrome ]
counter = len(result)

print(f"Found palindrome {counter} times")
