import pandas as pd


def get_perpetrator_df():
    
    
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
    df = df.drop(columns={'Unnamed: 0', 'Unnamed: 0.1', 'year', 'month', 'day'})
    
    # set index
    df = df.set_index('date')
    
    df = df.dropna()
    
    return df