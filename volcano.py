import random
import time
import threading
from queue import Queue

class Volcano(threading.Thread):

    def __init__(self, treasure_queue: Queue, stop_svent: threading.Event) -> None:
        super().__init__()
        # Fronta kde vkláda sopka poklady
        self.__treasure_queue: Queue = treasure_queue
        # Ukončení všech vláken
        self.__stop_event: threading.Event = stop_svent

    def run(self) -> None:
        while not self.__stop_event.is_set():
            # Náhodný interval pro vyvrhnutí pokladů
            sleep_time: float = random.uniform(0, 5)
            time.sleep(sleep_time)

            # Náhodná hodnota pokladu 0 - 5000
            treasure_value: int = random.randint(0, 5000)

            # Vložření do sdílené fronty
            self.__treasure_queue.put(treasure_value)
            print(f"[Sopka] Vyvržen poklad v hodnotě {treasure_value}")