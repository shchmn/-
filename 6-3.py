class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.sername = s
        self.position = p
        self._income = {"wage": w, "bonus": b}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.sername}"

    def get_total_income(self):
        return f"{sum(self._income.values())}"


w = Position("Feride", "Sh", "Doctor", 21700, 20000)
print(w.position)
print(w.get_full_name())
print(w.get_total_income())
