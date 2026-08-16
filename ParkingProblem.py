DAYS = 31
DAYS_IN_A_WEEK = 7
weeks = DAYS // 7
extra = DAYS % 7
WEEK_COST = 100
EXTRA_COST = 20

print(int((WEEK_COST * weeks) + (EXTRA_COST * extra)))