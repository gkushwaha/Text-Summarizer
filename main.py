from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re

page =urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")

soup = BeautifulSoup(page, features="html.parser")


#to find the all the paragraph with tag <p>
find_all = soup.find_all('p')




b=''


#for p in find_all:
#	print(p.text)

#Does the same thing as the for loop does
#TO FIND AND JOIN ALL THE CONTENT which has been EXTRACTED TEXT FROM THE paragraph tag
text = b.join(map(lambda p: p.text, find_all))




#sametext=text.lower()

#removing all the square bracket and numbers from wiki-pidia article

original_text=re.sub(r'\[[0-9]*\]', '', text)


#creating another objet to stor our farmated text which doesnot include fullstop or number.

new_text= re.sub('[^a-zA-Z]', ' ', text)
new_text = re.sub(r'\s+', ' ', new_text) 



#spliting the originla text into single sentences
sentences=sent_tokenize(original_text)
print(sentences)


#print(text)
#print(soup.title.text)
#print(text)

#list of stop words
stopwords = stopwords.words('english')

#split the words into single word for the whole text
words=word_tokenize(text)
#print(words)
#print(words)

#split each sentences from text
sentences=sent_tokenize(text)
#print(sentences[0])



word_dic = dict()

sentence_dic = dict()

for word in words:
	word=word.lower()
	#print(word)
	word=re.sub("[^a-zA-Z0-9]", "", str(word)) # Search for all non-letter, replace with "".
	#print(word)
	if word in stopwords or word is "":
		continue
	if word in word_dic:
		word_dic[word]=word_dic[word]+1
	else:
		word_dic[word]=1
#print(word_dic)

for sentence in sentences:
	#print(sentence)
	#print('\n')
	sentence = sentence.lower()
	for key, value in word_dic.items():
		#print(word[0])
		#print(word)
		if key in sentence:
			if sentence in sentence_dic:
				sentence_dic[sentence] +=value
			else:

				sentence_dic[sentence]=value


#print(sentence_dic)
#print(word_dic)



#print(dic) 

#print(text.split())

#print(sentences)

sumValues = 0
for sentence in sentence_dic:
	#print(sentence)
	sumValues += sentence_dic[sentence]

#print(sumValues)

newValues=0
for key, value in sentence_dic.items():
	newValues += value 

#print(newValues)
#print(len(sentence_dic))
# Average value of a sentence from original text
average = int(newValues / len(sentence_dic))

#print(average)


summary = ''
for sentence in sentence_dic:
	#print(sentence in sentence_dic)
	#print(sentence_dic[sentence])
	if (sentence_dic[sentence] > (1.2*average)):
		summary += " " + sentence

#print(soup.title.text)
#print(summary)

#index=nlargest(n, )

