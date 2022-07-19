# DECORATOR
import datetime
import time


def tracking(old_function):
    def new_function(*args):
        start = datetime.datetime.now()
        current_time_start = start.strftime("%H:%M:%S")

        result = old_function(*args)

        end = datetime.datetime.now()
        current_time_end = end.strftime("%H:%M:%S")

        with open('logs/logs.log', 'a') as log:
            log.write(f'Start - {start}\n'
                      f'Time - {end - start}\n'
                      f'Name - {old_function.__name__}\n'
                      f'Arguments - {args}\n'
                      f'Value - {result}\n\n')

        print('Логи были записаны!')

        return result
    return new_function
