'''
Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

Input
The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

Output
Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

Examples

Input
4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis

Output
word
l10n
i18n
p43s
'''

# n = int(input())
# word = []
# for i in range(n):
#     i = input()
#     word.append(i)

# for i in word:
#     if len(i) <= 10:
#         print(i)
#     else:
#         k = list(i)
#         y = ''
#         y = k[0]
#         y += str(len(i) - 2)
#         y += k[-1]
#         print(y)

def abbrevations(word):
    k = []
    for i in word:
        if len(i) <= 10:
            k.append(i)
        else:
            y = list(i)
            t = ''
            t = y[0]
            t += str(len(i) - 2)
            t += y[-1]
            k.append(t)
    return k

print(abbrevations(['word', 'localization', 'internationalization', 'pneumonoultramicroscopicsilicovolcanoconiosis']))