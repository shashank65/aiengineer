print("python")

def odd_even(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


def month_name(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return months.get(month, "Invalid month")