#coding=utf8
import time
import logging
logging.basicConfig(format='%(asctime)s - line:%(lineno)d - %(levelname)s - %(message)s', level=logging.DEBUG)
#logging.disable(level = logging.DEBUG)

def main():
    print(time.ctime())
    

if __name__ == '__main__':
    main()