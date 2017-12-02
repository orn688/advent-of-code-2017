import os
import requests


def get_input_for_day(day):
    session_id = os.environ['SESSION_ID']
    cookies = dict(session=session_id)

    input_url = f'http://adventofcode.com/2017/day/{day}/input'

    response = requests.get(input_url, cookies=cookies)

    return response.text.strip()
