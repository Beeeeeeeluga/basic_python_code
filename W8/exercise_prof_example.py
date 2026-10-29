def add_student(new_name, new_score, d):
    if new_name not in d:
        number = 1

        while new_name + "-" + str(number) in d:
            number = number + 1

        if number == 1:
            d[new_name] = new_score
        else:
            d[new_name + "-" + str(number)] = new_score

        return d

    if new_name in d:
        score_of_existing_name = d.pop(new_name)

        d[new_name + "-1"] = score_of_existing_name
        d[new_name + "-2"] = new_score

        return d

Student_name = ["Alan", "Bob", "Marco"]
updated_score = [43, 60, 100]

d = {}

for i in range(len(Student_name)):
    add_student(Student_name[i], updated_score[i], d)

add_student("Bob", 99, d)

count = 0

for score in d.values():
    if score > 60:
        count = count + 1

print("Question 3:", count)

add_student("Bob", 60, d)

print(d)
