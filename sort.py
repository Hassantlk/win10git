incomes = {
    "apple": 5000,
    "orange": 6000,
    "bannana": 4000
}

def by_value(item):
    return item[1]

for k, v in sorted(incomes.items(), key=by_value):
    print(k, "===>", v)