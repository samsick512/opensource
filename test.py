
def findMAx(a,b,c):
    if a>b:
        big=a
    else:
        big=b

    if c>big:
        big=c

    return biggest


a=int(input("첫 번째 숫자 입력:"))
b=int(input("두 번째 숫자 입력:"))
c=int(input("세 번째 숫자 입력:"))

biggest= findMAx(a,b,c)

print(a,b,c,"중 가장큰 수는", biggest,"입니다.")
