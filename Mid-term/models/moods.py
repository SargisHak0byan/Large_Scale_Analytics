import pandas as pd
import random

books=pd.read_csv(r'data/books.csv')
tags=pd.read_csv(r'data/tags.csv')
btags=pd.read_csv(r'data/book_tags.csv')
books=books.dropna()
tags=tags.dropna()
btags=btags.dropna()

tagsf=pd.merge(tags,btags,left_on='tag_id',right_on='tag_id',how='inner')

fin=tagsf.merge(books, left_on='goodreads_book_id', right_on="book_id", how="inner")

t=['original_title','tag_name']
thr=fin[fin['tag_name']=='thriller']
mys=fin[fin['tag_name']=='mystery']
rom=fin[fin['tag_name']=='romance']
fic=fin[fin['tag_name']=='fiction']

def get_r(romance=list(rom['original_title'])):
	n=random.sample(romance,6)
	return n
	
def get_m(romance=list(mys['original_title'])):
	n=random.sample(romance,6)
	return n

def get_t(romance=list(thr['original_title'])):
	n=random.sample(romance,6)
	return n
	
def get_f(romance=list(fic['original_title'])):
	n=random.sample(romance,6)
	return n
	
#print(list(get_f()))