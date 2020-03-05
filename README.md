# QuizGenerator
A quiz generator written in Python. Inspired by the Automate the Boring Stuff US state capitals quiz project (https://automatetheboringstuff.com/2e/chapter9/).

This CLI tool allows a user to either generate quiz files (in .txt format) or take a practice quiz in the console using the 'practice' command line argument.

The project currently contains 4 files:
* pyDictionaryExtractor.py - a short Python script used to extract state-capital pairs from a hard-coded Python dictionary. This isn't actively used in the main project, but it could be a useful utility to extract other key-value pairs from hard-coded Python dictionaries.
* capsFile.txt - a CSV format .txt file that contains state-capital pairs. This file is read in by the randomQuizGenerator.py file and is used as the basis for the quizzes that are generated.
* randomQuizGenerator.py - the main file for the quiz generation. This file has two modes: quiz file generation mode and practice mode. The practice mode is accessed by passing 'practice' as a command line argument when running the randomQuizGenerator.py file.
* NBAScoringLeadersByTeam.csv - a sample CSV file that contains column headers. These column headers are read in and used during the quiz generation if the user specifies that their CSV file contains column headers.
