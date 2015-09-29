##Continuation of Project 2
##Testing a lot of graphs in this one to select the most accurate predictors and strongest correlations
##
##
##
##Author: Casey Faist

import seaborn
import matplotlib.pyplot as plt
import pandas
import numpy
import scipy
import scipy.stats

#where I saved the csv file
csv = '/Users/Casey/miniconda3/envs/datagraphics/bin/Programs/turnstile_weather_v2.csv'


headers = ['UNIT', 'DATEn', 'ENTRIESn', 'EXITSn', 'ENTRIESn_hourly', 'EXITSn_hourly', 'datetime', 'hour', 'day_week', 'weekday', 'station', 'latitude', 'longitude', 'conds', 'fog', 'precipi', 'pressurei', 'rain', 'tempi', 'wspdi', 'meanprecipi', 'meanpressurei', 'meantempi', 'meanwspdi', 'weather_lat', 'weather_lon']

df = pandas.read_csv(csv)




plt.figure() #Histogram used in report
seaborn.distplot(df["ENTRIESn_hourly"][df['rain']==1], kde=False, bins=1000) #from http://stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html, http://stanford.edu/~mwaskom/software/seaborn-dev/generated/seaborn.distplot.html
seaborn.distplot(df["ENTRIESn_hourly"][df['rain']==0], kde=False, bins=1000)
plt.xlabel("Number of Entries -- Green:No Rain, Blue:Rain") #from http://matplotlib.org/users/text_intro.html
plt.ylabel("Frequency")
plt.suptitle('Histogram of Hourly Entries with rain and without')
plt.show()

plt.figure() #plot of conditions vs. entries used in report
seaborn.barplot(x="ENTRIESn_hourly", y='conds', data=df, palette="Blues_d", linewidth = .05) # from http://stanford.edu/~mwaskom/software/seaborn/generated/seaborn.barplot.html
plt.xlabel("Number of Entries")
plt.ylabel("Weather Conditions")
plt.suptitle('Entries by Local Weather Condition')
plt.show()


plt.figure() #graph of entries by different hours rain vs no rain, used in report
seaborn.barplot(x='hour', y='ENTRIESn_hourly', hue = 'rain', data=df.sort('hour')) #from http://stanford.edu/~mwaskom/software/seaborn/tutorial/categorical.html
plt.xlabel("Hour")
plt.ylabel("Number of Entries")
plt.suptitle('Entries Per Hour by Rain')
plt.show()

plt.figure() # weekday rain/nonrain vs weekend rain/nonrain ridership, used in report
seaborn.barplot(x='weekday', y='ENTRIESn_hourly', hue='rain', data=df)
plt.suptitle('Ridership Per Day Per Hour, No Rain')
plt.xlabel("Non-Weekdays (0) vs Weekdays (1)")
plt.ylabel('Average Hourly Entries')
plt.show()


#Playing with a map comparing ridership increases during different weather conditions animation - for later playing with
#plt.figure() #attempted longitude/latitude heat map! http://stanford.edu/~mwaskom/software/seaborn/tutorial/color_palettes.html#qualitative-color-palettes
#seaborn.jointplot(x='longitude', y='latitude', hue='ENTRIESn_hourly', data=df, kind='kde') #http://stanford.edu/~mwaskom/software/seaborn/tutorial/distributions.html#plotting-bivariate-distributions
#plt.show()


#
#These graphs were helpful to both learn seaborn and explore the data's relevant predictors, but were not used in the report.
#

new = df[df['rain']==1]
newn = df[df['rain']==0]

hour1 = df[df['hour']==0]
hour2 = df[df['hour']==4]
hour3 = df[df['hour']==8]
hour4 = df[df['hour']==12]
hour5 = df[df['hour']==16]
hour6 = df[df['hour']==20]

plt.figure()
seaborn.barplot(x='day_week', y="ENTRIESn_hourly", hue='hour', data=new.sort("day_week"))
plt.suptitle('Ridership Per Day Per Hour, With Rain')
plt.xlabel("Days of the Week")
plt.ylabel('Hourly Entries per Unit')
plt.show()

plt.figure()
seaborn.barplot(x='day_week', y='ENTRIESn_hourly', hue='hour', data=newn.sort('day_week'))
plt.suptitle('Ridership Per Day Per Hour, No Rain')
plt.xlabel("Days of the Week")
plt.ylabel('Hourly Entries per Unit')
plt.show()

plt.figure()
seaborn.barplot(x='day_week', y="ENTRIESn_hourly", hue='rain', data=df, palette = "BuGn_r")
plt.suptitle('Ridership Per Day, Rain vs No Rain')
plt.xlabel("Days of the Week")
plt.ylabel('Hourly Entries per Unit')
plt.show()

#All these charts go together; palette help from http://chrisalbon.com/python/seaborn_color_palettes.html
plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour1.sort("day_week"), palette="Reds")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 0")
plt.ylabel("Number of Entries")
plt.show()

plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour2.sort("day_week"), palette="YlOrBr")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 4")
plt.ylabel("Number of Entries")
plt.show()

plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour3.sort("day_week"), palette="Greens")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 8")
plt.ylabel("Number of Entries")
plt.show()

plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour4.sort("day_week"), palette="BuGn")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 12")
plt.ylabel("Number of Entries")
plt.show()

plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour5.sort("day_week"), palette="Blues")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 16")
plt.ylabel("Number of Entries")
plt.show()

plt.figure()
seaborn.barplot(x="day_week", y="ENTRIESn_hourly", hue='rain', data=hour6.sort("day_week"), palette="Purples")
plt.suptitle("Hourly Ridership per day, rain vs no rain")
plt.xlabel("Day of the Week - Hour 20")
plt.ylabel("Number of Entries")
plt.show()
