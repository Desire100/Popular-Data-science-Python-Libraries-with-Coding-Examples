#Practice numpy

import numpy as np

#Create an array of 10 zeros
array=np.zeros(10)

#Create an array of 10 ones 
array = np.ones(10)

#create an array of 10 fives
array = np.zeros(10)+5
array =np.ones(10)*5

#Create an array of all the even integers from 10 to 50
array = np.arange(10,51,2)

#create a 3x3 matrix with values ranging from 0 to 8
m= np.arange(9).reshape(3,3)

#create a 3x3 idenity matrix 
m = np.eye(3)

#use numpy to generate a random number between 0 and 1
number= np.random.rand(1)

#use numpy to generate an array of 25 random numbers 
# sampled from a standard normal distribution
array= np.random.randn(25)

