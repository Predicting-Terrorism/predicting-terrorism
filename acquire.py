import pandas as pd

def get_gtd_df():
    """This function converts the user's local excel file into a dataframe. The excel file can be
    retrived by registeering with https://www.start.umd.edu/gtd/.
    This fucnction returns a dataframe with  """
    df = pd.read_excel('globalterrorismdb_0522dist.xlsx')
    return df


def clean_gt_df(df):
    """ This function takes in a df from the get_gtd_df() function and removes columns with more than 20k null values.
    Args: takes in a dataframe
    Returns: dataframe with 44 columns, each column <10% null"""
    cols_to_drop = []
    for col in list(df.columns):
        if df[col].isna().sum() > 20_000:
            cols_to_drop.append(col)
    df = df.drop(columns = cols_to_drop)
    return df

def get_and_clean_gtd():
    df = get_gtd_df()
    df = clean_gt_df(df)
    return df
