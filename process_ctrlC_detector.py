



import signal
import sys
import time

from global_variables import *
from functions_log import *

def signal_handler(sig, frame):
    print('Signal SIGINT capturé (Ctrl+C)')
    
    Variable("program_on").set(False)
    sys.exit(0)



def processCTRLcDetector():

    

    # Associer le gestionnaire de signal à SIGINT (Ctrl+C)
    signal.signal(signal.SIGINT, signal_handler)

    print("Le programme est en cours d'exécution. Appuyez sur Ctrl+C pour le terminer.")



    while True:
        log_write("working process", "processCTRLcDetector")
        time.sleep(1)
        pass
