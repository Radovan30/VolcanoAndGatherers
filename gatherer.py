import time
import threading
from queue import Queue
from typing import Callable

class Gatherer(threading.Thread):

    def __init__(
            self,
            name: str,
            strategy_function: Callable[[], float],
            treasure_queue: Queue,
            stop_event: threading.Event,
            ) -> None:

        super().__init__()
        self.__name: str = name
        self.__strategy_function: Callable[[], float] = strategy_function
        self.__treasure_queue: Queue = treasure_queue
        self.__stop_event: threading.Event = stop_event

        self.__total_collected: int = 0

    def get_total_collected(self) -> int:
        return self.__total_collected

    def get_name(self) -> str:
        return self.__name

    def run(self) -> None:

        while not self.__stop_event.is_set():
            sleep_time: float = self.__strategy_function()
            time.sleep(sleep_time)

            strength: int = int(sleep_time * 1000)

            taken_value = self.__try_take_treasure(strength)
            if taken_value is not None:
                self.__total_collected += taken_value
                print(f"[{self.__name}] Sebral poklad {taken_value} (síla {strength}) - "f"Celkem: {self.__total_collected}")

        print(f"[{self.__name}] Končím. Celkem sebral: {self.__total_collected}")

    def __try_take_treasure(self, strength: int) -> int:
        temp_list = []
        taken_value = None
        found = False

        while not self.__treasure_queue.empty():
            val = self.__treasure_queue.get()
            if not found and val <= strength:
                taken_value = val
                found = True
            else:
                temp_list.append(val)

        # Vraťme zbývající poklady zpět do fronty
        for v in temp_list:
            self.__treasure_queue.put(v)

        return taken_value