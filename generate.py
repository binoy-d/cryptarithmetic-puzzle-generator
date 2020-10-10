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


def format_test(num, inputs: list)->None:
    print(f"\n\nTEST(GeneratedCasesYes, YesTest_{num}_Size{len(inputs[2])})", end = "{\n")
    print("\tstd::map<char, unsigned> puzzle;")
    print(f'\tbool p1 = puzzleSolver("{inputs[0]}", "{inputs[1]}", "{inputs[2]}", puzzle);')
    print(f'\tEXPECT_TRUE( p1 &&  gradeYesAnswer("{inputs[0]}", "{inputs[1]}", "{inputs[2]}", puzzle) );\n\n')
    print("}\n\n")

if __name__ == '__main__':
    num = 0
    while True:
        format_test(num:=num+1, generate(int(input("How many digits should the solution have?  "))))
