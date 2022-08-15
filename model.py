import pandas as pd
import wrangle as w
import explore as e
import seaborn as sns


from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

from functools import reduce

import matplotlib.pyplot as plt

# importing necessary libraries
import pandas as pd
import numpy as np


from kmodes.kmodes import KModes
import matplotlib.pyplot as plt



def create_model_df():
    # acquire dataframe
    df = w.get_perpetrator_df()

    # create production dataframe based on the target variables
    production_df = df[df['gname'].str.contains('Unknown')==True]

    # create target variable dataframe
    df1 = df[df['gname'].str.contains('Unknown')==False]

    # drop columns from the dataframe that arent relevant in the predictor
    model_df = df1.drop(columns=['event_id',
                 'month',
                 'day',
                 'region',
                 'latitude',
                 'longitude',
                 'success',
                 'attacktype_n',
                 'targtype_n',
                 'targsubtype_n',
                 'targsubtype',
                 'corp1',
                 'target_description',
                 'nationality',
                 'claimed',
                 'weapdesc',
                 'nkillus',
                 'nkillter',
                 'nwound',
                 'nwoundus',
                 'nwoundte',
                 'property'])

    # create backup df
    production_df2 = production_df.drop(columns=['event_id',
                 'region',
                 'success',
                 'attacktype_n',
                 'targtype_n',
                 'targsubtype_n',
                 'targsubtype',
                 'corp1',
                 'target_description',
                 'nationality',
                 'claimed',
                 'weapdesc',
                 'nkillus',
                 'nkillter',
                 'nwound',
                 'nwoundus',
                 'nwoundte',
                 'property'])

    # create production df
    production_df = production_df.drop(columns=['event_id',
                 'month',
                 'day',
                 'region',
                 'latitude',
                 'longitude',
                 'success',
                 'attacktype_n',
                 'targtype_n',
                 'targsubtype_n',
                 'targsubtype',
                 'corp1',
                 'target_description',
                 'nationality',
                 'claimed',
                 'weapdesc',
                 'nkillus',
                 'nkillter',
                 'nwound',
                 'nwoundus',
                 'nwoundte',
                 'property'])

    # change year to object type
    model_df.year = model_df.year.astype('str')
    production_df.year = production_df.year.astype('str')

    data = model_df
    return data, production_df, production_df2


def loop_boop(data, production_df):  
    ''' This function takes in 2 dataframes and
    '''
    i = 4
    while i > 0:
        y1 = set(production_df['provstate'])
        x1 = set(data['provstate'])

        y2 = set(production_df['city'])
        x2 = set(data['city'])

        prov_diff = y1.difference(x1)
        prov_diff = list(prov_diff)

        prov_diff2 = x1.difference(y1)
        prov_diff2 = list(prov_diff2)

        city_diff = y2.difference(x2)
        city_diff = list(city_diff)

        city_diff2 = x2.difference(y2)
        city_diff2 = list(city_diff2)

        for prov in prov_diff:
            production_df = production_df[production_df.provstate!=prov]

        for prov1 in prov_diff2:
            data = data[data.provstate!=prov1]

        for cities in city_diff:
            production_df = production_df[production_df.city!=cities]

        for cities1 in city_diff2:
            data = data[data.city!=cities1]
            
        i = i -1
    return data, production_df


def scaling_func(data): 
    # create a dataframe for the gname target variable
    gnames = pd.DataFrame(data.gname)

    # create nkill df
    nkills = pd.DataFrame(data.nkill)

    # scale nkill
    from sklearn.preprocessing import MinMaxScaler
    scaler = MinMaxScaler()

    scaler.fit(nkills)
    nkills = pd.DataFrame(scaler.transform(nkills))
    nkills = nkills.rename(columns={0:'nkill'})
    
    print(data.shape[0], gnames.shape[0], nkills.shape[0])
    return gnames, nkills



def dummy_df(data, gnames, nkills):   
    ''' This function takes in columns from a df and creates dummy variables based on the values of those columns.
    '''
    dummy_df = pd.get_dummies(data[['country',
                                        'provstate',
                                        'city',
                                        'suicide',
                                        'attack_type', 
                                        'targtype',  
                                        'weaptype',
                                        'year']], dummy_na=False, drop_first=[True, True])

    dummy_df = dummy_df.reset_index(drop=True)
    dummy_df.index

    gnames = gnames.reset_index(drop=True)
    gnames.index

    dummy_df = pd.concat([dummy_df, gnames, nkills], axis=1)

    print(dummy_df.shape)
    return dummy_df


def train_validate_test_split(df, target, seed=123):
    '''
    This function takes in a dataframe, the name of the target variable
    (for stratification purposes), and an integer for a setting a seed
    and splits the data into train, validate and test. 
    Test is 20% of the original dataset, validate is .30*.80= 24% of the 
    original dataset, and train is .70*.80= 56% of the original dataset. 
    The function returns, in this order, train, validate and test dataframes. 
    '''
    train_validate, test = train_test_split(df, test_size=0.27, 
                                            random_state=seed, 
                                            stratify=df[target])
    train, validate = train_test_split(train_validate, test_size=0.35, 
                                       random_state=seed,
                                       stratify=train_validate[target])
    return train, validate, test
