import sys
import json

def count_questions(data: dict):
    question_count = 0
    for round in data["game"]["rounds"]:
        question_count += len(round["questions"])
    print(f"Количество вопросов: {question_count}")

def print_right_answers(data: dict):
    print("Правильные ответы:")
    for round in data["game"]["rounds"]:
        for question in round["questions"]:
            print(question["correct_answer"])

def print_max_answer_time(data: dict):
    max_time = 0
    for round in data["game"]["rounds"]:
        for question in round["questions"]:
            if "time_to_answer" in question:
                max_time = max(max_time, question["time_to_answer"])
        max_time = max(max_time, round["settings"]["time_to_answer"])
    print(f"Максимальное время ответа: {max_time}")

def main(filename):
    with open(filename) as f:
        data = json.load(f)
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)