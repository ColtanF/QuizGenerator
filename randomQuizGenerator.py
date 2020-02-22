#! python3
# atbsRandomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key

import random
import pyinputplus as pyip
import sys
import time

# parseCSV(filename):
#   This function parses the first two items in each line of a csv into a dictionary,
#   which is then returned.
#
#   filename: the name of the csv file to be parsed
def parseCSV(filename):
    # This code could be modified to support more than state/capitals
    # Ideally, this code could be used for any kind of flashcard style questions
    capitals = {}
    capsFile = open(filename, 'r')
    for line in capsFile.readlines():
        capitals[line.split(',')[0]] = line.split(',')[1].strip()
    return capitals

# getAnswers(it, states):
#   This code will return a tuple of answerOptions and the correct answer for
#   each quiz question.
#
#   it: iterated question in the current quiz
#   states: list of states to choose from. This could also be cleaned up,
#           this is probably not completely necessary with capitals being
#           a global and states just being list(capitals.keys())
def getAnswers(it, states):
    correctAnswer = capitals[states[it]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers, 3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)
    return (answerOptions, correctAnswer)

# takeQuiz(numQs):
#   This function is called when the user just wants to take a quiz.
#
#   numQs: the number of questions for the user's quiz
def takeQuiz(numQs):
    states = list(capitals.keys())
    rightAns = 0
    random.shuffle(states)
    for questionNum in range(numQs):
        # Get the right and wrong answers.
        answerOptions, correctAnswer = getAnswers(questionNum, states)
        print('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
        for i in range(4):
            print('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        userAns = pyip.inputMenu(['A', 'B', 'C', 'D'],prompt='')
        if (userAns == 'ABCD'[answerOptions.index(correctAnswer)]):
            print('Correct!')
            rightAns +=1
        else:
            print('Incorrect.')
    gradeQuiz(rightAns, numQs)

# gradeQuiz(right,total):
#   This function is called after the user finishes the quiz.
#   The user's grade on the quiz (P/F) is determined and
#   displayed to the user.
#
#   right: The number of answers the user got correct
#   total: The total number of questions in the quiz
def gradeQuiz(right,total):
    print('\n\nGrading quiz...')
    time.sleep(2)
    if (right == total):
        print('PERFECT!')
    elif (right/total > .6):
        print('PASS.')
    else:
        print('FAIL.')
    print('Total answers right: %s/%s (%0.2f%%)' % (right, total, right / total * 100))

# makeQuizzes(numQuizzes, numQuestions):
#   This function handles generating the quiz text files for the user.
#
#   numQuizzes: the number of quizzes the user wants generated
#   numQuestions: the number of questions that will be on each quiz
def makeQuizzes(numQuizzes, numQuestions):
     # Generate 35 different quiz files.
    for quizNum in range(numQuizzes):
        # Create the quiz and answer key files
        quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
        answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

        # Write out the header for the quizNum
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
        quizFile.write('\n\n')

        # Shuffle the order of the states
        states = list(capitals.keys())
        random.shuffle(states)

        # Generate each question.
        for questionNum in range(numQuestions):
            # Get right and wrong answers.
            answerOptions, correctAnswer = getAnswers(questionNum, states)

            # Write the question and answer options to the quiz file
            # TODO: Maybe allow the user to choose question format?
            #       i.e. 'What is the capital of %s' could be replaced by
            #       something like 'What is the ____ of %s' or
            #       'What does _____ mean?'
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum+1, states[questionNum]))
            for i in range(4):
                quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n')

            # Write the answer key to a file
            answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()

    print("%s quizzes successfully generated." % resp)

# getDataFromFile():
#   This function tries to parse data from a file that the user specifies. If the
#   function is unsuccessful at parsing the user's specified file, the function
#   instead parses in the default csv file.
def getDataFromFile():
    # I had trouble getting the optional pyip function parameters to work, so I
    # implemented my own crude version of the mustExist and limit parameters by
    # using a while loop.
    data = {}
    fileFound = False
    i = 0
    while (not fileFound and i < 3):
        try:
            userInp = pyip.inputFilepath("Enter the name of the CSV file to parse for the quiz data:\n", blank=True)
            data = parseCSV(userInp)
            fileFound = True
        except FileNotFoundError:
            print("File to parse not found. Please enter a different file. ")
        i+=1
    if (not fileFound):
        print("\nCould not find file. Importing US state capitals file instead...\n")
        data = parseCSV('capsFile.txt')
    return data

# Main program execution begins here
capitals = getDataFromFile()

# First, check the CLI arguments. If the user specified 'practice', let them
# take a practice quiz.
if (len(sys.argv) >= 2 and sys.argv[1].lower() == 'practice'):
    print("How many questions for your quiz?")
    numOfQuestions = pyip.inputNum('',max=len(capitals))
    takeQuiz(numOfQuestions)

else:
    # The user just wants to generate the quizzes. Ask them how many quizzes, and
    # how many questions per quiz.
    print("How many different quizzes do you need? (Please enter a number)")
    resp = pyip.inputNum()

    print("How many questions in each quiz?")
    numOfQuestions = pyip.inputNum('',max=len(capitals))
    makeQuizzes(resp, numOfQuestions)
