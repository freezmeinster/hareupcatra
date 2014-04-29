import ConfigParser
import os

here = os.path.abspath(os.path.dirname(__file__))
conf_path = os.path.join(here,"../hareupcatra.conf")
config = ConfigParser.ConfigParser()
config.readfp(open(conf_path))


def get_config(section,item,type="string"):
        
    if type == "integer" :
        return config.getint(section,item)
    elif type == "float" :
        return config.getfloat(section,item)
    elif type == "boolean" :
        return config.getboolean(section,item)
    else :
        return config.get(section,item)
        
def list_section():
    return config.sections()