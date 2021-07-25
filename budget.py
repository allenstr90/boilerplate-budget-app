class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.founds = 0

    def deposit(self, amount, description=''):
        self.founds += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.founds -= amount
            return True
        return False

    def get_balance(self):
        return self.founds

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if self.founds < amount:
            return False
        return True

    def __str__(self):
        result = self.name.center(30, '*')
        for operation in self.ledger:
            result += f'\n{operation["description"][0:23]:23} {operation["amount"]:.2f}'
        result += f'\nTotal: {self.founds}'
        return result

    def total_withdraws(self):
        withdraws = round(-sum([item["amount"]
                                for item in self.ledger if item["amount"] < 0]), 2)
        return withdraws


def create_spend_chart(categories):
    result = 'Percentage spent by category'
    data = []
    total_withdraws = sum(item.total_withdraws() for item in categories)
    for cat in categories:
        data.append({'name': cat.name, 'percent': (cat.total_withdraws() / total_withdraws) * 100})
    for x in range(100, -10, -10):
        row = ' '
        for bar in data:
            if bar['percent'] > x:
                row += 'o  '
            else:
                row += '   '
        result += f'\n{x:3}|{row}'
    result += '\n    -'.ljust(len(data) * 3 + 6, '-')
    max_len = len(data[0]['name'])
    for name in data:
        max_len = max(max_len, len(name['name']))
    for y in range(0, max_len):
        row = '\n     '
        for dat in data:
            name = dat['name']
            if len(name) > y:
                row += f'{name[y]}  '
            else:
                row += '   '
        result += row
    return result
