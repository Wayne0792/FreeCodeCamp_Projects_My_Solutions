class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output = self.name.center(30, '*') +"\n"
        for l in self.ledger:
            output += l["description"][:23]
            output += ("%.2f"%(l["amount"]))[:7].rjust(30-len(l["description"][:23]), ' ')+"\n"
        output += "Total: "+("%.2f"%self.get_balance())
        return output

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for l in self.ledger:
            balance += l["amount"]
        return balance

    def transfer(self, amount, budget):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+budget.name)
            budget.deposit(amount, "Transfer from "+self.name)
            return True
        return False
    
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

def create_spend_chart(categories):
    total_spent = 0
    spents = []
    for c in categories:
        c_spent = 0
        for l in c.ledger:
            if l["amount"] < 0:
                c_spent += abs(l["amount"])
        total_spent += c_spent
        spents.append(c_spent)
    
    spents = [int(s/total_spent*10)*10 for s in spents]

    #title
    output = "Percentage spent by category\n"
    #chart body
    for p in range(100, -10, -10):
        output += str(p).rjust(3) + "| "
        for i in range(len(categories)):
            if spents[i] >= p:
                output += "o  "
            else:
                output += "   "
        output += "\n"
    #chart base
    output += "    " + (3*len(categories)+1)*"-" + "\n"
    #labels
    max_len_name = max([len(c.name) for c in categories])
    for i in range(max_len_name):
        output += "     "
        for c in categories:
            if len(c.name) > i:
                output += c.name[i] + "  "
            else:
                output += "   "
        if i < max_len_name - 1:
          output += "\n"

    return output