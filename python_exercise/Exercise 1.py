#John wants to know his average expenses for each semester. Using a for loop, calculate John’s average expenses for the first semester (January to June) and the second semester (July to December).
monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61,
                    3890.45]
first_monthly_spending = 0
second_monthly_spending = 0

for index, cost in enumerate(monthly_spending):
    if index < 6:
        first_monthly_spending += cost
    else:
        second_monthly_spending += cost

print("In the first semester John has spent ", first_monthly_spending/6)
print("In the second semester John has spent ", second_monthly_spending/6)

