word=input("문자열을 입력: ")

length=len(word)

if length%2==1:
    middle = word[length//2]
    print("중간 글자는 ", middle)
else:
    mid1 = word[length//2-1]
    mid2 = word[length//2]
    print("중간 글자는 ", mid1, mid2)
