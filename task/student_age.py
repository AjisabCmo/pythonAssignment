def student_age():
    name =input("enter your name :").lower()
    students ={"dike":33 , "ope":25 , "melody": 20 , "precious": 27}
    for student in students.keys():
        if student == name:
            return f" hi, {name} ,your age is  {students.get(name)} years old"
    else:
        while name not in students.keys():
            age = int(input("name no found,enter your age: "))
            students.update({name:age})
            return f'hi, {name} , your age is {students.get(name)} years old '


print(student_age())
