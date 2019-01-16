# Text-Summarizer

Objective: Take an URL from a newspaper article and automatically summarize it in few sentences.

Goals:
1)	Download the article from online using Python library
2)	Extract the html and div tag from the article python Library
3)	Figuring out the main sentences from the article
4)	Using NLTk library to train my data
5)	Using pandas to see my data frame.
6)  Using tkinter to built the gui for this software


Algorithm:
To extract html, div and other tag I used Beautiful SOUP library in python.
Finding out most important sentences, I used NLTK algorithm. NLTK has building functions to extract long article and split it into sentences. Again, split sentences into word and it has stop words (most common words).
Finding the most common words in the article, and then find the weight frequency of the word. Running the weight frequencies in each sentences and then ranking the sentences. At the end showing the top ranked sentences.
I build the GUI with tkinter, User has to give the URL and no. of sentences they want to see the output. 
I also used pandas for converting my list into data frame so that I can see my output and analyses my data 
