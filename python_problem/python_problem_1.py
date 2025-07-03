#1단계
num=0 


#2단계
부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


#3단계
while True: 
    try:
        부를숫자 = int(부를숫자)
        if 1 <= 부를숫자 <= 3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
            부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    except ValueError:
        print("정수를 입력하세요")
        부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


#4단계
for i in range(부를숫자): 
    num += 1
    print(f"playerA : {num}")


#5단계
while True:
    부를숫자= input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
    try:
        부를숫자_b = int(부를숫자)
        if 1 <= 부를숫자_b <= 3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요")
    except ValueError:
        print("정수를 입력하세요.")

for i in range(부를숫자_b):
    num += 1
    print(f"playerB : {num}")