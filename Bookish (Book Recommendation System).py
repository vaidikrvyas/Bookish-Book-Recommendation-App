import numpy as np
import pandas as pd

#Data Reading

books=pd.read_csv('BX-Books.csv', sep=";",error_bad_lines=False, encoding='latin-1')

books=books[['ISBN','Book-Title','Book-Author','Year-Of-Publication','Publisher']]

books.rename(columns={'Book-Title':'title','Book-Author':'author', 'Year-Of-Publication':'year','Publisher':'publisher'},inplace=True)

users=pd.read_csv('BX-Users.csv',sep=";",error_bad_lines=False, encoding='latin-1')

users.rename(columns={'User-ID':'user_id','Location':'location','Age':'age'},inplace=True)

ratings=pd.read_csv('BX-Book-Ratings.csv', sep=";",error_bad_lines=False, encoding='latin-1')

ratings.rename(columns={'User-ID':'user_id',"Book-Rating":'rating'},inplace=True)

#Data Abstraction

x=ratings['user_id'].value_counts()>200

y=x[x].index

ratings=ratings[ratings['user_id'].isin(y)]

ratings_with_books=ratings.merge(books,on='ISBN')

number_rating=ratings_with_books.groupby('title')['rating'].count().reset_index()

number_rating.rename(columns={'rating':'number of ratings'},inplace=True)

final_rating=ratings_with_books.merge(number_rating,on='title')

final_rating=final_rating[final_rating['number of ratings']>=50]

final_rating.drop_duplicates(['user_id','title'],inplace=True)

book_pivot=final_rating.pivot_table(columns='user_id',index='title',values='rating')

book_pivot.fillna(0,inplace=True)


from scipy.sparse import csr_matrix
book_sparse=csr_matrix(book_pivot)

from sklearn.neighbors import NearestNeighbors
model=NearestNeighbors(algorithm='brute')

model.fit(book_sparse)

distances,suggestions=model.kneighbors(book_pivot.iloc[237,:].values.reshape(1,-1),n_neighbors=6)
 
lst=[None]*6

def recommend_book():
    book_name=ent.get()
    txt.delete(0.0,'end')
    bookid=np.where(book_pivot.index==book_name)[0][0]
    distances,suggestions=model.kneighbors(book_pivot.iloc[bookid,:].values.reshape(1,-1),n_neighbors=6)
    
    j=0;
    
    for i in range(len(suggestions)):
        lst[j]=book_pivot.index[suggestions[i]].values
        j=j+1; 
        
    for x in lst:
        txt.insert(END, x )
        
#GUI Implementation
        
from tkinter import *
import tkinter 
    
root=Tk()

root.configure(background='#a1aaaf')
root.geometry("450x400")
 
l0=Label(root,text="Bookish",fg="black",justify="center",bg='#a1aaaf')
l0.config(font=("cursive",30))

l1=Label(root,text="Enter Book's Title:",bg='#424949',fg="white")
         
l2=Label(root,text="Top 5 recommendations for you:",bg='#424949',fg="white")
         
l3=Label(root,text="      ",bg='#a1aaaf')
         
l=Label(root,text="      ",bg='#a1aaaf')

ent=Entry(root)

l0.grid(row=0)
l1.grid(row=1)
l.grid(row=3)
l2.grid(row=4,column=0)
l3.grid(row=5)

ent.grid(row=1,column=1)

txt=Text(root,width=50,height=13,wrap=WORD,bg = "light cyan")
txt.grid(row=6,columnspan=2,sticky=W)

btn=Button(root,text="Search",bg="#211e1e",fg="white",activebackground='white',command=recommend_book)
btn.grid(row=2,columnspan=2)


root.mainloop()
