import pandas as pd
import os


# file = 'terrorism.csv'
# df = pd.read_csv(file, encoding='cp1252')
# df_date = df[df.iyear > 2000]
# middle_east_countries = ['bahrain', 'egypt', 'iran', 'iraq', 'israel', 'jordan', 'kuwait', 'lebanon', 'oman', 'palestine', 'qatar', 'saudi arabia', 'syria', 'afghanistan'
#                         , 'djibouti', 'turkey', 'maghreb', 'pakistan', 'sudan', 'somalia']
# filtered_df = df_date[df_date['country_txt'].isin(middle_east_countries)]
# filtered_df.to_csv('filtered_terrorism_df.csv')



def get_gtd_df():
    """This function converts the user's local excel file into a dataframe. The excel file can be
    retrived by registeering with https://www.start.umd.edu/gtd/.
    This fucnction returns a dataframe with  """
    df = pd.read_excel('globalterrorismdb_0522dist.xlsx')
    return df

def prep_df():
    ''' This function prepares the terrorism df for exploration and returns it.
    '''
    df = pd.read_excel('globalterrorismdb_0522dist.xlsx')
    columns = ['Unnamed: 0.1', 'attacktype1', 'targtype1', 'targsubtype1']
    df = df.drop(columns, axis = 1)
    # df = df.dropna()
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


def clean_gt_df(df):
    """ This function takes in a df from the get_gtd_df() function and removes columns with more than 20k null values.
    Args: takes in a dataframe
    Returns: dataframe with 44 columns, each column <10% null"""
    df = prep_df()
    cols_to_drop = []
    for col in list(df.columns):
        if df[col].isna().sum() > 20_000:
            cols_to_drop.append(col)
    df = df.drop(columns = cols_to_drop)
    return df

def get_and_clean_gtd():
    df = clean_gt_df(df)
    df = pd.DataFrame(df.groupby('gname').filter(lambda x : len(x)>100))
    #renames columns
    df = df.rename(columns={'eventid':'event_id', 'iyear':'year', 'imonth':'month', 'iday':'day', 
                    'country_txt':'country', 'region_txt':'region', 'attacktype1':'attacktype_n', 
                    'attacktype1_txt': 'attack_type', 'targtype1':'targtype_n','targtype1_txt':'targtype', 
                    'targsubtype1':'targsubtype_n', 'targsubtype1_txt':'targsubtype', 'corp':'target_id', 
                    'target1':'target_description', 'natlty1_txt':'nationality', 'weaptype1_txt':'weaptype', 
                    'weapsubtype1_txt':'weapdesc'})
    # removes impossible dates
    df = df[df.day != 0]
     # create date-time 
    df['date'] = pd.to_datetime(df.year.astype(str) + '/' + df.month.astype(str) + '/' + df.day.astype(str))
    # drops uneeeded columns
    #df = df.drop(columns={'Unnamed: 0', 'Unnamed: 0.1'})
    # set index
    #df = df.set_index('date')
    # drop columns where gname = Unknown
    # alt code for this identical function: df = df[df['gname'].str.contains('Unknown) == False]
    df = df[df.gname!='Unknown']
    # drop columns where gname is null
    df.to_csv('maximum_gtd_df.csv', index=False)
    return df

def get_maximum_df(use_cache=True):
    """This function returns the maximum dataframe where there is a label for terror group (gname). It drops rows where gname is null or 'unknown'."""
    filename = "'maximum_gtd_df.csv'"
    if os.path.isfile(filename) and use_cache:
        # .values returns a list of values from Series, instead of
        # a Series, which this acquire cannot process.
        return pd.read_csv(filename).values
    else:
        #obtains data and sets to dataframe.
        df = get_and_clean_gtd()
        df.to_csv('maximum_gtd_df.csv', index=False)
    return df


def get_perpetrator_df():
    """This function returns the smaller df used to build the initial predictive model. 
    It drops all nulls, and returns approx 40k rows"""
    #obtains data and sets to dataframe.
    df = pd.read_csv('final_df.csv')
    df = pd.DataFrame(df.groupby('gname').filter(lambda x : len(x)>300))
    
    #renames columns
    df = df.rename(columns={'eventid':'event_id', 'iyear':'year', 'imonth':'month', 'iday':'day', 
                    'country_txt':'country', 'region_txt':'region', 'attacktype1':'attacktype_n', 
                    'attacktype1_txt': 'attack_type', 'targtype1':'targtype_n','targtype1_txt':'targtype', 
                    'targsubtype1':'targsubtype_n', 'targsubtype1_txt':'targsubtype', 'corp':'target_id', 
                    'target1':'target_description', 'natlty1_txt':'nationality', 'weaptype1_txt':'weaptype', 
                    'weapsubtype1_txt':'weapdesc'})
    
    # removes impossible dates
    df = df[df.day != 0]
    
    # create date-time 
    df['date'] = pd.to_datetime(df.year.astype(str) + '/' + df.month.astype(str) + '/' + df.day.astype(str))
    
    # drops uneeeded columns
    df = df.drop(columns={'Unnamed: 0', 'Unnamed: 0.1'})
    
    # set index
    df = df.set_index('date')
    
    df = df.dropna()
    
    return df

def get_maximum_df(use_cache=True):
    filename = "'maximum_gtd_df.csv'"
    if os.path.isfile(filename) and use_cache:
        # .values returns a list of values from Series, instead of
        # a Series, which this acquire cannot process.
        return pd.read_csv(filename).values
    else:
        #obtains data and sets to dataframe.
        df = get_and_clean_gtd()
    return df

# How is the tree making decisions? print the diagram, 
# this is a highly interpretable model
# KNN to impute nulls
