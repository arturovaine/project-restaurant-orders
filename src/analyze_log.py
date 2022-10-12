import csv
import os


def favorite_of(orders, name):
    filtered_orders = []
    for order in orders:
        if order[0] == name:
            filtered_orders.append(order[1])
    return max(set(filtered_orders), key=filtered_orders.count)
    # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list


def how_many_of(orders, name, food):
    counter = 0
    for order in orders:
        if order[0] == name and order[1] == food:
            counter += 1
    return counter


def never_ordered(orders, name):
    never_ordered = set()
    for order in orders:
        never_ordered.add(order[1])
    for order in orders:
        if order[0] == name and order[1] in never_ordered:
            never_ordered.remove(order[1])
    return never_ordered


def never_went(orders, name):
    never_went = set()
    for order in orders:
        never_went.add(order[2])
    for order in orders:
        if order[0] == name and order[2] in never_went:
            never_went.remove(order[2])
    return never_went


def verify_path(path):
    if not path.endswith("csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")


def analyze_log(path_to_file):
    verify_path(path_to_file)
    orders = list()
    with open(path_to_file, mode="r", encoding="utf-8") as file:
        registers = csv.reader(file, delimiter=",", quotechar='"')
        for row in registers:
            orders.append(row)

    maria = favorite_of(orders, "maria")
    arnaldo = how_many_of(orders, "arnaldo", "hamburguer")
    joao_never_ordered = never_ordered(orders, "joao")
    joao_never_went = never_went(orders, "joao")
    result = [
                f"{maria}\n",
                f"{arnaldo}\n",
                f"{joao_never_ordered}\n",
                f"{joao_never_went}\n",
            ]

    with open("data/mkt_campaign.txt", mode="w") as file:
        for line in result:
            file.writelines(line)


analyze_log('data/orders_1.csv')
