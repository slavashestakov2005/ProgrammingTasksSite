import random
import subprocess


def generator(variables: dict, number: int):
    for v, info in variables.items():
        with open(f'tests\{number}_input.txt', 'a') as inp:
            if info[0] == int:
                t = random.randint(info[1], info[2])
                inp.write(str(t) + '\n')
            elif info[0] == float:
                t = random.randint(info[1] * 10 ** info[3], info[2] * 10 ** info[3]) / 10 ** info[3]
                inp.write(str(t) + '\n')


def generator_of_tests(code: str, count: int, variables: dict):
    with open('code.txt', 'w+') as code_file:
        code_file.write(code)
    for i in range(count):
        generator(variables, i)
        with open(f'tests\{i}_out.txt', 'w') as out, open(f'tests\{i}_input.txt', 'r') as inp, open(
                f'tests\{i}_err.txt', 'w+') as err:
            subprocess.run(args="python code.txt", stdout=out, stderr=err, stdin=inp)


generator_of_tests(
    '''a = float(input())\nb = float(input())\nc = int(input())\nprint(int(a), a)\nprint(int(b), b)\nprint(c ** 2)''',
    30,
    {'a': (float, 0, 10000, 5), 'b': (float, 0, 10000, 2), 'c': (int, 0, 20)})
