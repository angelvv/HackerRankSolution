if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores.append(score)
    
    highest2 = sorted(set(scores))[1]
    for student, s in sorted(students):
        if s == highest2:
            print(student)

