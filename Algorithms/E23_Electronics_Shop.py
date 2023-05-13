def getMoneySpent(keyboards, drives, b):
    max_cost = 0
    for k in keyboards:
        for d in drives:
            if k+d > max_cost and k+d <= b:
                max_cost = k+d
    if max_cost > 0:
        return max_cost
    else:
        return -1
    
def get_money_spent(keyboards,drives,b):
    
    keyboards.sort(reverse=True)
    drives.sort(reverse=True)
    max = keyboards[0]+drives[0]
    
