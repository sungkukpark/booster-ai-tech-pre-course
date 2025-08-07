# [연습] 무슨 학교 다니세요?
from datetime import date


def evaluate_school_stage(age):
    if age < 7:
        return "학생이 아닙니다"
    elif age < 14:
        return "초등학생"
    elif age < 17:
        return "중학생"
    elif age < 20:
        return "고등학생"
    elif age <= 26:
        return "대학생"
    else:
        return "학생이 아닙니다"


def main():
    current_year = date.today().year

    birth_year = -1
    while True:
        try:
            birth_year = int(
                input("당신이 태어난 년도를 입력하세요 (0 입력 시 종료): ")
            )
            if birth_year == 0:
                print("프로그램을 종료합니다.")
                return
            if birth_year < 1900 or birth_year > current_year:
                print("올바른 출생 연도를 입력하세요.")
                continue
            break
        except ValueError:
            print("숫자를 입력해주세요.")

    age = current_year - birth_year
    school_stage = evaluate_school_stage(age)

    if school_stage == "학생이 아닙니다":
        print(f"당신은 {age}살이며 {school_stage}")
    else:
        print(f"당신은 {age}살이며 '{school_stage}'입니다")


if __name__ == "__main__":
    main()
