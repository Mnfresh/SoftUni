days = int(input())
daily_plunder = int(input())
expected_plunder = int(input())
total_plunder = 0
for day in range(1, days+1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        loss = total_plunder * 0.3
        total_plunder -= loss

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage_plunder = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage_plunder:.2f}% of the plunder.")


