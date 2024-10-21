import random #used to generate the slot machines random values


MAX_LINES = 3 #Global Constant maximum lines is 3
MAX_BET = 100 #Global Constant maximum allowed bet is 100 dollars
MIN_BET = 1 #Global Constant minimum allowed bet is 1 dollar

ROWS = 3 #Global Constant number of rows
COLS = 3 #Global Constant number of columns

#Dictionary storing the symbols and values
symbolCount = {
  "A": 2,
  "B": 4,
  "C": 6,
  "D": 8
}




def getSlotMachineSpin(rows, cols, symbols):
  allSymbols = []
  for symbol, symbolCount in symbols.items():
    for _ in range(symbolCount):  # _ is same as i, unused values in python can use _
      allSymbols.append(symbol)

  columns = [] #start by defining columns list, gonna be 3 nested lists inside
  for _ in range(cols): #generate column, for every column we have, if 3 columns we run everything inside 3 times
    column = [] #column is = to an empty list
    currentSymbols = allSymbols[:] #current symbols, ones we can currently select from, are equal to a copy of all symbols
    for _ in range(rows): #loop through the number of values needed to generate, which is equal to rows we have, same as columns
      value = random.choice(currentSymbols) #random value from current symbols is stored in value
      currentSymbols.remove(value) #remove the value chosen so we dont pick it again
      column.append(value) #then add the value to our column list

    columns.append(column) #now that all loops are done , we add our column to our columns list

  return columns


def printSlotMachine(columns):
  for row in range(len(columns[0])):
    for i, column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], "|")
      else:
        print(column[row])


#collects user input, gets deposit from user 
def deposit():
  while True: #while loop, continually ask user to enter amount until given valid amount 
    amount = input("What would you like to deposit? $") # Prompt, stored in amount
    if amount.isdigit():# check if number entered is a number
      amount = int(amount)# if it is a digit then we make amount an integer data type
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")
  return amount

# function getting user input number of lines being played
def getNumberOfLines():
  while True: #while loop, continually ask user to enter lines until given valid input 
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ") # Prompt, user input stored in lines, const conv to string since displayed
    if lines.isdigit():# check if number entered is a number
      lines = int(lines)# if it is a digit then we make lines an integer data type
      if 1 <= lines <= MAX_LINES: # if lines is 1-3 perfect
        break
      else:
        print("Enter a valid number of lines.")
    else:
      print("Please enter a number.")
  return lines

# function to store user input value willing to bet
def getBet():
  while True: #while loop, continually ask user to enter amount until given valid amount 
    amount = input("What would you like to bet on each line? $") # Prompt, stored in amount
    if amount.isdigit():# check if number entered is a number
      amount = int(amount)# if it is a digit then we make amount an integer data type
      if MIN_BET <= amount <= MAX_BET: #amount must be between min and max bet, 1-100
        break
      else:
        print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.") #f string auto converts embedded values if possible
    else:
      print("Please enter a number.")
  return amount




#main function to re-run entire program 
def main():
  balance = deposit() #this is a function call stored inside balance
  lines = getNumberOfLines() #this is a function call stored inside lines
  while True:
    bet = getBet() #this is a function call stored inside bet
    totalBet = bet * lines

    if totalBet > balance:
      print(
        f"You do not have enough to bet that amount, your current balance is: ${balance}")
    else:
      break

  print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${totalBet}")

#main function call to actually run the function
main()