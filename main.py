##This is a project completed for the Udacity Data Analyst Nanodegree. 
##Most code is drawn from my answers to problem sets 2-4 in the Intro to Data Science course.
##Other is drawn from the seaborn documentation linked on the Anaconda page, found here:
##	http://stanford.edu/~mwaskom/software/seaborn/ and
##	http://stanford.edu/~mwaskom/software/seaborn/tutorial.html
##
## Jupyter reference that got me actually using QT Console:
##http://jupyter.org/qtconsole/stable/index.html
##
##
##Author: Casey Faist

import seaborn
import matplotlib.pyplot as plt
import pandas
import numpy
import scipy
import scipy.stats
import statsmodels.api as sm

datastuff = '/Users/Casey/miniconda3/envs/datagraphics/bin/Programs/turnstile_weather_v2.csv'

def read_file(csv_file):
	df = pandas.read_csv(csv_file) #makes a dataframe
	return df


def stat_stuff(turnstile_weather):
	#perform statistical operations based on my answers to problem set 3
	wrain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 1]
	woutrain = turnstile_weather['ENTRIESn_hourly'][turnstile_weather['rain'] == 0]
	with_rain_mean = numpy.mean(wrain)
	without_rain_mean = numpy.mean(woutrain)
	
	results = scipy.stats.mannwhitneyu(wrain, woutrain, use_continuity=True)
	
	U = results[0]
	p = results[1]
	
	return with_rain_mean, without_rain_mean, U, p
	
def OLS_regression(features, values): #with help from http://statsmodels.sourceforge.net/devel/generated/statsmodels.regression.linear_model.RegressionResults.html
	#same code as in lesson3 exercise, because it worked. 
	features = sm.add_constant(features)
	model = sm.OLS(values, features)
	results = model.fit()
	r2 = results.rsquared
	intercept = results.params[0]
	params = results.params[1:]
	return intercept, params, r2
	
def predictions(df):
	#possible features:'rain', 'precipi', 'hour', 'fog', 'minpressurei', 'meanpressurei', 'maxpressurei', 'meandewpti', 'maxdewpti', 'mintempi', 'datetime', 'day_week', 'weekday', 'station', 'latitute', 'longitude', 'conds', 'wspdi', 'weather_lat', 'weather_lon'
	features = df[["weekday", "hour", "latitude", "longitude", "precipi", "fog", 'rain', 'meanpressurei']]
	dummy_unit = pandas.get_dummies(df['UNIT'], prefix='unit')
	dummy_conds = pandas.get_dummies(df["conds"], prefix="condi")
	dummy_station = pandas.get_dummies(df["station"], prefix="Station")
	features = features.join(dummy_unit)
	features = features.join(dummy_conds)
	features = features.join(dummy_station)
	# Values
	values = df['ENTRIESn_hourly']
	# Perform linear regression - do not call OLS regression again in main! it is already here
	intercept, params, r2 = OLS_regression(features, values)
	
	predictions = intercept + numpy.dot(features, params)
	return predictions, r2, params




def main(csv_file):
	#put it all together!

	#make it a df
	data = read_file(csv_file)
	#test it!
	xmean, ymean, U, p = stat_stuff(data)
	#is it significant?
	if p < .025:
		result= True
		print "P-result =", p, " At a one-tailed alpha level of 5%, the statistical analysis is significant."
	else:
		result= False
		print "P-result =", p, " At a one-tailed alpha level of 5%, the statistical analysis is not significant."

	#regression!
	pred, r2, params = predictions(data)
	plt.figure() #residual plot used in report
	(data['ENTRIESn_hourly'] - pred).hist(bins = 1000)
	plt.title("Histogram: Residuals of the regression: Observed - Predicted")
	plt.xlabel("Residual Amount")
	plt.ylabel("Frequency")
	plt.show()
	
	print "The mean hourly entries with rain was:", xmean, "The mean hourly entries without rain was:", ymean, "R^2 value =", r2, " Coefficients: ", params
	return xmean, ymean, plt, r2, result
	
main(datastuff)	
