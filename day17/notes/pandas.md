# Pandas

- data analytics library
- installation
  - pip install pandas
- importing panads
  - import pandas as pd

- data types
  - series
  - data frame

## series

- 1d array implemented by pandas
- behind the scene the series uses numpy ndarray
- every value in series gets stored on specific index position
- creating a series object using list or tuple would create index positions automatically (integer index positions)
- creating a series object using dictionary would store values of dictionary in series using dictionary keys as index positions

## data frame

- 2d array implemented by pandas
- uses multiple series objects as columns
- every column in a dataframe is made up using a series object
- represents a tabular data structure
- methods
  - head(): used to get first 5 rows
  - head(n): used to get first n rows
  - tail(): used to get last 5 rows
  - tail(n): used to get last n rows
  - info(): used to get general information
  - describe(): used to get statistical information
  - iloc[row, column]: used to get data at rowth and columnth position
- NaN
  - not a number
  - value at this position is missing
  - also known as NA value
