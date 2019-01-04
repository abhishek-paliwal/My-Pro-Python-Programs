#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 16:48:06 2019

@author: abhishek

ABOUT:
This program merges two CSV files which have a common column.
It will do a left-merge, meaning it will take all columns of left file, and
only the matching rows of the right file.

Then, it will remove some rows with unwanted values.
    
"""

# %% Importing pandas, and then converting two csv files into dataframes
import pandas as pd

lt = pd.read_csv("1_mggk_mysql_category_id_table.csv")
rt = pd.read_csv("2_mggk_mysql_category_names_slugs_table.csv")


# %% Left merge: Keep everything from the left, drop things from the
# right (if they don't match)
df = pd.merge(left=lt, right=rt, on="catid", how="left")
df.head() # prints the top 5 rows

# %% Removing some rows with given values

# Initializing a list with all values we want removed later
donottake = ["branding" , "uncategorized" , "free-downloads" , "all-recipes", 
             "food-photography" , "videos" ]

# 
df1 = df # copying the dataframe
count=0 
# Looping through the dataframe to exlude all matching values
for i in donottake:
    print(i)
    df1 = df1[df1.catslug != str(i) ] # exlude rows where any value = i ; include all others
    count = count+1
    print(count)

print(df1.head())    

# %% Sorting the dataframe, then creating another dataframe with only the
# desired columns.
df2 = df1.sort_values(by='catslug')   
df2 = df2[['catid', 'catname', 'catslug']]  

## Transforming catname values to uppercase
df2['catname_upper']  = df2['catname'].str.upper()
df2['catname_lower']  = df2['catname'].str.lower()

# Adding a htmlvalue column from other column values
df2['htmlvaluecol'] = str("<h4 id='") + df2['catslug'] + str("'><a href='https://www.mygingergarlickitchen.com/category/")  + df2['catslug'] + str("/'>") + df2['catname_upper']  + str("</a> (<a href='https://www.mygingergarlickitchen.com/all-recipes-list/'> &uarr; Go to Top) </h4>") + str("[catlist name=") + df2['catslug'] + str(" numberposts=2000]")

# Adding a htmlTOCcol column from other column values
df2['htmlTOCcol'] = str("<li style='background : #e8e8e8; margin: 5px; padding: 5px; '><a style='text-transform: capitalize; ' href='#")  + df2['catslug'] + str("'>") + df2['catname_lower']  + str("</a></li>")

# %% Finally creating the final dataframes
df31 = df2[['htmlvaluecol']]
df311 = df31.apply('\n'.join) ## converts whole column into a single string joined by \n

# Creating dataframe column, then converting to series
df32 = df2[['htmlTOCcol']]
df321 = df32.apply('\n'.join) ## converts whole column into a single string joined by \n
df322 = str("<h3>Complete Recipe List with Categories (A-Z)</h3> <ol>") + df321 + str("</ol> <hr>")

print(df311)
print(df322)

# %% Creating the final csv file (for comfort, we are renaming it directly as HTML file)
df31.to_csv('output_final_1.html', encoding='utf-8', header=None, index=False)
df322.to_csv('output_final_2.html', encoding='utf-8', header=None, index=False)

##################################################
## PROGRAM ENDS 
##################################################
