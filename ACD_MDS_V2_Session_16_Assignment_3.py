# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 09:53:16 2018

@author: Eliud Lelerai
"""

import numpy as np
import pandas as pd
import matplotlib as mpl

# considering  a class of 100 students, for a random student: 

   #The probability of failing in 0 subjects, P(X=0) = 0.8

   #The probability of failing in 1 subjects, P(X=1) = 0.1

   #The probability of failing in 2 subjects, P(X=2) = 0.07

   #The probability of failing in 3 subjects, P(X=3) = 0.03

# Creating Probability distribution

data={'x':list(range(4)),'p(x)':[0.8,0.1,0.07,0.03]}
probability_distribution=pd.DataFrame(data,columns=['x','p(x)'])