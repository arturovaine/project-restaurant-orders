class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        filtered_orders = []
        for order in self.orders:
            if order[0] == customer:
                filtered_orders.append(order[1])
        return max(set(filtered_orders), key=filtered_orders.count)
        # https://stackoverflow.com/questions/1518522/find-the-most-common-element-in-a-list

    def get_never_ordered_per_customer(self, customer):
        never_ordered = set()
        for order in self.orders:
            never_ordered.add(order[1])
        for order in self.orders:
            if order[0] == customer and order[1] in never_ordered:
                never_ordered.remove(order[1])
        return never_ordered

    def get_days_never_visited_per_customer(self, customer):
        never_went = set()
        for order in self.orders:
            never_went.add(order[2])
        for order in self.orders:
            if order[0] == customer and order[2] in never_went:
                never_went.remove(order[2])
        return never_went

    def get_busiest_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return max(set(days), key=days.count)

    def get_least_busy_day(self):
        days = []
        for order in self.orders:
            days.append(order[2])
        return min(set(days), key=days.count)
