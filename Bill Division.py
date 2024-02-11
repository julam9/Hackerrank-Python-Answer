def bonAppetit(bill, k, b):
    total_anna = (sum(bill)-bill[k])//2
    if total_anna > b:
        return total_anna - b 
    else:
        return "Bon Apetit"
    