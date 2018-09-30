# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 15:59:08 2018

@author: pughatol
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
import pickle

data = pd.read_csv("GermanData.csv")

data = data.drop(['foreign_worker'],axis =1)

# Data Transformations

data['status'] = data['status'].map({'A11':'1','A12':'2','A13':'2','A14':'3'})
#print(data.head())
data['credit'] = data['credit'].map({'A30':'1','A31':'1','A32':'2','A33':'3','A34':'3'})
#print(data.head())
data['purpose'] = data['purpose'].map({'A40' : '1',
                            	      'A41' : '2',
                            	      'A42' : '3',
                            	      'A43' : '4',
                            	      'A44' : '5',
                            	      'A45' : '5',
                            	      'A46' : '5',
                            	      'A47' : '5',
                            	      'A48' : '5',
                            	      'A49' : '6',
                            	      'A410' : '5'})
#print(data.head())
data['savings_account_bonds'] = data['savings_account_bonds'].map({'A61' : '1','A62' : '2','A63' : '3','A64' : '3','A65' : '4'})
#print(data.head())
data['other_debtors_guarantors'] = data['other_debtors_guarantors'].map({'A101' : '1','A102' : '2','A103' : '2'})
#print(data.head())
data['other_installment_plans'] = data['other_installment_plans'].map({'A141' : '1','A142' : '1','A143' : '2'})
#print(data.head())
data['housing'] = data['housing'].map({'A151' : '1',
                                       'A152' : '2',
                                       'A153' : '1'
                                       })
#print(data.head())
data = pd.get_dummies(data)
print("HHEHEH",data.head())
data['credibility'] = pd.Categorical(data.credibility)
print("END",data.head())
train,test = train_test_split(data, test_size=0.10,random_state=100)
print(test.head(1))
test.to_csv('test.csv', sep=',', encoding='utf-8')
# Fit regression model
params = {'n_estimators': 300, 'max_depth': 6, 'min_samples_split': 3,
          'learning_rate': 0.007, 'loss': 'ls'}
clf = ensemble.GradientBoostingRegressor(**params)

clf.fit(train.loc[:, train.columns != 'credibility'],train['credibility'])
print(clf.predict(test.loc[:, test.columns != 'credibility']))
mse = mean_squared_error(test['credibility'], clf.predict(test.loc[:, test.columns != 'credibility']))
print("MSE: %.4f" % mse)
pickle.dump(clf, open('clf.pkl', 'wb'))