import time
import threading
from queue import Queue

from volcano import Volcano
from gatherer import Gatherer
import strategies


def main() -> None:

    # Aplikace běží po dobu 120 sekund
    runtime: int = 120

    # Sdílená pronta, kam sopka vrhá poklady a sběrači je odebírají
    treasure_queue: Queue = Queue()

    # Událost pro ukončení všech vláken
    stop_event = threading.Event()

    # Sopka
    volcano = Volcano(treasure_queue, stop_event)

    # Sběrači a jejích strategie
    gatherer1 = Gatherer("Radek",strategies.strategy_a ,treasure_queue, stop_event)
    gatherer2 = Gatherer("Tomáš",strategies.strategy_b ,treasure_queue, stop_event)
    gatherer3 = Gatherer("Danek",strategies.strategy_c ,treasure_queue, stop_event)

    # Spuštění všech vláken
    volcano.start()
    gatherer1.start()
    gatherer2.start()
    gatherer3.start()

    # Necháme hlavní vlákno spát RUNTIME
    start_time: float = time.time()
    while (time.time() - start_time) < runtime:
        time.sleep(0.1)

    # Když uběhne čas nastavíme stop_event, aby se ukončily všechny vlákna
    stop_event.set()

    # Požádáme o ukončení všechny vlákna
    volcano.join()
    gatherer1.join()
    gatherer2.join()
    gatherer3.join()

    # Vyhodnocení výsledků
    results = [
        (gatherer1.get_name(), gatherer1.get_total_collected()),
        (gatherer2.get_name(), gatherer2.get_total_collected()),
        (gatherer3.get_name(), gatherer3.get_total_collected()),
    ]

    # Sřadíme dle celkové hodnoty (sestupně)0
    results.sort(key=lambda x: x[1], reverse=True)

    print("\n|--- KONEC BĚHU ---|")
    print("Pořadí sběračů dle celkové hodnoty sebraných pokladů:")
    for name, value in results:
        print(f"{name}: {value} bodů")

    print(f"\nVítězem je: {results[0][0]} s {results[0][1]} body!")


if __name__ == "__main__":
    main()