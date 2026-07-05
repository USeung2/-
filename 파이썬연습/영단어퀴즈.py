import random

def get_words():
    words = {}
    n = int(input("단어 개수를 입력하세요: "))

    for i in range(n):
        while True:
            print(f"\n{i+1}번째 단어")
            word = input("영단어: ").strip()
            meaning = input("뜻: ").strip()

            # 공백 입력 방지
            if word == "" or meaning == "":
                print("영단어와 뜻은 비워둘 수 없습니다.")
                continue

            # 중복 입력 방지
            if word in words:
                print("이미 입력한 영단어입니다.")
                continue

            words[word] = meaning
            break

    return words


def quiz_round(words):
    word_list = list(words.keys())
    random.shuffle(word_list)

    correct = []
    wrong = []

    for word in word_list:
        mode = random.choice([0, 1])

        # 뜻 -> 영단어
        if mode == 0:
            answer = input(f"\n뜻: {words[word]}\n영단어: ").strip()

            if answer.lower() == word.lower():
                print("정답!")
                correct.append(word)
            else:
                print(f"오답! 정답은 {word}")
                wrong.append(word)

        # 영단어 -> 뜻
        else:
            answer = input(f"\n영단어: {word}\n뜻: ").strip()

            if answer == words[word]:
                print("정답!")
                correct.append(word)
            else:
                print(f"오답! 정답은 {words[word]}")
                wrong.append(word)

    return correct, wrong


def show_result(correct, wrong, total):
    correct_count = len(correct)
    wrong_count = len(wrong)
    accuracy = correct_count / total * 100

    print("\n===== 결과 =====")
    print(f"정답: {correct_count}개")
    print(f"오답: {wrong_count}개")
    print(f"정답률: {accuracy:.1f}%")


def review_wrong(words, wrong_list):
    wrong_words = {w: words[w] for w in wrong_list}
    correct, wrong = quiz_round(wrong_words)
    show_result(correct, wrong, len(wrong_words))


def main():
    words = get_words()

    correct, wrong = quiz_round(words)
    show_result(correct, wrong, len(words))

    if wrong:
        retry = input("\n틀린 단어 다시 풀어볼까요? (y/n): ").strip().lower()

        if retry == "y":
            review_wrong(words, wrong)


main()