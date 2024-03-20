



global_lock = None

def global_lock_set(gl):
    global global_lock
    global_lock = gl

def global_lock_get():
    global global_lock
    if global_lock == None :
        """
        DEBUG add an infinite loop
        """
        print("Error critic : global_lock == None in global_lock_get() function -see global variables lock manager")
    return global_lock




