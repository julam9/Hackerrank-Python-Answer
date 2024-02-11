def bonAppetit(bill, k, b):
    total_anna = (sum(bill)-bill[k])//2
    if total_anna < b:
        return b - total_anna
    else:
        return "Bon Apetit"
    