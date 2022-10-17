print("Are you ready to start?")
print("Yes or No")
answer = input()
if answer == "Yes":
    print("Which is the capital of Bulgaria?")
    name = input()
    if name == "Sofia":
        print("Correct!")
        print("Next question.")
        print("Which is the capital of France?")
        name2 = input()
        if name2 == "Paris":
            print("Correct again!!")
            print("Final question.")
            print("Who sings the song 'We are the champions'")
            name3 = input()
            if name3 == "Queen":
                print("Congratulations, You are the champion!!")
            else:
                print("You dropped out in the final, sorry.")
        else:
            print("Wrong answer!")
    else:
        print("Try again!")
else:
    print("You lose ;D")