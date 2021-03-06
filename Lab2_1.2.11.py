'''
Prepared by Alina Stryeltsova
Architecture of Computing Systems
LAB2 1.2.11
'''
import random

WIDTH = 14


def tick():
    input("Press Enter")


def prepare(_p, cmd):
    _p['IR'] = cmd
    _p['AC'] = _p['R1']
    _p['TC'] = 1
    _p['PC'] += 1


def to_register(s):
    x = int(s)
    data = to_binary(abs(x))

    if x < 0:
        for i in range(WIDTH):
            if data[i] == 0:
                data[i] = 1
            else:
                data[i] = 0

        owerflow = 1

        for i in range(WIDTH):
            x = data[i] + owerflow
            data[i] = x % 2
            owerflow = x // 2

    return data


def to_binary(x):
    data = [0] * WIDTH
    for i in range(WIDTH):
        data[i] = x % 2
        x = x // 2
    return data


def execute(_p):
    cmd = _p['IR']

    if cmd.startswith('MOV'):
        if cmd.startswith('MOV '):  # mov_to_r1 10
            src = int(cmd.replace('MOV', ''))
            _p['R1'] = get_data(_p, src)
            set_ps(_p, 'R1')
            p['AC'] = p['R1']
    elif cmd.startswith('INV '):  # inv 1/0
        arg1 = int(cmd.replace('INV ', ''))

        for i in range(arg1, WIDTH, 2):
            _p['R1'][i] = 0 if _p['R1'][i] == 1 else 1
            p['AC'] = p['R1']

    _p['TC'] = 2


def set_ps(_p, dst):
    if _p[dst][WIDTH - 1] == 0:
        _p['PS'] = '+'
    else:
        _p['PS'] = "-"


def get_data(_p, src):
    if src in ['R1', 'R2', 'R3', 'AC']:
        data = _p[src]
    else:
        data = to_register(src)
    return data


def show(_p):
    print()
    for k, v in _p.items():
        if k not in ['R1', 'R2', 'R3', 'AC']:
            print(f'{k}: {v}')
        else:
            print(f'{k}: {" ".join(map(str, v[::-1]))}')
    print()
R1 = [random.choice([0, 1]) for _ in range(WIDTH)]
R2 = [random.choice([0, 1]) for _ in range(WIDTH)]
R3 = [random.choice([0, 1]) for _ in range(WIDTH)]
AC =[random.choice([0, 1]) for _ in range(WIDTH)]

p = {
    'R1': R1,
    'R2': R2,
    'R3': R3,
    'AC': AC,
    'IR': "",
    'PS': "+",
    'PC': 0,
    'TC': 0
}


for line in open('commands.txt').readlines():
    print('Prepare:')
    prepare(p, line.strip())
    show(p)
    tick()

    print('Execute:')
    execute(p)
    show(p)
    tick()
