###### notes for chapter 1
###### https://learn.datacamp.com/courses/data-manipulation-with-pandas
###### pandas

import pandas as pd

# seaborn for datasets
import seaborn as sns

####### Data manipulation
####### Data visualization

####### chapter 1, DataFrames
####### chapter 2, Aggregating Data
####### chapter 3, Slicing and Indexing Data
####### chapter 4, Creating and Visualizing Data

####### pandas is built on NumPy and Matplotlib
####### pandas is popular, entire python data science community


####### rectangular data
####### print(dogs)

####### dogs.head()
####### dogs.info()
####### dogs.shape
####### dogs.describe() -- summary statistics, quick overview of numerical variables
####### dogs.values -- returns the data in a 2 dimensional numpy array
####### dogs.columns
####### dogs.index
####### Zen of Python
####### a variety of tools



######## streamlined python


######## Exercise 1
# Inspecting a DataFrame
#
# When you get a new DataFrame to work with, the first thing you need to do is explore it and see what it contains. There are several useful methods and attributes for this.
#
#     .head() returns the first few rows (the “head” of the DataFrame).
#     .info() shows information on each of the columns, such as the data type and number of missing values.
#     .shape returns the number of rows and columns of the DataFrame.
#     .describe() calculates a few summary statistics for each column.
#
# homelessness is a DataFrame containing estimates of homelessness in each U.S. state in 2018. The individual column is the number of homeless individuals not part of a family with children. The family_members column is the number of homeless individuals part of a family with children. The state_pop column is the state's total population.
#
# pandas is imported for you.

iris = sns.load_dataset('iris')
iris.head()
# Print the head of the homelessness data
print(iris.head())

# Print information about homelessness
print(iris.info())

# Print the shape of homelessness
print(iris.shape)

# Print a description of homelessness
print(iris.describe())


# Parts of a DataFrame
#
# To better understand DataFrame objects, it's useful to know that they consist of three components, stored as attributes:
#
#     .values: A two-dimensional NumPy array of values.
#     .columns: An index of columns: the column names.
#     .index: An index for the rows: either row numbers or row names.
#
# You can usually think of indexes as a list of strings or numbers, though the pandas Index data type allows for more sophisticated options. (These will be covered later in the course.)
#
# homelessness is available.

# sorting and subsetting
#
# dogs.sort_values("weight_kg")
# dogs.sort_values("weight_kg", ascending = False)
# dogs.sort_values()

# subsetting multiple columns
# subsetting rows dogs[""] > 50
# subsetting rows subsetting rows based on text data
# subsetting based on dates "2015-01-01" (international standard date format)
# subsetting using .isin()

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())


#
# Filter for rows where family_members is less than 1000
# and region is Pacific
fam_lt_1k_pac = homelessness[ (homelessness["family_members"] < 1000) & (homelessness["region"] == "Pacific") ]

# See the result
print(fam_lt_1k_pac)


# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[ homelessness["region"].isin(["South Atlantic", "Mid-Atlantic"]) ]

# See the result
print(south_mid_atlantic)

# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness["state"].isin(canu)]

# See the result
print(mojave_homelessness)



########################################
# new columns
# mutate
# transforming
# feature engineering

# dogs["height_m"] = dogs["height_cm"] / 100

# doggy mass index , weight in kg / (height in m)^2
# dogs["bmi"] =


# multiple manipulations
# bmi_lt_100 = dogs[dogs["bmi"] < 100]

# #
# Adding new columns
#
# You aren't stuck with just the data you are given. Instead, you can add new columns to a DataFrame. This has many names, such as transforming, mutating, and feature engineering.
#
# You can create new columns from scratch, but it is also common to derive them from other columns, for example, by adding columns together or by changing their units.
#
# homelessness is available and pandas is loaded as pd.

# Add total col as sum of individuals and family_members
homelessness["total"] = homelessness["individuals"] + homelessness["family_members"]

# Add p_individuals col as proportion of individuals
homelessness["p_individuals"] = homelessness["individuals"] / homelessness["total"]

# See the result
print(homelessness)

##

# Combo-attack!
#
# You've seen the four most common types of data manipulation: sorting rows, subsetting columns, subsetting rows, and adding new columns. In a real-life data analysis, you can mix and match these four manipulations to answer a multitude of questions.
#
# In this exercise, you'll answer the question, "Which state has the highest number of homeless individuals per 10,000 people in the state?" Combine your new pandas skills to find out.

#
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness["individuals"] / homelessness["state_pop"]

# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"] > 20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values("indiv_per_10k", ascending = False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[["state", "indiv_per_10k"]]

# See the result
print(result)


