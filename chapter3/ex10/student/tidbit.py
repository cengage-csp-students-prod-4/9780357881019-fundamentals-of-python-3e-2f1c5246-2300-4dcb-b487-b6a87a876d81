"""
Program: Credit Plan Calculator
9-18-2026
Michael Guillen

ask user for 'prchPrc', float
set 'downPymnt' to 0.10
set 'intRate' to 0.12
set 'curMnth' to 1
set 'mnthPrcRate' to 0.05
set 'bal' to 'prchPrc' - ('prchPrc'*'downPymnt')
set 'prcPerMnth' to 'prchPrc'*'mnthPrcRate'
set 'numMnths' to 'bal'/'prcPerMnth'

print header

use a for loop to calculate the:
    starting balance, interest, principal, total payment, and the end balance
    print each value, formatted
    break when balance reaches 0
"""

prchPrc = float(input("Enter the purchase price: "))
downPymnt = 0.10
intRate = 0.12
mnthPrcRate = 0.05
bal = prchPrc - (prchPrc * downPymnt)
prcPerMnth = prchPrc * mnthPrcRate
numMnths = round(bal / prcPerMnth)

print(
    f"{'|Month|':8s}"
    f"{'|Starting Balance|':19s}"
    f"{'|Interest to Pay|':18s}"
    f"{'|Principal to Pay|':19s}"
    f"{'|Payment|':10s}"
    f"{'|Ending Balance|':17s}"
)

for curMnth in range(1, numMnths+1):
    if curMnth == numMnths:
        intrst = 0.00
        prncplPay = bal
        endPay = 0.00
    else:
        intrst = bal * (intRate/12)
        prncplPay = prcPerMnth - intrst
        endPay = bal - prcPerMnth

    print(
        f"{curMnth:4d}"
        f"{bal:16.2f}"
        f"{intrst:18.2f}"
        f"{prncplPay:18.2f}"
        f"{prcPerMnth:15.2f}"
        f"{endPay:14.2f}"
    )
    bal = endPay
