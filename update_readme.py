#!/usr/bin/env python3

import os
import re

main_dir = 'solutions'


def get_latest_day() -> int:
    days = [int(x[3:]) for x in os.listdir(main_dir)]
    days.append(0)
    return sorted(days, reverse=True)[0]


day = get_latest_day()
day_str = f"day{day}"
with open(os.path.join(main_dir, day_str, 'README.md')) as f:
    problem_name = f.readline()[7:-5]

with open('README.md', 'r+') as readme:
    input = readme.read()
    if problem_name not in input:
        readme.write(f"- [{problem_name}](./{main_dir}/{day_str})\n")
    else:
        print(f"{problem_name} already added to README.md")
