from utils import config
from storage.db import add_storage


print config.list_section()
print config.get_config('broker','host')
print config.get_config('broker','username')
print config.get_config('broker','password')
print config.get_config('broker','queue')
add_storage("test")