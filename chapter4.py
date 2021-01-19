####################
####################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

###################
###################
dog_pack["height_cm"].hist()


###################
###################

dog_pack["height_cm"].hist(bins=20)
plt.show()

###################
# barplot
# .plot(kind="bar")
# title argument


# line plots
# sully.head()
# sully.plot(x = "date", y = "weight_kg", kind = "line", rot = 45)

# scatter plots
# kind = "scatter"


# layering plots
# add a legend
# plt.legend()
# plt.show()
# make histogram translucent (alpha)
#

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Look at the first few rows of data
print(avocados.head())

# Get the total number of avocados sold of each size
nb_sold_by_size = avocados.groupby("size")["nb_sold"].sum()

# Create a bar plot of the number of avocados sold by size
nb_sold_by_size.plot(kind="bar")

# Show the plot
plt.show()

#
# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date")["nb_sold"].sum()

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="date", y = "", kind="line")

# Show the plot
plt.show()

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Get the total number of avocados sold on each date
nb_sold_by_date = avocados.groupby("date", as_index = False).agg({"nb_sold": "sum"})

# Create a line plot of the number of avocados sold by date
nb_sold_by_date.plot(x="date", y = "nb_sold", kind="line")

# Show the plot
plt.show()

# Scatter plot of nb_sold vs avg_price with title
avocados.plot(y = "avg_price", x = "nb_sold", kind = "scatter", title = "Number of avocados sold vs. average price")

# Show the plot
plt.show()



### Missing values
### dogs.isna()
### dogs.isna().any() # if any missing values in the column
### dogs.isna().sum()
### can use counts to visualize missing values using a barplot
### dogs.fillna(0)
###

# Removing missing values
#
# Now that you know there are some missing values in your DataFrame, you have a few options to deal with them. One way is to remove them from the dataset completely. In this exercise, you'll remove missing values by removing all rows that contain missing values.
#
# pandas has been imported as pd and avocados_2016 is available.

# Remove rows with missing values
avocados_complete = avocados_2016.dropna()

# Check if any columns contain missing values
print(avocados_complete.isna().any())



### Creating DataFrames
###

### Dictionaries
### hold a set of key-value pairs
###
my_dict = {"key1": value1,
           "key2": value2,
           "key3": value3}

### from a list of dictionaires
### from a dictionary of lists

### list of dictionaries
### each key will become a column name
### pd.DataFrame()
### print()

### dictionary of lists
### dict_of_lists = { "name": ["Ginger", "Scout"],
# ...,
# ..., ...}

# pd.DataFrame()
#

# Create a list of dictionaries with new data
avocados_list = [
    {"date": "2019-11-03", "small_sold": 10376832, "large_sold": 7835071},
    {"date": "2019-11-10", "small_sold": 10717154, "large_sold": 8561348},
]

# Convert list into DataFrame
avocados_2019 = pd.DataFrame(avocados_list)

# Print the new DataFrame
print(avocados_2019)


#
# Create a dictionary of lists with new data
avocados_dict = {
  "date": ["2019-11-17", "2019-12-01"],
  "small_sold": [10859987, 9291631],
  "large_sold": [7674135, 6238096]
}

# Convert dictionary into DataFrame
avocados_2019 = pd.DataFrame(avocados_dict)

# Print the new DataFrame
print(avocados_2019)


# Reading and writing CSVs
# CSV file, comma separated values
# most database and spreadsheet can use csv
#

# pd.read_csv()
# to_csv() # pass a new file path
#

# From previous steps
airline_bumping = pd.read_csv("airline_bumping.csv")
print(airline_bumping.head())
airline_totals = airline_bumping.groupby("airline")[["nb_bumped", "total_passengers"]].sum()
airline_totals["bumps_per_10k"] = airline_totals["nb_bumped"] / airline_totals["total_passengers"] * 10000

# Print airline_totals
print(airline_totals)


# recap
# chapter 1: subsetting and sorting, adding new columns
# chapter 2: aggregating and grouping, summary statistics
# chapter 3: indexing and slicing
# chapter 4: visualizations, reading and writing CSVs

# more to learn
# joining data with pandas
# streamlined data ingesting with pandas