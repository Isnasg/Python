def canmakepalindrome(word):
    charcount = {}
    oddcount = 0

    for char in word:
        if char in charcount:
            charcount += 1
        else:
            charcount[char] = 1

    for count in charcount.values():
        if count % 2 != 0:
            oddcount += 1

    if oddcount > 1:
        return False

    palindrome =''
    middlechar = ''

    for char, count in charcount.items():
        if count % 2 != 0:
            middlechar = char
        palindrome.extend([char] * (count // 2))

    palindromestr = ''.join(palindrome) + middlechar + ''.join(palindrome[::-1])
    return palindromestr


word = input()
result = canmakepalindrome(word)
if not result:
    print("Cannot make a palindrome from the word")
else:
    print(result)