import datetime

def most_frequent_days(year):
    day_list = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
    start = datetime.date(year,1,1).weekday()
    start_list = day_list[start:]
    end = datetime.date(year,12,25).weekday()
    end_list = day_list[:end]
    answer = []
    for day in start_list:
        if day in end_list:
            answer.append(day)
    if len(answer) > 0:
        return answer
    else:
        return sorted(start_list + end_list)

    return day_list




print(most_frequent_days(2427))
        # output: ['Friday'])
print(most_frequent_days(2185))
        # output: ['Saturday'])
print(most_frequent_days(1770))
        # output: ['Monday'])
print(most_frequent_days(1785))
        # output: ['Saturday'])
print(most_frequent_days(1984))
        # output: ['Monday', 'Sunday'])
print(most_frequent_days(2000))
        # output: ['Saturday', 'Sunday'])
