class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'

            total += item['amount']

        output = title + items + "Total: " + str(total)
        #print(output)
        return output

    def deposit(self, amount, description=""):
        #print('Depositing: ', amount)
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        #print(f"{'Withdrawing:' [0:7]:7}" + f"{amount:>30.3f}")
        balanceCheck = self.check_funds(amount)
        if balanceCheck == True:
            self.ledger.append({
                "amount": amount * -1,
                "description": description
            })
            return True
        else:
            return False

    def get_balance(self):
        total = 0
        for entry in self.ledger:
            total = total + float(entry["amount"])

        return (round(total, 2))

    def transfer(self, amount, category):
        balanceCheck = self.check_funds(amount)
        if balanceCheck == True:
            self.ledger.append({
                "amount": amount * -1,
                "description": "Transfer to " + category.name
            })
            category.ledger.append({
                "amount": amount,
                "description": "Transfer from " + self.name
            })
            return True
        else:
            return False

    def check_funds(self, amount):
        currentBalance = self.get_balance()
        #print('currentBal: ', currentBalance)
        if amount > self.get_balance():
            return False
        else:
            return True


def create_spend_chart(categories):
    items = []
    withdrawals = []
    expenses = []
    output = ""
    graphRow = ""
    lineOutput = ""
    underLine = ""
    xLegend = []
    letterList = []
    xLegendTitlesList = []
    xLegendTitlesStr = ""

    for item in categories:
        items.append("self." + item.name.lower())
        withdrawals.append(item.ledger)
    j = 0
    for i in range(len(withdrawals)):
        k = 1
        expenses.append(withdrawals[j][k]["amount"] * -1)
        k += 1
        j += 1

    totalExp = sum(expenses)

    proportionOfExp = list()
    for expense in expenses:
        proportionOfExp.append((expense / totalExp * 100))

    graphDataPercent = list()
    m = 0
    for item in items:
        graphDataPercent.append((item, proportionOfExp[m]))
        m += 1

    gdpLength = len(graphDataPercent)
    #print('gdpLength', gdpLength)

    yAxisValues = list()
    y = 100
    for val in range(y, -1, -10):
        yAxisValues.append(val)

    xAxisValues = list()
    x = 0
    for val in range(x, gdpLength, 1):
        xAxisValues.append(val)

    #print('yAxisVals', yAxisValues[0])
    #print('xAxisVals', xAxisValues)

    for yAxisVal in yAxisValues:
        if yAxisVal == 100:
            graphRow = "" + str(yAxisVal) + "|"
        elif yAxisVal > 9:
            graphRow = " " + str(yAxisVal) + "|"
        else:
            graphRow = "  " + str(yAxisVal) + "|"
        #print('yAxisVals', yAxisVal)

        for catVal in proportionOfExp:
            #print('valPrint', catVal)
            if catVal <= yAxisVal:
                graphRow = graphRow + "   "
            else:
                graphRow = graphRow + " o "

        lineOutput = lineOutput + graphRow + " \n"
        #print('lineOutput', lineOutput)
    #print('spacedLine', spacedLine)

    for catVal in items:
        underLine = underLine + "---"
    
    underLine = "    " + underLine + "-"

    for item in items:
        xLegend.append((item.split(".")[1]).capitalize())
        #print('first letter capped categs', xLegend)

    # >> find longest categ
    longestCateg = max(xLegend, key=len)
    longestCategLen = len(longestCateg)
    #print('longestCategLen =', longestCategLen)

    for categ in xLegend:
        if len(categ) < longestCategLen:
            trailingSpace = longestCategLen - len(categ)
            for count in range(0, trailingSpace, 1):
                categ = categ + " "

        for letter in categ:
            #print('letter', letter)
            letterList.append(letter)

    #print('letterList', letterList)
    #print('longestCategLen =', longestCategLen)

    def GetNthLetters(text, step, n):
        n = n + 1
        xLegendTitlesList.append(text[n::step])

    m = -1
    for count in longestCateg:
        GetNthLetters(letterList, longestCategLen, m)
        m = m + 1

    #print('xLegendTitlesList', xLegendTitlesList)

    xLegendTitlesStr = "\n     " + "  \n     ".join(
        list(map('  '.join, xLegendTitlesList)))

    #print(xLegendTitlesStr)

    output = 'Percentage spent by category\n' + lineOutput + underLine + xLegendTitlesStr + "  "
    return output
