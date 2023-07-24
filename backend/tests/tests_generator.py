import random
import subprocess
from string import ascii_letters
import numpy as np


def default_generator(variables: dict, number: int):
    for v, info in variables.items():
        with open(f'tests\{number}_input.txt', 'a') as inp:
            if info[0] == int:
                t = random.randint(*info[1])
                inp.write(str(t) + '\n')
            elif info[0] == float:
                t = random.randint(*map(lambda x: x * 10 ** info[2])) / 10 ** info[2]
                inp.write(str(t) + '\n')
            elif info[0] == str:
                t = ''.join(random.choices(info[2], k=random.randint(*info[1])))
                inp.write(t + '\n')
            elif info[0] == list:
                t = np.random.randint(low=info[2][0], high=info[2][1], size=random.randint(*info[3]))
                inp.write(str(len(t)) + '\n')
                if info[1]:
                    inp.write(' '.join(map(str, t)) + '\n')


def generator_of_tests(code=None, code_name=None, count: int = 0, variables: dict = {}, generator=default_generator):
    if code:
        with open('code.txt', 'w+') as code_file:
            code_file.write(code)
    for i in range(count):
        generator(variables, i)
        with open(f'tests\{i}_out.txt', 'w') as out, open(f'tests\{i}_input.txt', 'r') as inp, open(
                f'tests\{i}_err.txt', 'w+') as err:
            subprocess.run(args=f"python {'code.txt' if code else code_name}", stdout=out, stderr=err,
                           stdin=inp)


generator_of_tests(code_name='my_code.txt',
                   count=10,
                   variables={'a': (list, True, (0, 100), (0, 100)), 'n': (int, (0, 10 ** 4))})
