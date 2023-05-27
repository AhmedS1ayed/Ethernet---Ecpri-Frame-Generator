import sys
import os
sys.path.append("./generator")
sys.path.append("./configuration")
from generate import generate
from config import config_type,set_config,set_fname


def main(arg1 = 'config.ini', arg2 = 'packets.txt'):
    if(not os.access(arg1,os.R_OK)):
        print(arg1 + ' has no read permission')
        return 0
    
    if(not os.access(arg2,os.W_OK)):
        print(arg2 + ' has no write permission')
        return 0
    
    try :
        set_config(arg1)
        set_fname(arg2)
        generate(config_type())
    except :
        print("config file is not valid")
    
    print(arg1, arg2)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)