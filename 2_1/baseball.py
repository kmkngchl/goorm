
import random

# 1. 정답 생성 (1~9 중 중복 없는 3자리)
answer = random.sample(range(1, 10), 3)

attempts = 0

print("⚾ 숫자야구 게임 시작!")
print("1~9 사이의 서로 다른 숫자 3개를 맞혀보세요.")

while True:
    guess = input("\n3자리 숫자를 입력하세요: ")

    # 2. 입력값 검사
    if len(guess) != 3 or not guess.isdigit():
        print("3자리 숫자를 입력해주세요.")
        continue

    if "0" in guess or len(set(guess)) != 3:
        print("1~9 사이의 중복되지 않는 숫자를 입력해주세요.")
        continue

    attempts += 1
    guess = list(map(int, guess))

    # 3. 스트라이크, 볼 계산
    strike = 0
    ball = 0

    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    # 4. 결과 출력
    if strike == 3:
        print(f"🎉 정답입니다! {attempts}번 만에 성공!")
        break
    elif strike == 0 and ball == 0:
        print("OUT!")
    else:
        print(f"{strike} 스트라이크, {ball} 볼")
