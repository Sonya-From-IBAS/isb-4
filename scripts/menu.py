import argparse
import time
import logging

from scripts.card_info import CardInfo
from scripts.luhn_algorithm import luhn_algorithm
from scripts.card_number import create_card_number
from scripts.cores_time import Stat

logging.getLogger().setLevel(logging.INFO)

def menu() -> None:
    """
    Func for working with user
    """
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument(
        "path", type=str, help="Путь к json файлу с настройками")
    group.add_argument("-cn", "--cardnumber",
                       help="Запускает скрипт нахождения номера карты")
    group.add_argument("-ct", "--corestime",
                       help="Запускает скрипт для замера времени")
    group.add_argument("-la", "--luhnalg",
                       help="Запускает алгоритм Луна")
    args = parser.parse_args()
    if args.cardnumber:
        card_info = CardInfo(args.path)
        number = create_card_number(
            card_info.hash_card, card_info.last_num, card_info.bins_card, 8)
        print(f"card number is {number}")
        card_info.card_number_serealization(number, args.path)
    elif args.corestime:
        card_info = CardInfo(args.path)
        stat = Stat(args.path)
        for i in range(1, 9):
            start = time.perf_counter()
            create_card_number(card_info.hash_card,
                               card_info.last_num, card_info.bins_card, i)
            end = time.perf_counter()
            stat.time_serialization(i, end-start)
        stat.save_fig()
    elif args.luhnalg:
        card_info = CardInfo(args.path)
        number = card_info.card_number_deserealization(args.path)
        print(luhn_algorithm(number))