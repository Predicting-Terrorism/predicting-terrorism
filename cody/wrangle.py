import pandas as pd     
import os
from sklearn.model_selection import train_test_split


def get_terrorism_data():
    ''' 
    This function acquires a local csv entitled final_df.csv and returns it as a dataframe. For this function to run, it must exist as a csv in the working directory
    '''
    filename = 'final_df.csv'

    if os.path.isfile(filename):
        df = pd.read_csv(filename, index_col = 0)
        return df


def prep_df(df):
    ''' This function prepares the terrorism df for exploration and returns it.
    '''
    columns = ['Unnamed: 0.1', 'attacktype1', 'targtype1', 'targsubtype1']
    df = df.drop(columns, axis = 1)
    df = df.dropna()
    df = df[df['region_txt'].str.contains('Western Europe')==False]
    df.region_txt = df.region_txt.apply(str.lower)
    df.provstate = df.provstate.apply(str.lower)
    df.city = df.city.apply(str.lower)
    df.weaptype1_txt = df.weaptype1_txt.apply(str.lower)
    df.weapsubtype1_txt = df.weapsubtype1_txt.apply(str.lower)
    df = df.rename(columns = {'iyear' : 'year', 'imonth' : 'month', 'iday' : 'day', 'country_txt' : 'country', 'region_txt' : 'region', 'attacktype1_txt' : 'attack_type' , 'targtype1_txt' : 'target', 'targsubtype1_txt' : 'targ_desc' , 'corp1' : 'targeted_group', 'target1' : 'tg_desc', 'natlty1_txt': 'nationality', 'gname' : 'atk_group', 'weaptype1_txt':'weap_type' , 'weapsubtype1_txt' : 'weap_sub', 'nkill' : 'killed' , 'nkillus':'us_killed' , 'nkillter' : 'ter_killed', 'nwound':'wounded' , 'nwoundus' : 'us_wounded' , 'nwoundte':'ter_wounded'})
    df.attack_type = df.attack_type.apply(str.lower)
    df.target = df.target.apply(str.lower)
    df.targ_desc = df.targ_desc.apply(str.lower)
    df.targeted_group = df.targeted_group.apply(str.lower)
    df.tg_desc = df.tg_desc.apply(str.lower)
    df.nationality = df.nationality.apply(str.lower)
    df.atk_group = df.atk_group.apply(str.lower)
    return df


def split_data(df):
    '''
    Takes in a cleaned dataframe, splits it into train, validate and test subgroups and then returns those subgroups.
    Arguments: df - a cleaned pandas dataframe with the expected feature names and columns in a dataset
    Return: train, validate, test - dataframes ready for the exploration and model phases.
    '''

    train_validate, test = train_test_split(df, test_size=.2, 
        random_state=17)

    train, validate = train_test_split(train_validate, test_size=.3, 
        random_state=17)
    return train, validate, test




    ###############################################

    ## download big csv as terrorism.csv


file = 'terrorism.csv'
df = pd.read_csv(file, encoding='cp1252')

df_date = df[df.iyear > 2000]

middle_east_countries = ['bahrain', 'cyprus', 'egypt', 'iran', 'iraq', 'israel', 'jordan', 'kuwait', 'lebanon', 'oman', 'palestine', 'qatar', 'saudi arabia', 'syria', 'afghanistan'
                        , 'djibouti', 'turkey', 'maghreb', 'pakistan', 'sudan', 'somalia']



filtered_df = df_date[df_date['country_txt'].isin(middle_east_countries)]

filtered_df.to_csv('filtered_terrorism_df.csv')