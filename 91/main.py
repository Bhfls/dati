# BEGIN: 9ycx9r934x4
def calculate_score(answer_key, student_answers):
    score = 0
    for i in range(len(answer_key)):
        if student_answers[i] == answer_key[i]:
            score += 30
        elif student_answers[i] == 'E':
            pass
        else:
            pass
    return score

# 假设正确答案为 "DCBAD"
answer_key = "DCBAD"

# 选手提交的答案
student_answers = input()

# 计算并打印选手的总分
total_score = calculate_score(answer_key, student_answers)
print( total_score)
# END: 9ycx9r934x4
