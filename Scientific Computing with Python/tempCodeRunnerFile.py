class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category
    
    def __str__(self):
        title = self.category.center(30, '*')
        string = title + '\n'
        count = 0
        for _ in self.ledger:
            if len(self.ledger[count]['description']) <= 23:
                shift = 30 - len(self.ledger[count]['description'])
                shift = shift - len("{:.2f}".format(self.ledger[count]['amount']))
                amount_shift = " " * shift
            else:
                amount_shift = " "
            string = string + (self.ledger[count]['description'][:23]) + amount_shift + "{:.2f}".format(self.ledger[count]['amount']) + '\n'
            count+=1
        string = string + "Total: " + "{:.2f}".format(self.get_balance())
        return string

    def deposit(self, amount, description=""):
        object = {'amount': amount, 'description': description}
        self.ledger.append(object)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            amount = -1 * amount
            object = {'amount': amount, 'description': description}
            self.ledger.append(object)
            return True
        else:
            return False
            
    def get_balance(self):
        count = 0
        balance = 0
        for _ in self.ledger:
            balance = balance + self.ledger[count]['amount']
            count+=1
        return balance
    
    def transfer(self, amount, des_Category):
        if self.check_funds(amount) == False:
            print(f"Not enough funds in account. {self.category} has {self.get_balance()}.")
            return False
        else:
            self.withdraw(amount, f'Transfer to {des_Category.category}')
            des_Category.deposit(amount, f'Transfer from {self.category}')
            return True
    
    def check_funds(self, amount):
        balance = self.get_balance()
        if amount <= balance:
            return True
        else:
            return False



def create_spend_chart(categories):
    # Find withdrawls from categories
    spend_Array = []
    percentage_Array = []
    balance = 0
    for i in categories:
        count = 0
        while count < len(i.ledger):
            if i.ledger[count]['amount'] < 0:
                balance = balance + i.ledger[count]['amount']
            count+=1
        balance = round(balance, 2) * -1
        spend_Array.append(balance)
        balance = 0
    total = sum(spend_Array)
    for i in spend_Array:
        percentage = i/total
        percentage = int(percentage * 100) // 10 * 10
        percentage_Array.append(percentage)


    # Place o on graph
    final = ""
    number = 100
    while number >= 0:
        # if 0
        if number == 0:
            final = final + "  " + str(number) + "| "
            for i in percentage_Array:
                if i >= number:
                    final = final + "o  "
        # if 100
        elif number < 100:
            final = final + " " + str(number) + "| "
            for i in percentage_Array:
                if i >= number:
                    final = final + "o  "
        # everything else    
        else:
            final = final + str(number) + "| "
            for i in percentage_Array:
                if i >= number:
                    final = final + "o  "
        final = final.rstrip()
        final = final + "\n"
        number-=10
    
    # bar calculation
    bar = "-" * (len(categories) * 3)
    final = final + "    -" + bar + "\n"

    # prepping for text
    final = final + "     "
    str_max = ""
    
    # finding max string length
    for i in categories:
        if len(i.category) > len(str_max):
            str_max = i.category
    max = len(str_max)
    count = 0
    while count <= max:
        for i in categories:
            if count < len(i.category):
                word = str(i.category)
                final = final + word[count] + "  "
            else:
                final = final + "   "
        final = final.rstrip()
        final = final + "\n" + "     "
        count +=1

    return final

def main():
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    clothing.deposit(100, "deposit")
    clothing.withdraw(30, "Balenciaga")
    auto = Category("Auto")
    auto.deposit(1000, "deposit")
    auto.withdraw(60, "tires")
    print(food)
    print(clothing)
    list = [food, clothing, auto]
    chart = create_spend_chart(list)
    print(chart)

main()




        
