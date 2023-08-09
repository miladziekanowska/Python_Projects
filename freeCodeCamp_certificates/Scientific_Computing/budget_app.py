class Category:
      def __init__(self, name: str):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.spending = 0

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, 
                            "description": description})
        self.balance += amount
        self.spending += amount

    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": - amount, 
                                "description": description})
            self.balance -= amount 
            self.spending += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount: float, dest_cat):
        if not self.withdraw(amount, f"Transfered to {dest_cat}"):
            return False

        dest_cat.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount: float):
        return self.balance >= amount

    def spendings(self):
        return - self.spending

    def __str__(self):
        items_list = [self.name.center(30, "*")]
        for item in self.ledger:
            description = item["description"][0:23]
            items_list.append("{:<23}{:>7.2f}".format(description, item["amount"]))

            items_list.append(f"Total: {self.balance}")
            return "\n".join(items_list)





def create_spend_chart(categories):
    spendings = [category.spendings() for category in categories]
    total_amount = sum(spendings)
    percentages = [spending * 100 / total_amount for spending in spendings]
    chart_print_list = ["Percentage spent by category"]
    for i in range(0,11):
        decimal = 10 * (10 - i)
        s = "{:>3}| ".format(decimal)
        for percentage in percentages:
            if percentage >= decimal:
                s += "o  "
            else:
                s += "   "
        chart_print_list.append(s)  
    padding = "    "
    chart_print_list.append(padding + "-" * 3 * len(spendings) + "-")

    category_names = [category.name for category in categories]
    n = max(map(len, category_names))
    for i in range(0, n):
        s = padding
        for category in category_names:
              s += " "
              s += category[i] if len(category) > i else " "
              s += " " 
        chart_print_list.append(s + " ")

    return "\n".join(chart_print_list)