# MasterSherkulov
# MasterSherkulov.github.io
# 06.06.2019 Uzbekistan

def credit_calc(amountCredit,percent,month):
    lastAmountCredit = amountCredit

    persentTotal = 0 
    result = []
    for row in range(month):
        tbodyTr = ""
        calc2 = amountCredit / month
        calc3 = lastAmountCredit * percent / 12 / 100
        lastAmountCredit -= calc2
        calc1 = (calc3 + calc2)
        persentTotal += calc3
        result.append({
            "total": round(calc1,2),
            "debit": round( calc2,2),
            "percent": round(calc3,2),
            "lastamount": round(lastAmountCredit,2)
        })
        #print(row + 1,"\t",  round(calc1,2),"\t",round( calc2,2),"\t", round(calc3,2) , "\t",  round(lastAmountCredit,2))
    return result

amountCredit = 10000000
percent = 19
month = 12

credit = credit_calc(amountCredit, percent, month)

for row in credit:
    print(row['total'], '\t' , row['debit'], '\t' , row['percent'], '\t' , row['lastamount'])
