







import winsound
import time







def binary_confirmation(message):
    """
    Print a message and enter yes to continue
    """

    print(message)
    response = str(input())

    if response == "yes":
        return 
    else : 
        print("negative answer")
        binary_confirmation(message)



def sound_notification():


    for i in range(10):
        winsound.Beep(1000, 2000)
        time.sleep(2)

