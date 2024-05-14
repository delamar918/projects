import emoji

def main():
    budget = get_budget()
    total_budget = budget[0] + budget[1] + budget[2] + budget[3]
    expenses = get_expense()
    total_exp = expenses[0] + expenses[1] + expenses[2] + expenses[3]
    total_remaining = total_budget - total_exp
    report_format = input("Do you want to see an itemized summary of your expenses? (y/n) ").lower()
    if report_format == "y":
        rem = []
        rem_house = budget[0]-expenses[0]
        rem.append(rem_house)
        rem_util = budget[1]-expenses[1]
        rem.append(rem_util)
        rem_food = budget[2]-expenses[2]
        rem.append(rem_food)
        rem_misc = budget[3]-expenses[3]
        rem.append(rem_misc)

        sorted_rem = itemize_it(rem)

        for a in sorted_rem:
            if sorted_rem[a] < 0:
                abs_sr = abs(sorted_rem[a])
                print(emoji.emojize(f"You have spent ${abs_sr} over your {a} budget :prohibited::credit_card::prohibited:"))
            elif sorted_rem[a] > 0:
                print(emoji.emojize(f"You are ${sorted_rem[a]} under your {a} budget. Good job! :party_popper:"))
            elif sorted_rem[a] == 0:
                print(emoji.emojize(f"You are exactly at the limit of your {a} budget :balance_scale:"))

    elif report_format == "n":
        if total_remaining > 0:
            print(emoji.emojize(f"You have ${total_remaining} remaining in your total budget this month. Hooray! :clapping_hands:"))
        elif total_remaining < 0:
            abs_tr = abs(total_remaining)
            print(emoji.emojize(f"You have spent ${abs_tr} over your total budget this month :person_facepalming:"))
        elif total_remaining == 0:
            print(emoji.emojize(f"You have spent all of your total budget this month. Best to pause any new spending :warning:"))
    else:
        pass


def get_budget():
    budget_house = int(input("What's your monthly housing budget? "))
    budget_utility = int(input("What's your monthly utilities budget? "))
    budget_food = int(input("What's your monthly food budget? "))
    budget_misc = int(input("What's your monthly miscellaneous budget? "))

    return budget_house, budget_utility, budget_food, budget_misc

def get_expense():
    total_housing = 0
    total_utilities = 0
    total_food = 0
    total_misc = 0

    while True:
        a = int(input("What are your housing expenses this month? "))
        total_housing = total_housing + a
        cont = input("Do you have another expense to add? (y/n) ").lower()
        if cont == "y":
            continue
        elif cont == "n":
            break

    while True:
        b = int(input("What are your utility expenses this month? "))
        total_utilities = total_utilities + b
        cont2 = input("Do you have another expense to add? (y/n) ").lower()
        if cont2 == "y":
            continue
        elif cont2 == "n":
            break

    while True:
        c = int(input("What are your food expenses this month? "))
        total_food = total_food + c
        cont3 = input("Do you have another expense to add? (y/n) ").lower()
        if cont3 == "y":
            continue
        elif cont3 == "n":
            break

    while True:
        d = int(input("What are your miscellaneous expenses this month? "))
        total_misc = total_misc + d
        cont4 = input("Do you have another expense to add? (y/n) ").lower()
        if cont4 == "y":
            continue
        elif cont4 == "n":
            break

    return total_housing, total_utilities, total_food, total_misc


def itemize_it(rem):
    house = rem[0]
    utility = rem[1]
    food = rem[2]
    misc = rem[3]

    itemized_list = {"Housing": house, "Utilities": utility, "Food": food, "Miscellaneous": misc}

    sorted_itemized_list = sorted(itemized_list.items(), key=lambda x:x[1], reverse=True)
    sorted_list = dict(sorted_itemized_list)

    return sorted_list


if __name__ == "__main__":
    main()


