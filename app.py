import sys
sys.path.append("./generator")
from generate import generate_eth,generate_ecpri
from config.config import config_type


if(config_type() == 'ethernet') :
    generate_eth()
elif(config_type() == 'ecpri') :
    generate_ecpri()