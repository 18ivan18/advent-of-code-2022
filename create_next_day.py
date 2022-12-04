#!/usr/bin/env python3
import os
import requests
import shutil
import stat
from bs4 import BeautifulSoup


advent_of_code_base_url = 'https://adventofcode.com'
year = 2022
main_dir = 'solutions'

if (not os.path.exists(main_dir)):
    os.mkdir(main_dir)


def get_next_day() -> int:
    days = [int(x[3:]) for x in os.listdir(main_dir)]
    days.append(0)
    return sorted(days, reverse=True)[0] + 1


def get_day_url(day: int) -> str:
    return f"{advent_of_code_base_url}/{year}/day/{day}"


day = get_next_day()
day_str = f"day{day}"
url = get_day_url(day)

response = requests.get(url)

if(not response):
    print('\033[1m' + "You're all up to date.")
    exit(0)

shutil.copytree('day_x_template', os.path.join(main_dir, f"day{day}"))
main_py_dir = os.path.join(main_dir, day_str, 'main.py')
os.chmod(main_py_dir, os.stat(main_py_dir).st_mode | stat.S_IEXEC)

soup = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
with open(os.path.join(main_dir, day_str, 'README.md'), 'w') as fd:
    fd.write(soup.find('main').get_text())

print('\033[1m' + f"Successfully created day {day}!\n{url}")
