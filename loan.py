#################                  ##############
# Machine Learning Project - Loan Forgiveness ###
######## STARTED Saturday August 17th, 2019 #####
#################                  ##############


import numpy as np
import pandas as pd
import matplotlib as plt



# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)



###############################
# READING IN THE TEST DATA


#df = pd.read_csv('Desktop/Machine Learning/Loan Prediction/train_ctrUa4K.csv')
df = pd.read_csv('train_ctrUa4K.csv')
############################3##
###############################
# MUNGING PART 1 - FILLING IN NULL DATA


      #####  
# Check
# print(df.apply(lambda x: sum(x.isnull())))
      #####


# df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)


# Here we assume Self_Employed nulls = 'No' (i.e. not self-employed)
df['Self_Employed'].fillna('No', inplace = True)


      #####  
# Check
# print(df.apply(lambda x: sum(x.isnull())))
      #####
      

# We will say that empty loan amounts are filled by the median of 
# loan amounts the corresponding category of (self/empld, grad)
# as these are both binary categories

# This process can be done using pivot tables
# Here is the process done in python:

table = df.pivot_table(values = 'LoanAmount', index = 'Self_Employed', columns = 'Education', aggfunc = np.median)
# print(table)

# Define a function to return value of this pivot table by category
def fage(x):
    return table.loc[x['Self_Employed'],x['Education']]
    
# Replace missing values with fage
df['LoanAmount'].fillna(df[df['LoanAmount'].isnull()].apply(fage, axis = 1), inplace = True)

# print(df.apply(lambda x: sum(x.isnull())))


# Now we must full in null values for
# Gender
# Married
# Dependents
# Loan_Amount_Term
# Credit History

#####
# for Credit History I will assume that None means no history:
df['Credit_History'].fillna(0, inplace = True)
# print(df.apply(lambda x: sum(x.isnull())))

#####
# for gender - most seem to be men.
# I will run a gender check on the entire column and if
# at least 80% of listing are men I will make all null = male

#print(df['Gender'].value_counts())
#print(str(48900.0/(489.0+112.0)) + "% are Men")
 
# 81% are men so we'll assume all nulls are men
df['Gender'].fillna('Male', inplace =True)
#print(df.apply(lambda x: sum(x.isnull())))
#print(df['Gender'].value_counts())


#####
# for married there are only 3 values, so we'll just make them
# whichever state is more common

#print(df['Married'].value_counts())

# Married.YES is more common so we'll just make all 3 nulls married
df['Married'].fillna('Yes', inplace =True)
#print(df.apply(lambda x: sum(x.isnull())))
#print(df['Married'].value_counts())


#####
# for Dependents we'll do our pivot table again on the binary
# categories of Gender and Married

df['Dependents'].replace('3+', 3, inplace=True)
df['Dependents'].replace('2', 2, inplace=True)
df['Dependents'].replace('1', 1, inplace=True)
df['Dependents'].replace('0', 0, inplace=True)
table = df.pivot_table(values = 'Dependents', index = 'Gender', columns = 'Married', aggfunc = np.median)
# print(table)
# Define a function to return value of this pivot table by category
def fage2(x):
    return table.loc[x['Gender'],x['Married']]
    
# Replace missing values with fage2
df['Dependents'].fillna(df[df['Dependents'].isnull()].apply(fage2, axis = 1), inplace = True)
#print(df.apply(lambda x: sum(x.isnull())))
#print(df['Dependents'].value_counts())


#####
# for Loan_Amount_Term I'll fill all None with the most common value: 360
df['Loan_Amount_Term'].fillna('360', inplace =True)






#############
# ALL DATA FULL, NOW TO ADJUST

#####
# To adjust for massive skew upwards on  loan amount and
# income let's use a log function and combine app/coapp income

df['LoanAmount_log'] = np.log(df['LoanAmount'])
#print(df.apply(lambda x: sum(x.isnull())))

df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']
df['TotalIncome_log'] = np.log(df['Total_Income'])
#print(df.apply(lambda x: sum(x.isnull())))


####################################################
###                                           ###### 
#      ALL VALUES FULL, LET'S DATA, BITCH        ###
                                                   #
####################################################
import sklearn
from sklearn import preprocessing as pp

var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
le = pp.LabelEncoder()
for i in var_mod:
    df[i] = le.fit_transform(df[i])

df.dtypes

### CHECK LABELENCODER
# print(df['Gender'].value_counts())
###


from sklearn import linear_model as lm
from sklearn import model_selection as ms
from sklearn import ensemble as ens
from sklearn import tree
from sklearn import metrics

# This is a generic function for making a classification model and 
# then accessing its performance
# Feel free to reuse this for future projects













def classification_model(model, data, predictors, outcome):
    # Fit the model:
    model.fit(data[predictors], data[outcome])
    
    # Make predictions on training set:
    predictions = model.predict(data[predictors])
    
    # Print accuracy:
    accuracy = metrics.accuracy_score(predictions,data[outcome])
    print("Accuracy: %s" % "{0:.3}".format(accuracy))
    
    # Perform k-fold cross-validation with 5 folds:
    cv = ms.KFold(n_splits = 5)
    error = []
    for train, test in cv.split(data):
        # Filter training data:
        train_predictors = (data[predictors].iloc[train,:])
        
        # The target we're using to train the algorithm
        train_target = data[outcome].iloc[train]
        
        # Training the algorith using the predictors and target
        model.fit(train_predictors, train_target)
        
        # Record error from each cross-validation run
        error.append(model.score(data[predictors].iloc[test,:], data[outcome].iloc[test]))
    
    print("Cross-Validation Score: %s" % "{0:.3%}".format(np.mean(error)))
    
    # Fit the model again so that it can be refered to outside the function:
    model.fit(data[predictors],data[outcome])
    


############
# Logistic Regression Model:

#####
# First: only using credit score as a predictor:

outcome_var = 'Loan_Status'
model = lm.LogisticRegression()
predictor_var = ['Credit_History']

#classification_model(model, df, predictor_var, outcome_var)
            
    # Accuracy: 0.77
    # Cross-Validation Score: 77.041%
       
#######           
# Now using 5 variables          
                    
model = lm.LogisticRegression()
predictor_var = ['Credit_History','Education','Married','Self_Employed','Property_Area']

#classification_model(model, df, predictor_var, outcome_var)
    # Accuracy: 0.77
    # Cross-Validation Score: 77.041%
   
    # Not much better, I'll mess with it later
      
##############
# Decision Tree Method

model = tree.DecisionTreeClassifier()
predictor_var = ['Credit_History','Gender','Married','Education']

classification_model(model, df,predictor_var,outcome_var)

    # Accuracy: 0.772
    # Cross-Validation Score: 76.553%
    
    # NOT BAD! better, at least than logistic regression served
    # I'ma try my own variables
    
######### MY OWN CODE WOOOOOO #############

print(df.head(5))

# OK. I decided I want to test for loan_amount, total_income,
# and credit history. Let's see.

model = lm.LogisticRegression()
predictor_var = ['LoanAmount_log', 'TotalIncome_log', 'Loan_Amount_Term']
print("Logistic Regression: ")
classification_model(model, df,predictor_var,outcome_var)

#Logistic Regression:
#Accuracy: 0.687
#Cross-Validation Score: 68.729%

model = tree.DecisionTreeClassifier()
predictor_var = ['LoanAmount_log', 'TotalIncome_log', 'Credit_History']
print("Decision Tree: ")
classification_model(model, df,predictor_var,outcome_var)

#Decision Tree:
#Accuracy: 1.0
#Cross-Validation Score: 66.300%

####### AWWWW BACK TO STRUCTURED CODE ######

###############
# Random Forest (Forest only has one 'r'?)

