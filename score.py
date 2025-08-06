INPUT_FILE = "score.txt"
OUTPUT_FILE = "score_graded.txt"


def evaluate_grade(score):
    """점수에 따른 학점을 반환하는 함수."""
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        raise ValueError("점수는 0 ~ 100 사이의 숫자여야 합니다.")

    if score >= 95:
        return "A+"
    elif score >= 90:
        return "A"
    elif score >= 85:
        return "B+"
    elif score >= 80:
        return "B"
    elif score >= 75:
        return "C+"
    elif score >= 70:
        return "C"
    elif score >= 65:
        return "D+"
    elif score >= 60:
        return "D"
    else:
        return "F"


def process_score_line(line):
    """한 줄을 처리하여 점수와 학점을 반환하거나 원본 라인을 반환합니다."""
    tokens = line.strip().split()

    if not tokens:  # 빈 줄에 대한 처리
        return line

    try:
        score = int(tokens[0])
        grade = evaluate_grade(score)
        return f"{score:<6}{grade:<6}\n"
    except (ValueError, IndexError):
        # 숫자가 아니거나 파싱할 수 없는 경우 원본 라인 유지
        return line


def main():
    try:
        print("채점을 시작합니다.")

        # 파일 읽기 (with 블록을 간결하게)
        with open(INPUT_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()

        # 각 줄 처리 (파일 외부에서)
        processed_lines = [process_score_line(line) for line in lines]

        # 마지막 줄의 줄바꿈 문자 제거
        if processed_lines:
            processed_lines[-1] = processed_lines[-1].rstrip("\n")

        # 결과를 파일에 저장
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.writelines(processed_lines)

        # 처리 완료 메시지 출력
        print(f"채점이 완료되었습니다. 결과는 '{OUTPUT_FILE}'에 저장되었습니다.")

    except FileNotFoundError:
        print(f"오류: '{INPUT_FILE}' 파일을 찾을 수 없습니다.")
    except PermissionError:
        print(f"오류: 파일에 대한 권한이 없습니다.")
    except Exception as e:
        print(f"예상치 못한 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
