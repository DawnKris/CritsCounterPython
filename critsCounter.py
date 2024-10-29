import random

# Пример использования
crit_chance_percent = 60  # крит шанс в процентах
hits_number = 10  # количество ударов
min_crit_hits = 9   # минимальное количество критов для убийства босса

simulations_count = 10000 # уменьшение приведет к ускорению выполнения, но снизит точность результатов

def simulate_dungeon_runs(crit_chance_percent, hits_number, min_crit_hits, simulations_count):
    # Переводим вероятность в доли (например, 60% -> 0.6)
    crit_chance = crit_chance_percent / 100.0
    total_runs = 0

    for number_of_current_simulations in range(simulations_count):
        runs = 0
        while True:
            runs += 1
            crit_hits = sum(1 for _ in range(hits_number) if random.random() < crit_chance)
            if crit_hits >= min_crit_hits:
                break
        total_runs += runs
        # Использовать для вывода промежуточных результатов. Сначала ознакомьтесь с P.S.S в статье
        #print(f"Среднее количество на данный момент: {round(total_runs / (number_of_current_simulations + 1), 3) }")

    # Среднее количество заходов
    average_runs = total_runs / simulations_count
    return average_runs

average_runs = simulate_dungeon_runs(crit_chance_percent, hits_number, min_crit_hits, simulations_count)
print(f"Среднее количество заходов в данж для выполнения условия: {average_runs}")
