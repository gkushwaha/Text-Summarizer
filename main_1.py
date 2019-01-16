import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re


weighted_frequency=[]
weighted_frequency_sentence=[]
sentences_for_printing=[]
last_list=[]

page =urlopen("https://en.wikipedia.org/wiki/Artificial_intelligence")

soup = BeautifulSoup(page, features="html.parser")

find_all = soup.find_all('p')

text = ''.join(map(lambda p: p.text, find_all))

#print(text)

#Original text
original_text=re.sub(r'\[[0-9]*\]', '', text)

sentences=sent_tokenize(original_text)

#print(sentences)


#Text with out full stop ',', ';', or any character except just word.

new_text= re.sub('[^a-zA-Z]', ' ', text)

new_text = re.sub(r'\s+', ' ', new_text) 

new_text = new_text.split(' ')


stopwords = stopwords.words('english')



#finding the frequency of the word

word_dict= {}

for word in new_text:
	if word not in stopwords:
		if word != '':
			if word in word_dict:
				word_dict[word] += 1
			else:
				word_dict[word] = 1


#getting the top repeted value in  dict 
maximum = max(word_dict, key=word_dict.get) 
maximum_no= word_dict[maximum]

#converting dictonary into dataframe
#Creating dataframe by converting dict to list of items

data=pd.DataFrame(list(word_dict.items()), columns=['Word', 'frequency'])

for i in word_dict:
	calulated_frequencies = word_dict[i]/maximum_no
	weighted_frequency.append(calulated_frequencies)

data['weighted_frequency'] = weighted_frequency

#storing the data frame into decending order based on the frequency column
data=data.sort_values(by=['frequency'], ascending=False)



#print(data.to_string(index=False))

#converting out dataframe of the word frequency into list
data_tolist=data.values.tolist()


new_data=pd.DataFrame(sentences, columns=['sentences'])

#print(new_data)

#calculating the weighted frequency of each word in a sentences 
for sentence in sentences:
	l=0
	if (len(sentence.split(' '))<30):	
		for x in sentence.split(' '):
			k=0
			x=re.sub('[^a-zA-Z]', ' ', x)
			for j in data_tolist:
				#print(data_tolist[k][0])
				if x.lower() == data_tolist[k][0].lower():
					l+=data_tolist[k][2]
					break
				k+=1
	#sentences_for_printing.append(sentence)
	weighted_frequency_sentence.append(l)


new_data['weighted_frequency'] = weighted_frequency_sentence

#print(new_data.head())

new_data=new_data.sort_values(by=['weighted_frequency'], ascending=False)

shorted_five_value=new_data.nlargest(7, 'weighted_frequency')

#print(shorted_five_value)

last_list=shorted_five_value.values.tolist()



print('Title of Article:', soup.title.text)

print('\n')

for i in range(len(last_list)):
	print(last_list[i][0])
	print('\n')
	pass

#print(new_data.values.tolist())



