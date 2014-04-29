from pizza.pizza import Pizza
from utils.config import get_config

def add_storage(name,type="zfs",capacity=None):
    default_capacity = get_config('storage','default_capacity')
    default_pool = get_config('storage','default_pool')
    pool = Pizza()
    
    if capacity :
        capacity = capacity
    else :
        capacity = default_capacity
        
    if type == 'zfs' :
        attr = {'quota' : capacity }
        pool.create_dataset(default_pool,name,attribute=attr)
    elif type == "zvol" :
        pool.create_zvol(default_pool,name,capacity)
    else :
        pass
    
def attach_storage(name,vm_name):
    pass

def destroy_storage(name):
    pass

def resize_storate(name,new_capacity):
    pass



