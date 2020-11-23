def reverse(str1):
    reverseStr = ''
    for i in range(len(str1)):
        reverseStr = str1[i] + reverseStr
        return reverseStr
