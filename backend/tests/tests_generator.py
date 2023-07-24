import random
import subprocess
import numpy as np


def default_generator(variables: dict):
    for v, info in variables.items():
        if info[0] == int:
            t = random.randint(*info[1])
        elif info[0] == float:
            t = random.randint(*map(lambda x: x * 10 ** info[2])) / 10 ** info[2]
        elif info[0] == str:
            t = ''.join(random.choices(info[2], k=random.randint(*info[1])))
        elif info[0] == list:
            t = tuple(np.random.randint(low=info[2][0], high=info[2][1], size=random.randint(*info[3])))
            if info[1]:
                yield len(t)
        yield t


def write_inputs(inputs: tuple, number: int):
    with open(f'tests\{number}_input.txt', 'a') as inp:
        for i in inputs:
            if type(i) == tuple:
                inp.write(' '.join(map(str, i)) + '\n')
            else:
                inp.write(str(i) + '\n')


def generator_of_tests(code=None, code_name=None, count: int = 0, variables: dict = {}, generator=default_generator):
    if code:
        with open('code.txt', 'w+') as code_file:
            code_file.write(code)
    for i in range(count):
        write_inputs(generator(variables), i)
        with open(f'tests\{i}_out.txt', 'w') as out, open(f'tests\{i}_input.txt', 'r') as inp, open(
                f'tests\{i}_err.txt', 'w+') as err:
            subprocess.run(args=f"python {'code.txt' if code else code_name}", stdout=out, stderr=err,
                           stdin=inp)
