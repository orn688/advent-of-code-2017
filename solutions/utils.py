import os
import glob
import requests


def get_input_for_day(day):
    """
    Return the AoC input for a given day, first checking to see if the input
    has already been cached locally.
    """
    session_id = os.environ['SESSION_ID']
    cookies = dict(session=session_id)

    input_directory_name = os.path.join('.', 'puzzle_inputs')
    if not os.path.isdir(input_directory_name):
        os.mkdir(input_directory_name)

    input_files = glob.glob(os.path.join(input_directory_name, '*.txt'))
    day_input_file = os.path.join(input_directory_name,
                                  f'day{str(day).zfill(2)}.txt')

    if day_input_file in input_files:
        with open(day_input_file) as f:
            day_input = f.read()
    else:
        input_url = f'http://adventofcode.com/2017/day/{day}/input'
        response = requests.get(input_url, cookies=cookies)

        day_input = response.text.strip()

        with open(day_input_file, 'w') as f:
            f.write(day_input)

    return day_input
