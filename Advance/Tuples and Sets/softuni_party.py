n = int(input())
party_info = [input() for _ in range(n)]
unique_party_codes = set()
guest_come_to_party = set()
for code in party_info:
    if code not in unique_party_codes:
        unique_party_codes.add(code)

while True:
    command = input()
    if command == 'END':
        break
    else:
        guest_come_to_party.add(command)

guest_did_not_come = unique_party_codes.difference(guest_come_to_party)
print(len(guest_did_not_come))
for names in sorted(guest_did_not_come):
    print(names)


