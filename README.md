# 📌 Sopka a Sběrači
Sopka a Sběrači je multithreadová simulace, která demonstruje použití vláken v Pythonu. Projekt simuluje sopku, která v náhodných intervalech vyvrhuje poklady s náhodnou hodnotou, a několik sběračů, kteří v různých intervalech „odpočívají“, získávají sílu a poté se pokouší sebrat poklady, jejichž hodnota nepřesáhne jejich aktuální sílu.

## 💡 Obsah projektu
### volcano.py
Obsahuje třídu Volcano, která představuje sopku – producenta, jež generuje poklady v náhodných intervalech a vkládá je do sdílené fronty.

### gatherer.py
Obsahuje třídu Gatherer, která reprezentuje sběrače – konzumenty, kteří na základě své strategie (doba odpočinku) nabírají sílu a poté se pokoušejí sebrat poklady z fronty.

## strategies.py
Obsahuje různé strategie spánku (např. fixní, náhodnou do určitého intervalu apod.), které určují dobu odpočinku sběračů.

### main.py
Hlavní spouštěcí skript, který inicializuje všechny komponenty, spouští vlákna a po uplynutí stanoveného času (2 minuty) vyhodnocuje výsledky.

### 🚀 Jak projekt funguje
**Sopka (Volcano)**

Běží jako vlastní vlákno a v náhodných intervalech (0–5 sekund) generuje poklady s náhodnou hodnotou (0–5000).
Poklady se ukládají do sdílené fronty (Queue).
Sběrači (Gatherers)

Každý sběrač spí podle své strategie (např. fixní nebo náhodnou dobu), během které „nabere sílu“ (síla = doba spánku v ms).
Po probuzení se pokouší sebrat z fronty libovolný počet poklad, jejichž hodnota je menší nebo rovna jeho aktuální síle.
Při úspěšném sebrání se hodnota pokladu přičítá k jeho celkovému skóre.
Simulace a vyhodnocení

Aplikace běží 2 minuty.
Po skončení se zastaví všechna vlákna a vyhodnotí se, který sběrač nashromáždil nejvyšší hodnotu pokladů.

