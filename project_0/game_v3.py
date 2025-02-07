from game_v2 import score_game


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Метод бинарного поиска
    count = 0
    low, high = 1, 100 # Диапазон поиска

    while True:
        count += 1
        predict_number = (low + high) // 2 # Делим диапазон пополам

        if predict_number == number:
            break
        elif predict_number > number:
            high = predict_number - 1 # Двигаем верхнюю границу
        else:
            low = predict_number + 1 # Двигаем нижнюю границу
    # Ваш код заканчивается здесь

    return count 


print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3) 