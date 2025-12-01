

1DV501 Introduction to Programming
Yetnayet Belachew (yb222ce)
2025

## Introduction

The goal of this project was to make a Python program that can read a text file and show some information about it. The program counts words, lines, and characters, and also finds which words are used the most. It can also show the results in charts and save them to a new file.

For my test, I used the book The Wonderful Adventures of Nils by Selma Lagerlöf. It is a famous Swedish story about a boy traveling across Sweden. I chose this book because it is connected to Sweden and it is a good size for testing.

# Method

I followed the steps from the problem-solving handouts:

Understand the problem: I needed to make a program that reads a text file and gives results.

Plan the solution: I planned to use small functions for each part of the work — reading, counting, showing, and saving.

Write the program: I used what we learned in the lectures.


#  Results

I tested the program with test.txt.
When I run the program, it shows this result:

--- Basic Statistics ---
Total lines: 16501
Total words: 153396
Characters (with spaces): 828441
Characters (no spaces): 688240
Average words per line: 9.30
Average chars per word: 5.40

## Word Analysis ##

Unique words: 9449
Words appearing only once: 4381
Top 10 most common words: the, and, to, he, a, that, of, was, in, had


After that, I exported the results to a file.
The program saved a new file called results_test.txt.txt that includes all the results and analysis.



#  How to Run the Program

Put text_analyser.py and your .txt file (for example test.txt) in the same folder.

Open a terminal and run:

python3 text_analyser.py


Choose options from the menu:

1  Load the file

2  Show basic statistics

3  Run word analysis

4  Export results

The exported file will be saved in the same folder.

#  Conclusion

My program works well and does everything that was required:

It can load and analyse a text file 

It shows basic statistics and a chart 

It has advanced word analysis 

It exports results to a file 

