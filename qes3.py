try:
    with open('quiz.txt') as file:
        questions = []
        answers = []
        for line in file:
            row = line.strip().split(',')  
            questions.append(row[0])
            answers.append(row[1])
except FileNotFoundError:
    print("The file 'quiz.txt' was not found.")
    exit()
except IndexError:
    print("There was an error reading the 'quiz.txt'. Please check the file format.")
    exit()

name = input("Write Your name: ")

count = 0

for i in range(len(questions)):
    answer = input(questions[i] + " ")
    if answer.lower() == answers[i].lower():
        print("correct")
        count += 1
    else:
        print("Incorrect answer !")

print("YOU got :", count)

try:
    with open('saly.txt', mode='a') as file:
        for item in [name, count]:
            file.write(str(item) + ',')  # Writing as comma-separated values
        file.write('n')  
except Exception as e:
    print(f"An error occurred while writing to 'saly.txt': {e}")
