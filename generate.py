import random




def generate(solution_length:int)->list:
    solution = str(random.randint(int("9"*(solution_length-1)), int("1"+"0"*solution_length)))
    s2 = str(random.randint(int("9"*(solution_length-1)), int(solution)))
    s1 = str(int(solution)-int(s2))

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = random.sample(letters, 10)
    
    s1code = ""
    s2code = ""
    s3code = ""
    for n in s1:
        s1code+=mapping[int(n)]
    for n in s2:
        s2code+=mapping[int(n)]
    for n in solution:
        s3code+=mapping[int(n)]

    return [s1code, s2code, s3code]



if __name__ == '__main__':
    while True:
        print(generate(int(input("How many digits should the solution have?  "))))
