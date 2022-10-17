to_do_notes_sorted = [0] * 10
while True:
    to_do_notes = input()
    if to_do_notes == 'End':
        break
    to_do_notes = to_do_notes.split('-')
    importance = int(to_do_notes[0]) -1
    note = to_do_notes[1]
    to_do_notes_sorted.pop(importance)
    to_do_notes_sorted.insert(importance, note)
    result = [element for element in to_do_notes_sorted if element != 0]
print(result)
