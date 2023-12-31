import sys # Add 2 extra arguments (starting seed and ending seed) for brute-forcing.
# 3x+1 problem
# The 3x+1 rule is: If x is odd, x=3*x+1. If x is even, x=x/2.
global isEven
isEven=lambda number : not number%2

scriptUsage="3x+1" # Default: "3x+1", change for development use.
# Tests isEven lambda.
# For development use only.
print(not isEven(1)) and (isEven(2)) and (not isEven(3)) and (isEven(4)) and (not isEven(5)) if scriptUsage=="isEven" else None


# Calculates next number based off of the 3x+1 rule.
def nextInt(current):
    return int(current/2 if isEven(current) else current*3+1)

# The thing that calculates the 3x+1 problem.
def problem(seed):
    maximum=0
    steps=0
    current=seed
    ints=[current]
    breakingInt=1
    while current != breakingInt:
        ints.append(current:=nextInt(current))
        if current>maximum:
            maximum=int(current)
        steps+=1
        continue
    return maximum, ints, steps

if len(sys.argv)!=3:
    out=problem(int(input("Seed: ")))
    print(f"Max: {out[0]}")
    print(f"Integers: {out[1]}")
    print(f"Steps: {out[2]}")
else:
    import pyperclip
    answers=[]
    for seed in range(int(sys.argv[1]), int(sys.argv[2])):
        answer=problem(seed)
        answers.append(f"Seed: {seed}")
        answers.append(f"Max: {answer[0]}")
        answers.append(f"Ints: {answer[1]}")
        answers.append(f"Steps: {answer[2]}")
        continue
    answers=str(answers)
    contents=pyperclip.paste()
    pyperclip.copy(answers)
    print(f"Answers copied to clipboard. Clipboard content: {content}")
    print("Brute-forcing done.")
