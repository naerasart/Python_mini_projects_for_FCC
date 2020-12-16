class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = (list())

  def deposit(self, amount, description = True):
    if description==True:
      self.ledger.append({"amount":(amount), "description": ''})
    elif description !=True:
      self.ledger.append({"amount":(amount), "description": (description)})
    
  def withdraw(self, amount, description = True):
    if self.check_funds(amount) ==True:
      if description==True:
        self.ledger.append({"amount":(-amount), "description": ''})
        return True
      else:
        self.ledger.append({"amount":(-amount), "description": (description)})      
        return True
    elif self.check_funds(amount) !=True:
      return False  

  def get_balance(self):
    total =int()
    for item in self.ledger:
      total += item['amount']
    return total

  def transfer(self, amount, budget_category):
     
    if self.check_funds(amount)==True:
       self.ledger.append({"amount":-(amount), "description": f'Transfer to {budget_category.name}'})
       budget_category.ledger.append({"amount":(amount), "description": f'Transfer from {self.name}'})
       return True
    elif self.check_funds(amount)!=True:
       return False

  def check_funds(self, amount):
    if amount <= self.get_balance():
      return True
    elif amount > self.get_balance():
      return False

  def __str__(self):
    
    title= ("*"*(int( (30 - (len(self.name))) / 2 ))) + self.name + ("*"*(int( (30 - (len(self.name))) / 2 )))

    for items in self.ledger:
      itemdescript=str
      if (23 - len(items['description'])) > 0:
        itemdescript = items['description'] + (" "*(23 - len(items['description'])))  
      elif (23 - len(items['description'])) == 0:
        itemdescript = items['description']  
      elif (23 - len(items['description'])) < 0:
        itemdescript = items['description'][:23]  
      title += "\n" + itemdescript

     
        
      if(7 - len(("{:.2f}".format(items['amount']))))==0:
         title += ("{:.2f}".format(items['amount']))
      elif (7 - len(("{:.2f}".format(items['amount'])))) != 0:
         title += (" "*(7 - len(("{:.2f}".format(items['amount']))))) + ("{:.2f}".format(items['amount'])) 
    title += "\nTotal: " + "{:.2f}".format(self.get_balance()) 
    
    return title


#second half of the problem: Creating the graph:
def create_spend_chart(itemnames):
  item, spent, percentage = list(),list(), list()   

  for x in itemnames:
    total = int()
    for y in x.ledger:
      if y['amount'] < 0:
        total -= y['amount']
      elif y['amount'] == 0:
        total += 0
      elif y['amount'] > 0:
        total += 0
    spent.append(round(total, 2))
    item.append(x.name)

  for price in spent:
    percentage.append (price / sum(spent)*100)

  result = "Percentage spent by category\n"

  percentages = reversed(range(0, 110, 10))

  for num  in  percentages:
    result += str(num).rjust(3) + "| "
    for number in percentage:
      if number >= num:
        result += "o  "
      elif number < num:
        result += (" "*3)
    result += "\n"

  result += "    ----" + ("---" * (len(item) - 1))
  result += "\n     "

  lengthiestname = int()

  for name in item:
    if lengthiestname < len(name):
      lengthiestname = len(name)

  for i in range(lengthiestname):
    for name in item:
      if len(name) > i:
        result += name[i] + (" "*2)
      elif len(name) < i:
        result += (" "*3)
      elif len(name) == i:
        result += (" "*3)
      
    if i < lengthiestname-1:
      result += "\n"+(" "*5)
    elif i > lengthiestname-1:
      result += 0

    

  return(result)
 #Reference:https://repl.it/@Flak_A239/budget-app?lite=true#budget.py