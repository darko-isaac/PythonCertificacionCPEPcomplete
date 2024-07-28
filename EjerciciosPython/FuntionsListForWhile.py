def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    if year < 1582 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    return total_days

def day_of_week(year, month, day):
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J
    day_of_week = f % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    return days[day_of_week]

# Probando las funciones
test_dates = [(1900, 2, 28), (2000, 2, 29), (2016, 1, 1), (1987, 11, 30)]
for year, month, day in test_dates:
    print(f"Date: {year}-{month}-{day}")
    print(f"Day of the year: {day_of_year(year, month, day)}")
    print(f"Day of the week: {day_of_week(year, month, day)}\n")

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
test_months = [2, 2, 1, 11]
test_results2 = [28, 29, 31, 30]
for i in range(len(test_data)):
    yr = test_data[i]
    mo = test_months[i]
    print(yr,"-> ",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")
    result = days_in_month(yr, mo)
    if result == test_results2[i]:
        print("OK")
    else:
        print("Fallido")
