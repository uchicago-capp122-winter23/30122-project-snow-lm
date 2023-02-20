'''
CAPP 30122
Team: Snow Laughing Matter
Code for querying the U.S. Census' API
'''

import re
import pathlib
import pandas as pd
import requests
#anything else we need to import?

#Assemble components of this query by following these steps:
#1. Start query with the host name:
host_name = "https://api.census.gov/data"
query_url = host_name

#2. Add the data year to the query:
#https://api.census.gov/data/2021
data_year = "/2021"
query_url += data_year

#3. Add the dataset name acronym:
#https://api.census.gov/data/2019/acs/acs5
dataset_name_acronym = "/acs/acs5/profile"
query_url += dataset_name_acronym

#4. Add ?get= to the query:
#https://api.census.gov/data/2021/acs/acs5/profile?get=
get = "?get="
query_url += get

#5. Add variables:
list_of_vars = "NAME,DP02_0001E,DP02PR_0001E,DP03_0001E,DP03_0051E,DP03_0095E,DP02_0058E,DP05_0033E" #IS THIS LIST COMPLETE?
query_url += list_of_vars

'''
See below for descriptions of each variable:
#NAME = name of location
#DP02_0001E = total households
#DP02PR_0001E = total households in puerto rico - cut this one?
#DP03_0001E = employment (employment rate); Estimate!!EMPLOYMENT STATUS!!Population 16 years and over
#DP03_0051E = income and poverty (median household income); Estimate!!INCOME AND BENEFITS (IN 2018 INFLATION-ADJUSTED DOLLARS)!!Total households
#DP03_0095E = health (without health care coverage); Estimate!!HEALTH INSURANCE 
#DP02_0058E = education (bachelor's degree or higher); Estimate!!EDUCATIONAL ATTAINMENT!!Population 25 years and over
#DP05_0033E = Estimate!!RACE!!Total population
#additional geocodes???
'''

#6. Add geographies:
geo = "&for=county:*"
query_url += geo

#7. Add census API key for this project:
census_api_key = "&key=dbaf6b8c0aa053d4df5ae844bba98940952fc50b"
query_url += census_api_key

#Request data using the full query url:
response = requests.get(query_url)
census_json = response.json()

#Save census data to a pandas dataframe:
#census_df = 

#Cleaning variable names in the df 
#(e.g., it would be nice if the variables had descriptive variable names):


#Checking variable types and making any revisions necessary:


#Save df to CSV:

