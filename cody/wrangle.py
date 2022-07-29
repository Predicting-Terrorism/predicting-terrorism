import pandas as pd     
import os

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