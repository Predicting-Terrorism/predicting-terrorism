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
	fig = px.histogram(
    df, 
    x = 'year',
    title="Number of Attacks by Year")
	return fig.show()



def top_groups(df):
	# create a df of the top 20 groups with their number of attacks
	top_groups = pd.DataFrame(df.atk_group.value_counts().head(20))
	# create a list of the top 20 groups
	top_list= list(top_groups.index)
	# create a new df of the top 20 groups that contains all the info of the original df
	df_top = df[df['atk_group'].isin(top_list)]
	df_top= df_top.sort_values('year')
	return df_top


def attacks_by_group_by_year(df):
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
	fig = px.histogram(df.country)
	return fig.show()



def groups_by_country(df):
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
	# create a dictionary of the different countries
	country_dict = {}
	countries = train.country.unique()
	for country in countries: 
	    country_dict[country] = train[train.country == country]
	    country_dict[country] = country_dict[country].sort_values('year')
	return 



def attack_graph(dict): 
    # create a histogram of the top groups over the time frame
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
	fig = px.scatter(train, x = 'year', y = 'wounded', color = 'weap_type', size = 'wounded', title = 'Wounded by Year' )
	return fig.show()


def killed_by_year(train):
	fig = px.scatter(train, x = 'year', y = 'killed', color = 'weap_type', size = 'killed', title = 'Killed by Year' )
	return fig.show()


def weapon_terrorist_relationship_test(train): 
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











