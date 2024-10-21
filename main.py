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
#symbol multiplier
symbolValue = {
  "A": 5,
  "B": 4,
  "C": 3,
  "D": 2
}


def checkWinnings(columns, lines, bet, values):
  winnings = 0
  winningLines = []
  for line in range(lines):#every line in the lines, looping through every row
    symbol = columns[0][line] #the symbol we wanna check is whatever symbol is in the first column of the current row
    for column in columns: #now loop through every column and check for that symbol
      symbolToCheck = column[line] #go to the column and we say, the symbol to check is equal to the column at the current row
      if symbol != symbolToCheck: #then check if the symbols are not the same
        break #if not the same we break and go check next line
    else:
      winnings += values[symbol] * bet #if we finish for loop without breaking out then the user won
      winningLines.append(lines + 1)
  
  return winnings, winningLines



#function produces the actual slot spin via random
def getSlotMachineSpin(rows, cols, symbols): #function takes rows, columns, and symbols
  allSymbols = [] #list containing all symbols we can select from
  for symbol, symbolCount in symbols.items(): #iterating through dict, 
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

#loop through every row, for every row loop through every column, for every column print current row we are on
def printSlotMachine(columns):
  for row in range(len(columns[0])): #transposing, get length of columns assuming we always had atleast 1 column
    for i, column in enumerate(columns): #loop through all columns and only print first value
      if i != len(columns) - 1:
        print(column[row], end=" | ") #using \n would do this for every column, end="" only affects each row like we want
      else:
        print(column[row], end="") #if its the last one dont print pipe

    print() #brings us down to next line, since its a newline by default

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


def spin(balance):
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

  slots = getSlotMachineSpin(ROWS, COLS, symbolCount)
  printSlotMachine(slots)
  winnings, winningLines = checkWinnings(slots, lines, bet, symbolValue)
  print(f"You won ${winnings}.")
  print(f"You won on lines:", *winningLines)

  return winnings - totalBet

#main function to re-run entire program 
def main():
  balance = deposit() #this is a function call stored inside balance
  while True:
    print(f"Current balance is: ${balance}")
    answer = input("Press enter to play (q to quit).")
    if answer == "q":
      break
    balance += spin(balance)

  print(f"You left with ${balance}")

#main function call to actually run the function
main()