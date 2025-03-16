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

    # Vrací všechny sebrané poklady
    def get_total_collected(self) -> int:
        return self.__total_collected

    # Vrací jmnéno sběrače
    def get_name(self) -> str:
        return self.__name

    # Hlavní běh vlákna
    def run(self) -> None:

        while not self.__stop_event.is_set():
            sleep_time: float = self.__strategy_function()
            time.sleep(sleep_time)

            strength: int = int(sleep_time * 1000)

            taken_value = self.__try_take_treasure(strength)
            if taken_value > 0:
                self.__total_collected += taken_value
                print(f"[{self.__name}] Sebral poklad {taken_value} (síla {strength}) - "f"Celkem: {self.__total_collected}")

        print(f"[{self.__name}] Končím. Celkem sebral: {self.__total_collected}")

    # Funkce, která se snaží nasbírat co nejvíce pokladu
    def __try_take_treasure(self, strength: int) -> int:
        temp_list = []
        total_taken_value = 0
        remaining_strength = strength

        # Vytáhne z fronty, vše co tam je
        while not self.__treasure_queue.empty():
            val = self.__treasure_queue.get()

            # Jestli se poklad vejde do zbytku síly tak jej přičtu
            if val <= remaining_strength:
                total_taken_value += val
                remaining_strength -= val
            else:
                # Jestli se poklad do zbytku síly nevejde tak jej vrátím zpět
                temp_list.append(val)

        # Vraťme zbývající poklady zpět do fronty
        for v in temp_list:
            self.__treasure_queue.put(v)

        return total_taken_value