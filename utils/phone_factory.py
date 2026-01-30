import random

def generate_phone() -> str:
    """
    Генерирует новый номер для каждого прогона.
    Формат: 79XXXXXXXX
    """
    return "79" + "".join(str(random.randint(0, 9)) for _ in range(9))
