#coding=utf8
import time
import logging
logging.basicConfig(format='%(asctime)s - line:%(lineno)d - %(levelname)s - %(message)s', level=logging.DEBUG)
#logging.disable(level = logging.DEBUG)

def main():
    print(time.ctime())
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('record.log', 'w') as fw:
        fw.write(now)
        fw.write('\n')
        fw.write(time.ctime())
    

if __name__ == '__main__':
    main()