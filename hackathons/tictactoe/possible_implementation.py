

def print_field(field):
    print('--------' * len(field[0]))
    for row in field:
        res = '   |   '.join(row)
        res = f"|   {res}   |"
        print(res)
        print('--------' * len(row))


def check_field(field):
    n = len(field)
    m = len(field[0])

    all_got = True

    for i in range(n):
        for j in range(m):
            if field[i][j] != ' ':
                all_got = False
                break
        if not all_got:
            break

    if all_got:
        return 'tie'

    for i in range(n):
        for j in range(m):
            for delta_i, delta_j in [[1, 1], [1, 0], [0, 1]]:
                if (i + 2 * delta_i) >= n: continue
                if (j + 2 * delta_j) >= m: continue

                if (field[i][j] == field[i + delta_i][j + delta_j] == field[i + 2 * delta_i][j + 2 * delta_j]) \
                    and field[i][j] != ' ':

                    return field[i][j]
    return 'continue'


field = [
    [' ', 'o', 'x', 'x'],
    [' ', ' ', ' ', 'o'],
    ['x', ' ', 'x', ' '],
    ['o', ' ', 'x', ' ']
]

print_field(field)
print(check_field(field))

field = [
    [' ', 'x', 'x', 'x'],
    [' ', ' ', ' ', 'o'],
    ['x', ' ', 'x', ' '],
    ['o', ' ', 'x', ' ']
]


print_field(field)
print(check_field(field))


field = [[' ' for _ in range(5)] for _ in range(5)]

cur_move = 'x'
while True:

    print_field(field)

    x, y = map(int, input(f"Move {cur_move}. coords:\n--> ").split())
    field[x][y] = cur_move

    if check_field(field) == 'continue':
        cur_move = 'o' if cur_move == 'x' else 'x'
    else:
        print(check_field(field))
        break
