import pandas as pd     


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
    columns = ['Unnamed: 0', 'Unnamed: 0.1', 'attacktype1', 'targtype1']
    df = df.drop(columns, axis = 1)
    df = df.dropna()
    df = df[df['region_txt'].str.contains('Western Europe')==False]
    return df