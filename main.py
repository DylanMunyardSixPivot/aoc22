import sys

import day1
import day2

if __name__ == '__main__':
    day = sys.argv[1] if len(sys.argv) >= 2 else '1'
    match day:
        case '1':
            day1.solve()
        case '2':
            day2.solve()
        case _:
            print(f'day {day} not solved')

