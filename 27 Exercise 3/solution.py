print("Welcome to the varaliya KBC(Kon Banega CrorePati)")

questions = [
    "The International Literacy Day is observed on",
    "The language of Lakshadweep. a Union Territory of India, is",
    "In which group of places the Kumbha Mela is held every twelve years?",
    "Bahubali festival is related to",
    "Which day is observed as the World Standards  Day?"
]

answers = [
    [
        "1. Sep 8",
        "2. Nov 28",
        "3. May 2",
        "4. Sep 22"
    ],
    [
        "1. Tamil",
        "2. Hindi",
        "3. Malayalam",
        "4. Telugu"
    ],
    [
        "1. Ujjain. Purl; Prayag. Haridwar",
        "2. Prayag. Haridwar, Ujjain,. Nasik",
        "3. Rameshwaram. Purl, Badrinath. Dwarika",
        "4. Chittakoot, Ujjain, Prayag,'Haridwar"
    ],
    [
        "1. Islam",
        "2. Hinduism",
        "3. Buddhism",
        "4. Jainism"
    ],
    [
        "1. June 26",
        "2. Oct 14",
        "3. Nov 15",
        "4. Dec 2"
    ]
]

correct_ans = [1, 3, 2, 4, 2]

final_amt = 0
i = 0
name = input("Enter Your name : ")
while i < len(questions):
    print("\n")
    print("Please select the correct option and win 10000")
    print(f"Your balance is {final_amt}")
    print("\n")
    print(questions[i])
    print("Answers:")
    print(*answers[i], sep="\n")
    print("\n")
    user_answer = int(input("Enter the correct option and win prize : "))
    print("\n")
    
    print("The correct answer is : ", correct_ans[i])
    
    if user_answer == correct_ans[i]:
        final_amt += 10000
        i += 1
    else:
        i += 1
    
print(f"{name} Your Final amount after winning the questions is : {final_amt}")
    
