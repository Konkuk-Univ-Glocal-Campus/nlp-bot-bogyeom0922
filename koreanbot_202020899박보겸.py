import random

# 무작위 답변
random_responses = ["그랬군요. 다음엔 더 좋은 결과가 있을 거예요.",
                    "그런 일이 있었다고요? 더 자세히 이야기해 주세요.",
                    "이번엔 다른 이야기를 해보는 것은 어떤가요?",
                    "요즘 날씨가 정말 덥죠?",
                    "정말 재밌네요!",
                    "얼마 전까지 시험 기간이었는데 시험은 잘 보셨나요?",
                    "요즘 학교생활은 어떠세요?",
                    "최근 고민거리는 없었나요?"]

print("안녕하세요. 저는 당신의 친구가 되어줄 로봇입니다.")
print("언제든지 '잘가'를 입력하여 이 대화를 끝낼 수 있습니다.")
print("제 말에 답변한 후 'Enter'를 누르세요!")
print("오늘 하루 어떠셨나요?")

while True:
    # 상대방의 답변 입력
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # 잘가라고 입력 시 대화 종료
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("함께 대화해서 정말 재밌었어요. 다음에 또 만나요!")
