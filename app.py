import sys
import configparser
sys.path.append("./generator")
sys.path.append("./configuration")
from generate import generate
from config import config_type,set_config,set_fname


def main(arg1, arg2):
    set_config(arg1)
    set_fname(arg2)
    generate(config_type())
    
    print(arg1, arg2)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)

#.configuration/configs.ini