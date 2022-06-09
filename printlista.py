def printlista(list,sel):
    for a in range(0, 6):
        if list[a][1] == '_':
            for b in range (0,5):
                print(list[a][b], end=(' '))
            print()
        else:
            if list[a] == sel:
                for b in range(0, 5):
                    print(f'\033[32m{list[a][b]}\033[m', end=(' '))
                print()
            else:
                for b in range(0, 5):
                    if list[a][b] == sel[b]:
                        print(f'\033[32m{list[a][b]}\033[m', end=(' '))
                    elif list[a][b] in sel:
                        print(f'\033[33m{list[a][b]}\033[m', end=(' '))
                    else:
                        print(f'\033[31m{list[a][b]}\033[m', end=(' '))
                print()