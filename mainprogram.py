import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
import re

class mainprogram:

	def __init__(self, value1, value2):
		self.url = str(value1)
		self.value2 = int(value2)
		self.stopwords = stopwords.words('english')
		self.get_text_from_url()

	def get_text_from_url(self):
		try:
			page =urlopen(self.url)
		except:
			self.message="Please Enter Valid Url"

		self.soup = BeautifulSoup(page, features="html.parser")


		#extracting all the sentences which start with <p> tag
		find_all = self.soup.find_all('p')

		#Joining all the extracted sentences
		self.text = ''.join(map(lambda p: p.text, find_all))

		#Our original text
		#wiki stores every sentences in a number. so removing the number inside box []
		self.original_text=re.sub(r'\[[0-9]*\]', '', self.text)
		#print(self.original_text)

		new_text= re.sub('[^a-zA-Z]', ' ', self.text)

		self.new_text = re.sub(r'\s+', ' ', new_text) 

		self.sentences=sent_tokenize(self.original_text)
		
		self.text_manupulation(self.new_text)



	def text_manupulation(self, new_text):

		new_text = new_text

		new_text = new_text.split(' ')

		#finding the frequency of the word
		word_dict= {}

		for word in new_text:
			if word not in self.stopwords:
				if word != '':
					if word in word_dict:
						word_dict[word] += 1
					else:
						word_dict[word] = 1

		#getting the top repeted value in  dict 
		self.maximum = max(word_dict, key=word_dict.get) 
		self.maximum_no= word_dict[self.maximum]


		self.converting_into_dataframe(word_dict)

	
	def converting_into_dataframe(self, word_dict):

		weighted_frequency=[]
		sentences_tap=[]
		weighted_frequency_sentence=[]
		self.final_item=[]
		#converting dictonary into dataframe
		#Creating dataframe by converting dict to list of items
		data=pd.DataFrame(list(word_dict.items()), columns=['Word', 'frequency'])

		for i in word_dict:
			calulated_frequencies = word_dict[i]/self.maximum_no
			weighted_frequency.append(calulated_frequencies)

		data['weighted_frequency'] = weighted_frequency

		#storing the data frame into decending order based on the frequency column
		data=data.sort_values(by=['frequency'], ascending=False)

		print(data)

		#converting out dataframe of the word frequency into list
		data_tolist=data.values.tolist()
		
		new_data=pd.DataFrame(self.sentences, columns=['sentences'])

		#calculating the weighted frequency of each word in a sentences 
		for sentence in self.sentences:
			l=0
			if (len(sentence.split(' '))<30):
				#making an array of sentences with length less than 30
				sentences_tap.append(sentence)	
				for x in sentence.split(' '):
					x=re.sub('[^a-zA-Z]', ' ', x)
					for j in range(len(data_tolist)):
						#print(data_tolist[k][0])
						if x.lower() == data_tolist[j][0].lower():
							l+=data_tolist[j][2]
							break
				#making an array of weighted frequency
				weighted_frequency_sentence.append(l)

		#converting the new value into dictnoary
		value={"Sentences" :sentences_tap, "weighted_frequency" :weighted_frequency_sentence}

		#converting into dataframe for sentences and its weighted frequency
		new_data = pd.DataFrame(value)

		print("<<<<")
		
		new_data=new_data.sort_values(by=['weighted_frequency'], ascending=False)

		print(new_data)

		shorted_value=new_data.nlargest(self.value2, 'weighted_frequency')

		summery=shorted_value.values.tolist()


		for i in summery:
			self.final_item.append(i[0])


		self.page_title = self.soup.title.text

		self.final()

	def final(self):
		return self.final_item, self.page_title











