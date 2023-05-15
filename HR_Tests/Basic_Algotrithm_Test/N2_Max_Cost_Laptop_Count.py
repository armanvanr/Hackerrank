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
    return max(total_cost)

# print(maxCost([2,5,3,11,1],["legal","illegal","legal","illegal","legal"],2))
print(maxCost([0,3,2,3,4],["legal","legal","illegal","legal","legal"],3))

# Problem Description:
# A company manufactures a fixed number of laptops every day.
# However, if some defect is encountered during the testing of a laptop,
# it is labeled as "illegal" and is not counted in the laptop count of the day.
# Given the cost to manufacture each laptop, its label as "illegal" or "legal",
# and the number of legal laptops to be manufactured each day,
# find the maximum cost incurred by the company in a single day in manufacturing all the laptops.

# Note that if a laptop is labeled as illegal, its manufacturing cost is still incurred by the company,
# even though it is not included in the laptop count.
# Also, days are only taken into when the daily laptop count has been completely met.
# If there are no such days, the answer is 0.

# For example,
# let's say there are n = 5 laptops, where cost = [2,5, 3, 11, 1].
# The labels for these laptops are labels = ["legal", "illegal", "legal", "illegal", "legal").
#     Finally, the daily Count = 2, which means that the company needs to manufacture 2 legal laptops each day.
# The queue of laptops can be more easily viewed as follows:

# cost 2, "legal" 
# cost 5, "illegal" 
# cost 3, "legal" 
# cost 11, "illegal" 
# cost 1, "legal"

# On the first day, the first three laptops are manufactured in order to reach the daily count of 2 legal laptops.
# The cost incurred on this day is 2 + 5 + 3 = 10.
# On the second day, the fourth and fifth laptops are manufactured,
# but because only one of them is legal, the daily count isn't met, so that day is not taken into consideration.
# Therefore, the maximum cost incurred on a single day is 10.


# My Algorithm:
# Since the laptops and labels are always in pairs, so I loop over them using index-based loop.
# To get an easier loop control, I use while-loop whose conditional logic is more flexible than for-loop.

# I will check the laptop one by one, each check will add up the "cost count" incrementally (line10).
# Only if there is any laptop has label "legal", the "legal" counter will add up +1 (line9).
# Repeat it until the legal counter equals to DailyCount.

# I need to add a guard clause (line12), since at the last checking day the number of legals might be below DailyCount.
# So, only if "legal" counter is exactly the same as DailyCount, append the dailycost into the final list (total_cost).
# If there are still laptops left, then reset the "legal" counter and "dailycost" counter, repeat the checking process.

# The final list (line3) must have at least 0, in case none of the laptops meet the checking criteria.
# Return the maximum value of the final list.