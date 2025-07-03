num=0 #1단계


부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ") #2단계


while True: #3단계
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


for i in range(부를숫자): #4단계
    num += 1 # num을 1씩 증가
    print(f"playerA : {num}")