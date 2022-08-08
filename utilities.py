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

