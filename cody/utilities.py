import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os





######## encode variables ############


def is_explosion(df):
	if df.attack_type.lower() == 'bombing/explosion':
		return 1
	else:
		return 0

def is_armed_assault(df):
	if df.attack_type.lower() == 'armed assault':
		return 1
	else:
		return 0

def is_assassination(df):
	if df.attack_type.lower() == 'assassination':
		return 1
	else:
		return 0

def is_kidnapping(df):
	if df.attack_type.lower() == 'hostage taking (kidnapping)':
			return 1
	else:
		return 0


def is_infrastructure(df):
	if df.attack_type.lower() == 'facility/infrastructure attack':
			return 1
	else:
		return 0


attack_list = ['bombing/explosion', 'armed assault', 'assassination', 'hostage taking (kidnapping)' , 'facility/infrastructure attack']


def is_other(df):
	if  df[df['attack_type'].contains(attack_list)]:
		return 0
	else:
		return 1


def encode_attack_type(df):
	df['is_explosion'] = df.apply(is_explosion, axis = 1)

	df['is_armed_assault'] = df.apply(is_armed_assault, axis = 1)

	df['is_assassination'] = df.apply(is_assassination, axis = 1)

	df['is_kidnapping'] = df.apply(is_kidnapping, axis = 1)

	df['is_infrastructure'] = df.apply(is_infrastructure, axis = 1)

	df['is_other'] = df.apply(is_other, axis = 1)

	return df
