def maxCost(cost, labels, dailyCount):
    i = 0
    total_cost = [0]
    while i < len(labels):
        daily_cost = 0
        legals = 0
        while legals < dailyCount and i < len(labels):
            if labels[i] == "legal":
                legals+=1
            daily_cost+=cost[i]
            i+=1
        if legals == dailyCount:
            total_cost.append(daily_cost)
    return total_cost

# print(maxCost([2,5,3,11,1],["legal","illegal","legal","illegal","legal"],2))
print(maxCost([0,3,2,3,4],["legal","legal","illegal","legal","legal"],1))