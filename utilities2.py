import pandas as pd
import numpy as np
import os
import wrangle
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
#sklearn stuff 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from scipy import stats
import utilities
import warnings
warnings.filterwarnings("ignore")


def attacks_by_year(df):
    ''' 
    This function creates a histogram based on the year column of the terrorist df
    '''
	fig = px.histogram(
    df, 
    x = 'year',
    title="Number of Attacks by Year")
	return fig.show()



def top_groups(df):
    ''' 
    This function takes in a df and returns a filtered df of only the top 20 terrorist organizations
    '''
	# create a df of the top 20 groups with their number of attacks
	top_groups = pd.DataFrame(df.atk_group.value_counts().head(20))
	# create a list of the top 20 groups
	top_list= list(top_groups.index)
	# create a new df of the top 20 groups that contains all the info of the original df
	df_top = df[df['atk_group'].isin(top_list)]
	df_top= df_top.sort_values('year')
	return df_top


def attacks_by_group_by_year(df):
    ''' 
    This function creates a histogram of the number of attacks by year by group
    '''
	df_top = top_groups(df)
	color_discrete_map = {'unknown': '#006ba4'}
	fig = px.histogram(
    	df_top, 
    	x = 'atk_group', 
    	animation_frame="year", 
    	range_y = [0,500],
    	range_x = [0,21],
    	color_discrete_map = color_discrete_map,
    	title="Attacks by Group by Year")
	fig.update_layout(
		template='ggplot2')
	fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 3000

	return fig.show()


def killed_by_group_by_year(df):
    ''' 
    This function creates a barchart of the number of people killed each year by individual terrorist groups. 
    '''
	df_top = top_groups(df)
	fig = px.bar(df_top, x="atk_group",y = 'killed', title='Killed by Group by Year', 
                labels={'count':'Number of Reported Attacks'}, animation_frame='year', color="country",
                hover_name="atk_group" )

	fig.update_layout(title='killed by group by year',
                title_x=0.5,
                width=800, height=600, 
                xaxis_title='group', 
                yaxis_title='killed',
                yaxis_range=(0,700),
                xaxis_range=(0,40), 
                  
                updatemenus=[dict(buttons = [dict(
                                             args = [None, {"frame": {"duration": 3000, 
                                                                      "redraw": False},
                                                            "fromcurrent": True, 
                                                            "transition": {"duration": 5}}],
                                             label = "Play",
                                             method = "animate")],
                              type='buttons',
                              showactive=False,
                              y=1,
                              x=1.12,
                              xanchor='right',
                              yanchor='bottom')])
	return fig.show()



def country_attack_graph(df):
    ''' 
    This function shows the number of terrorist incidents each year by country
    '''
	fig = px.histogram(df.country)
	return fig.show()



def groups_by_country(df):
    ''' 
    This function shows the number of terrorist attacks by different terrorist organizations, split by country.
    '''
	df_top = top_groups(df)
	fig = px.histogram(df_top, x="country", title='Killed by Group by Year', 
                labels={'count':'Number of Reported Attacks'}, color="atk_group",
                hover_name="atk_group" )

	fig.update_layout(title='Attacks by Groups',
                title_x=0.5,
                width=800, height=600, 
                xaxis_title='group', 
                yaxis_title='count',
                yaxis_range=(0,10000),
                xaxis_range=(0,17), 
                  
                updatemenus=[dict(buttons = [dict(
                                             args = [None, {"frame": {"duration": 3000, 
                                                                      "redraw": False},
                                                            "fromcurrent": True, 
                                                            "transition": {"duration": 5}}],
                                             label = "Play",
                                             method = "animate")],
                              type='buttons',
                              showactive=False,
                              y=1,
                              x=1.12,
                              xanchor='right',
                              yanchor='bottom')])
	return fig.show()



def country_group_test(train): 
    ''' 
    This function is a chi2 test to determine if there is a relationship between country and attack group. 
    '''
    alpha = .05

    target_table = pd.crosstab(train.country, train.atk_group)

    chi2, p, degf, expected = stats.chi2_contingency(target_table)
    
    
    print( 'alpha =' , .05)
    print('p =', p)
    if p < alpha:
        print('Reject the null')
    else:
        print('Fail to reject the null')
    return



def get_country_dict(train): 
    ''' 
    This function creates dictionaries based on the different countries of the df. 
    '''
	# create a dictionary of the different countries
	country_dict = {}
	countries = train.country.unique()
	for country in countries: 
	    country_dict[country] = train[train.country == country]
	    country_dict[country] = country_dict[country].sort_values('year')
	return 



def attack_graph(dict): 
    ''' 
    This function creates a histogram of the top groups being attacked
    '''
    color_discrete_map = {'unknown': '#006ba4'}
    fig = px.histogram(
        dict, 
        x = 'target', 
        range_y = [0,2000],
        range_x = [0,20],
        color_discrete_map = color_discrete_map,
        title="Count of Groups Attacked"
    )
    return fig.show()


def overall_attack_graph(dict): 
    ''' 
    This function creates a histgram of the top groups being attacked over time.
    '''
    # create a histogram of the top groups over the time frame
    color_discrete_map = {'unknown': '#006ba4'}
    fig = px.histogram(
        dict, 
        x = 'target', 
        range_y = [0,7000],
        range_x = [0,25],
        color_discrete_map = color_discrete_map,
        title="Count of Groups Attacked"
    )
    return fig.show()


def target_terrorist_relationship_test(train):
 ''' 
 This function is a chi2 test to determine if there is a statistical relationship between targets and terrorist organizations.
 '''
    alpha = .05

    target_table = pd.crosstab(train.target, train.atk_group)

    chi2, p, degf, expected = stats.chi2_contingency(target_table)
    
    
    print( 'alpha =' , .05)
    print('p =', p)
    if p < alpha:
        print('Reject the null')
    else:
        print('Fail to reject the null')
    return


def wounded_by_year(train):
    ''' 
    This function creates a scatter plot that shows the relationship between the year, wounded, weapons used columns.
    '''
	fig = px.scatter(train, x = 'year', y = 'wounded', color = 'weap_type', size = 'wounded', title = 'Wounded by Year' )
	return fig.show()


def killed_by_year(train):
    ''' 
    This function creates a scatter plot that shows the relationship between the year, killed, weapons used columns.
    '''
	fig = px.scatter(train, x = 'year', y = 'killed', color = 'weap_type', size = 'killed', title = 'Killed by Year' )
	return fig.show()


def weapon_terrorist_relationship_test(train): 
    ''' 
    This function is a chi2 test that is used to determine the relationship between terrorist organizations and the weapons used. 
    '''
    alpha = .05

    target_table = pd.crosstab(train.weap_type, train.atk_group)

    chi2, p, degf, expected = stats.chi2_contingency(target_table)
    
    
    print( 'alpha =' , .05)
    print('p =', p)
    if p < alpha:
        print('Reject the null')
    else:
        print('Fail to reject the null')
    return




############ modeling ################







def model_data():
    ''' 
    This function is used to create a df for modeling.
    '''
    #create the df
    df = wrangle.create_terrorism_df()
    # establish what columns will be dropped
    cols_to_drop =['eventid',
     'year',
     'month',
     'day',
     'country',
     'region',
     'provstate',
     'city',
     'latitude',
     'longitude',
     'success',
     'suicide',
     'attack_type',
     'targ_desc',
     'targeted_group',
     'tg_desc',
     'nationality',
     'atk_group',
     'claimed',
     'weap_type',
     'weap_sub',
     'killed',
     'us_killed',
     'ter_killed',
     'wounded',
     'us_wounded',
     'ter_wounded',
     'property']
    
    #establish a second df only target variable
    df3 = df.drop(cols_to_drop, axis = 1)
    # create a list of all targeted groups
    bottom_targ_groups = df3.target.value_counts().index.to_list()
    # filter list to not include the top 4 most targeted groups
    bottom_targ_groups = bottom_targ_groups[4:]
    # replace values in list with other in the df3 dataframe
    df3.target = df3.target.replace(bottom_targ_groups, 'other')
    # call in modeling csv
    data = pd.read_csv('modeling_df.csv')
    # change dtype of month to a string
    data.month = df.month.astype('str')
    # change dtype of year to a string
    data.year = df.year.astype('str')
    # drop unnamed column
    data = data.drop(columns = 'Unnamed: 0')
    # reset the index
    df3 = df3.reset_index()
    # drop index column
    df3 = df3.drop(columns = 'index')
    # create a dummy df
    dummy_df = pd.get_dummies(data[['Cluster',
                               'provstate',
                                'year',
                                'suicide',
                                'country',
                                'city',
                                'property',
                              'nationality',
                              'month',
                              'attack_type',
                              'atk_group', 
                              'weap_type',
                              'weap_sub']], dummy_na=False, drop_first=[True, True])
   
    # concat the df3 and dummy df
    df_trial2 = pd.concat([df3, dummy_df], axis = 1)
    
    #split the data
    encoded_train, encoded_validate, encoded_test = wrangle.split_data(df_trial2)
    
    return encoded_train, encoded_validate, encoded_test