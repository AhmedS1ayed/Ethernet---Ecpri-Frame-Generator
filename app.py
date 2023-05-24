import sys
sys.path.append("./generator")
sys.path.append("./configuration")
from generate import generate_eth,generate_ecpri
from config import config_type

if(config_type() == 'ethernet') :
    generate_eth()
elif(config_type() == 'ecpri') :
    generate_ecpri()