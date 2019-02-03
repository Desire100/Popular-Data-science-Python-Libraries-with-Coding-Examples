#Practice Pandas 

import numpy as np
import pandas as pd

#PART ONE: Creating a Series
"""you can convert a list, numpy array, or dictionary to a Series"""

labels = ['a','b','c']
my_list = [10,20,30]
arr = np.array([10,20,30])
d = {'a':10, 'b': 20, 'c':30}

#Using Lists
pd.Series(data = my_list)
pd.Series(data = my_list, index = labels)
pd.Series(my_list,labels)

#Using Numpy Arrays 
pd.Series(arr)
pd.Series(arr,labels)

#Using Dictionary
pd.Series(d)
pd.Series(d,labels)

#Using an Index
ser1 = pd.Series([1,2,3,4], index = ['USA','Germany','USSR','Japan'])


#PART TWO: DataFrames

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),index = 'A B C D E'.split(),columns = 'W X Y Z'.split())

#Selecting and Indexing
df['W']
#pass a list of column names
df[['W','Z']]
#sql sentax
df.W
#DataFrame Columns are just Series
type(df['W'])

#Creating a new column 
df['new'] = df['W'] + df['Y']

#Removing columns 
df.drop('new', axis =1)
#not inplace unless specified
df.drop('new', axis =1, inplace = True)
#can also drop this way
df.drop('E',axis =0)

#Selecting rows 
df.loc['A']
#or select based off of positioon instead of label
df.iloc[2]
#selecting subset of rows and columns
df.loc['B','Y']

#Conditional selection
df > 0
df[df>0]
df[df['W']>0]


#PART THREE: Missing Data
"""few convenient methods to deal with missing data in pandas"""

df = pd.DataFrame({'A':[1,2,np.nan], 'B':[5,np.nan,np.nan],'C':[1,2,3]})
df.dropna()
df.dropna(axis =1)
df.dropna(thresh =2)
df.fillna(value ='FILL VALUE')
df.fillna(value = df['A'].mean())


#GROUPBY
"""groupby method allows you group rows of data together and call 
   aggregate functions"""

data = {'Company': ['GOOG','GOOG','MSFT','MSFT','FB','FB'],
         'Person': ['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
         'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
"""now you can use the groupby() method to group rows together based off 
of a column name. for instance let's group off of company. this will a 
create a DataFrameGroupBy object"""

df.groupby('Company') 
"""you can save this object as a new variable"""
by_comp = df.groupby("Company")
"""then call aggregate methods off the object"""
by_comp.mean()
df.groupby('Company').mean()
by_comp.std()
by_comp.min()
by_comp.max()
bu_comp.count()
by_comp.describe()
by_comp.describe().transpose()
by_comp.describe().transpose()['GOOG']



#PART FIVE: Merging,Joining, and Concatenating
""" there are 3 main ways of conbibing DataFrames together. 
     Merging, Joining and Concatenating. here we have three methods with 
     examples"""
     
#Example DataFrames 

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                         index=[4, 5, 6, 7])
                         
df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])


# Concatenation
""" concatenation basically glues together DataFrames. 
    Keep in mind that dimensions should match along the axis you are concatenating on.
    you can use pd.concat and pass in a list of DataFrames to concatenate together."""
    
pd.concat([df1,df2,df3])
"""concatenate by columns"""
pd.concat([df1,df2,df3],axis =1)

#Example of DataFrames

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
   
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                          'C': ['C0', 'C1', 'C2', 'C3'],
                          'D': ['D0', 'D1', 'D2', 'D3']}) 

left
right

# Merging 
""" the merge function allows you to merge DataFrame together using 
    a similar logic as merging SQL Tables together."""
    
pd.merge(left,right,how='inner',on='key')
""" or to show a more comlicated"""

left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                               'key2': ['K0', 'K0', 'K0', 'K0'],
                                  'C': ['C0', 'C1', 'C2', 'C3'],
                                  'D': ['D0', 'D1', 'D2', 'D3']})

pd.merge(left, right, on=['key1', 'key2'])
pd.merge(left, right, on=['key1', 'key2'])

#Joining 
""" joining is a convenient method for combination of two potentially
    differentialy-indexed DataFrames into a single result DataFrame."""
 
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2']) 

right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

left.join(right)
left.join(right, how='outer')


#PART SIX: Operations
""" there are lots of operations with pandas that will be really useful"""

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()

#info on unique values
df['col2'].unique()
df['col2'].nunique()
df['col2'].value_counts()

#Applying functions
def times2(x):
    return x*2
df['col1'].apply(times2)
df['col3'].apply(len)
df['col1'].sum()

#permanently removing a column
del df['col1']


#PART SEVEN: Data Input and Output
""" this part is the reference code for getting input and output,
    pandas can read a variety of file using pd.read_methods.
    let's take a look at the most commmon data types."""
    
#CSV 
#csv input
df = pd.read_csv('example')

#csv output
df.to_csv('example',index= False)

#EXCEL
"""Pandas can read and write excel, keep in mind this only imports data.
   mot formulas or images, having images or macros may cause this 
   read_excel method to crash"""
   
#Excel Input
pd.read_excel('Excel_Sample.xlsx',sheetname='Sheet1')
#Excel output
df.to_excel('Excel_Sample.xlsx',sheet_name='Sheet1')

#HTML 
""" you may need to install htmllib5,lxml, and Beautifulsoup4"""

#HTML input
"""pandas read_html function will read tables off of a webpage and 
   return a list of DataFrame objects."""

df = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')

"""Great job"""
