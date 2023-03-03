def function(first,second,third,students):
    answer_per_hour = first + second + third
    needed_hours = 0
    while students > 0:
        students -= answer_per_hour
        needed_hours+=1
        if needed_hours %4 == 0:
            needed_hours+=1
    return needed_hours
employee_efficiency1 = int(input())
employee_efficiency2 = int(input())
employee_efficiency3 = int(input())
stundets_count = int(input())

print(f"Time needed: {function(employee_efficiency1,employee_efficiency2,employee_efficiency3,stundets_count)}h.")