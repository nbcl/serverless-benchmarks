
from time import sleep

def handler(event):
    # start timing
    sleep_time = event.get("sleep", default=False)
    if not sleep_time:
        return 'Error: No key "sleep" found on input data.'
    elif not isinstance(sleep_time, (int, float)):
        return f'Error: Key "sleep" expected int or float, not {type(sleep_time)}.'

    sleep(sleep_time)
    return { 'result': sleep_time }
