import pandas as pd
import numpy as np
import scipy as sp

import plotly.graph_objects as go
import plotly.express as px
import plotly.offline as py
import plotly.figure_factory as ff

from plotly.subplots import make_subplots
from scipy import stats
from pydataset import data

import matplotlib.pyplot as plt
import seaborn as sns

import wrangle as wr

pd.set_option('max_columns', None)
pd.set_option('max_colwidth', None)


def get_numattacks_plot(df):
    
    fig = px.histogram(df, x="country", title='Number of Attacks Per Country in the Middle East', 
                   labels={'count':'Number of Reported Attacks'}, animation_frame='year', color="country",
                   hover_name="country" )

    fig.update_layout(title='Number of Attacks Per Country in the Middle East',
                  title_x=0.5,
                  width=950, height=600, 
                  xaxis_title='Year', 
                  yaxis_title='Number of Attacks',
                  yaxis_range=(0,1800),
                  xaxis_range=(0,20), #you generate y-values for i =0, ...99, 
                                      #that are assigned, by default, to x-values 0, 1, ..., 99
                  
                  updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 1500, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 5}}],
                                               label = "Play",
                                               method = "animate")],
                                type='buttons',
                                showactive=False,
                                y=1,
                                x=1.08,
                                xanchor='center',
                                yanchor='bottom')])

    fig.show()
    return

def get_typeattacks_plot(df):
    fig = px.histogram(df, x="attack_type", title='Type of Attacks in the Middle East', 
                       labels={'count':'Number of Reported Attacks'}, animation_frame='year', color="weaptype",
                       hover_name="country" )

    fig.update_layout(title='Type of Attacks in the Middle East',
                      title_x=0.5,
                      width=1000, height=600, 
                      xaxis_title='Year', 
                      yaxis_title='Number of Attacks',
                      yaxis_range=(0,5000),
                      xaxis_range=(0,10), #you generate y-values for i =0, ...99, 
                                          #that are assigned, by default, to x-values 0, 1, ..., 99

                      updatemenus=[dict(buttons = [dict(
                                                   args = [None, {"frame": {"duration": 1500, 
                                                                            "redraw": True},
                                                                  "fromcurrent": True, 
                                                                  "transition": {"duration": 5}}],
                                                   label = "Play",
                                                   method = "animate")],
                                    type='buttons',
                                    showactive=False,
                                    y=1,
                                    x=1.08,
                                    xanchor='center',
                                    yanchor='bottom')])
    
    fig.show()
    return


def get_toawounded_plot(df):
    fig = px.scatter(df, x='year', y="nwound", color = 'attack_type', size='nwound')
    fig.show()
    return


def get_toagroup_plot(df):
    unknown = df[df['gname']=='Unknown']
    taliban = df[df['gname']=='Taliban']
    isil = df[df['gname']=='Islamic State of Iraq and the Levant (ISIL)']
    shabaab = df[df['gname']=='Al-Shabaab']
    pkk = df[df['gname']== "Kurdistan Workers' Party (PKK)"]
    ttp = df[df['gname']=='Tehrik-i-Taliban Pakistan (TTP)']
    alqaida = df[df['gname']=='Al-Qaida in Iraq']
    sinai = df[df['gname']=='Sinai Province of the Islamic State']
    khorsan = df[df['gname']=='Khorasan Chapter of the Islamic State']
    baloch = df[df['gname']=='Baloch Republican Army (BRA)']
    
    group_name = [unknown, taliban, isil, shabaab, pkk, ttp,
              alqaida, sinai, khorsan, baloch]

    str_name = ['Unknown',
                'Taliban',
                'Islamic State of Iraq and the Levant (ISIL)',
                'Al-Shabaab',
                "Kurdistan Workers' Party (PKK)",
                'Tehrik-i-Taliban Pakistan (TTP)',
                'Al-Qaida in Iraq ',
                'Sinai Province of the Islamic State ',
                'Khorasan Chapter of the Islamic State',
                'Baloch Republican Army (BRA)']
    
    for (name, strname) in zip(group_name, str_name):  
        fig = px.bar(name, x="attack_type", color= 'attack_type', title=f' Most Common Attacks By: {strname}')
        fig.update_traces(dict(marker_line_width=0))
        fig.update_xaxes(visible=False)
        fig.show()
        
    return


def get_attack_months(df): 
    fig = px.histogram(df, x="month", color= 'attack_type', title=' ', nbins = 31)
    fig.update_traces(dict(marker_line_width=0))
    fig.show()
    
    return


def get_attack_day(df):
    fig = px.histogram(df, x="day", color= 'attack_type', title=' ', nbins = 100)
    fig.update_traces(dict(marker_line_width=0))
    fig.show()
    
    return


def get_attack_day_proba(df):
    fig = px.histogram(df, x="day", histnorm='probability density')
    fig.show()
    
    return

def get_attack_day_proba_attacktype(df):
    fig = px.histogram(df, x="day", histnorm='probability density', color='attack_type')
    fig.show()
    
    return 

def get_nationality_attack_plot(df):
    fig = px.histogram(df, x="nationality", color= 'attack_type', title='', 
                   width=1000, height=800)
    fig.update_traces(dict(marker_line_width=0))
    fig.show()
    
    return

def terror_rate(df):
    year_kill= df.groupby(['year'])['nkill'].agg('sum').sort_values(ascending = False)

    year_kill = pd.DataFrame(year_kill).sort_index(ascending=True)

    num_attacks = pd.DataFrame(df.year.value_counts()).sort_index(ascending=True)

    num_attacks = num_attacks.rename(columns={'year':'num_attacks'})

    df1 = year_kill.merge(num_attacks, how='inner', left_on=year_kill.index, right_on=num_attacks.index)

    df1 = df1.rename(columns={'key_0':'year'})
    
    fig = px.scatter(df1 , x= 'year', y='num_attacks' , color= 'nkill',
                 labels={
                     "num_attacks": "Number of Attacks",
                     "year": "Year",
                     "nkill":"Casualties"
                 },
                 title='Terrorist activity (2001-2017)', size= 'nkill')
    fig.show()
    
    return


def get_toafatalities_plot(df):
    fig = px.histogram(df, x="nkill", title='Type of Attacks in the Middle East', nbins = 0,
                   labels={'count':'Number of Reported Attacks'}, animation_frame='year', color="attack_type",
                   hover_name="country" )

    fig.update_layout(title='Type of Attacks and Fatalities',
                  title_x=0.5,
                  width=1000, height=600, 
                  xaxis_title='Number of People Killed', 
                  yaxis_title='Number of Attacks',
                  yaxis_range=(0,1000),
                  xaxis_range=(0,25), #you generate y-values for i =0, ...99, 
                                      #that are assigned, by default, to x-values 0, 1, ..., 99
                  
                  updatemenus=[dict(buttons = [dict(
                                               args = [None, {"frame": {"duration": 1500, 
                                                                        "redraw": True},
                                                              "fromcurrent": True, 
                                                              "transition": {"duration": 5}}],
                                               label = "Play",
                                               method = "animate")],
                                type='buttons',
                                showactive=False,
                                y=1,
                                x=1.08,
                                xanchor='center',
                                yanchor='bottom')])

    fig.update_layout(bargap=0.2)
    fig.show()
    
    return


def terror_rate(df):
    year_kill= df.groupby(['year'])['nkill'].agg('sum').sort_values(ascending = False)

    year_kill = pd.DataFrame(year_kill).sort_index(ascending=True)

    num_attacks = pd.DataFrame(df.year.value_counts()).sort_index(ascending=True)

    num_attacks = num_attacks.rename(columns={'year':'num_attacks'})

    df1 = year_kill.merge(num_attacks, how='inner', left_on=year_kill.index, right_on=num_attacks.index)

    df1 = df1.rename(columns={'key_0':'year'})
    
    fig = px.scatter(df1 , x= 'year', y='num_attacks' , color= 'nkill',
                 labels={
                     "num_attacks": "Number of Attacks",
                     "year": "Year",
                     "nkill":"Casualties"
                 },
                 title='Terrorist activity (2001-2017)', size= 'nkill')
    fig.show()
    
    return


def get_attack_months(df): 
    fig = px.histogram(df, x="month", histnorm='probability density', title=' ', nbins = 31)
    fig.update_traces(dict(marker_line_width=0))
    fig.show()
    return

