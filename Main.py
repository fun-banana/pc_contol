from loguru import logger
import atexit
from datetime import datetime


def on_exit():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logger.info(f'[{now}] End proccess!!')

def on_run():
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    logger.info(f'[{now}] Start proccess!!')

def main():
    on_run()
    input('Wait')

if __name__ == '__main__':
    logger.add('log.log', format='[{level}]\t[{time}] [{file}]: {message}')
    atexit.register(on_exit)
    main()