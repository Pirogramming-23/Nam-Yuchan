#1단계
num=0 


# #2단계
# 부를숫자= input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


# #3단계
# while True: 
#     try:
#         부를숫자 = int(부를숫자)
#         if 1 <= 부를숫자 <= 3:
#             break
#         else:
#             print("1, 2, 3 중 하나를 입력하세요")
#             부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
#     except ValueError:
#         print("정수를 입력하세요")
#         부를숫자=input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")


# #4단계
# for i in range(부를숫자): 
#     num += 1
#     print(f"playerA : {num}")


# #5단계
# while True:
#     부를숫자= input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
#     try:
#         부를숫자 = int(부를숫자)
#         if 1 <= 부를숫자 <= 3:
#             break
#         else:
#             print("1, 2, 3 중 하나를 입력하세요")
#     except ValueError:
#         print("정수를 입력하세요.")

# for i in range(부를숫자):
#     num += 1
#     print(f"playerB : {num}")


# while True: 
#     if turn == 0:
#         현재플레이어= "playerA"
#     else: 
#         현재플레이어="playerB"
#     while True:
#         부를숫자= input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
#         try:
#             부를숫자 = int(부를숫자)
#             if 1 <= 부를숫자 <= 3:
#                 break
#             else:
#                 print("1, 2, 3 중 하나를 입력하세요")
#         except ValueError:
#             print("정수를 입력하세요.")
#     for i in range(부를숫자):
#         num += 1
#         print(f"{현재플레이어} : {num}")
#         if num >= 31:
#             break
# #7단계        
#     if num >= 31:
#         if turn == 0:
#             winner="playerB"
#         else:
#             winner="playerA"

#         print(f"{winner} win!")
#         break
#     turn = 1-turn

#8단계
def brGame(현재플레이어):
    global num
    while True:
        부를숫자= input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) : ")
        try:
            부를숫자 = int(부를숫자)
            if 1 <= 부를숫자 <= 3:
                break
            else:
                print("1, 2, 3 중 하나를 입력하세요.")
        except ValueError:
            print("정수를 입력하세요.")

    for i in range(부를숫자):
        num += 1
        print(f"{현재플레이어} : {num}")
        if num >= 31:
            break

#6단계
turn = 0 # 0: playerA, 1: playerB
while True:
    if turn == 0:
         현재플레이어= "playerA"
    else: 
         현재플레이어="playerB"
    brGame(현재플레이어)

#7단계
    if num >= 31:
        if turn == 0:
            winner="playerB"
        else:
            winner="playerA"

        print(f"{winner} win!")
        break
    turn = 1-turn
