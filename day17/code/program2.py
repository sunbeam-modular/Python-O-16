import numpy as np
import pandas as pd

def function1():
    # create a data frame using a list
    # note: this will create a df with size: 5x1 
    df1 = pd.DataFrame([10, 20, 30, 40, 50])
    print(df1)
    print('-' * 80)

    # create a data frame using a tuple
    # note: this will create a df with size: 5x1 
    df2 = pd.DataFrame((10, 20, 30, 40, 50))
    print(df2)
    print('-' * 80)

    # create a data frame using a dictionary
    # note: this will create a df with size: 3x4 
    df3 = pd.DataFrame({
        'name': ['alice', 'bob', 'charlie'],
        'age': [20, 40, 60],
        'salary': [10, 20, 30],
        'city': ['pune', 'mumbai', 'satara']
    })
    print(df3)
    print('-' * 80)

    # create data frame using list of lists
    # note: this will create a df with size: 3x4
    df4 = pd.DataFrame([
        ['alice', 20, 10, 'pune'],
        ['bob', 30, 20, 'mumbai'],
        ['charlie', 60, 30, 'satara'],
    ])
    print(df4)
    print('-' * 80)

    # create data frame using list of lists with column names
    # note: this will create a df with size: 3x4
    df5 = pd.DataFrame([
        ['alice', 20, 10, 'pune'],
        ['bob', 30, 20, 'mumbai'],
        ['charlie', 60, 30, 'satara'],
    ], columns=['name', 'age', 'salary', 'city'])
    print(df5)
    print('-' * 80)

# function1()

def function2():
    # read data from a csv file
    df = pd.read_csv('./50_startups.csv')
    # print(df)
    # print('-' * 80)

    # basic attributes
    print(f"#dimensions       = {df.ndim}")
    print(f"shape             = {df.shape}")
    print(f"columns           = {df.columns}")
    print('-' * 80)

    # first 5 rows 
    print(df.head())
    print('-' * 80)

    # first 10 rows
    print(df.head(10))
    print('-' * 80)

    # last 5 rows
    print(df.tail())
    print('-' * 80)

    # last 10 rows
    print(df.tail(10))
    print('-' * 80)

    # find the general information about the df
    df.info()
    print('-' * 80)

    # get statistical information about the df
    print(df.describe())

# function2()

def function3():
    # read data from a csv file
    df = pd.read_csv('./50_startups.csv')

    # read a single column
    # since, in df, every column is created using a series
    # these statements will return a series object
    # print(df['Administration'])
    # print(df.Administration)

    # read multiple columns
    # this statement will return a dataframe with multiple columns
    # print(df[['Administration', 'State']])

    # read the first row: returns a series object
    # print(df.head(1))
    # print(df.iloc[0])

    # read multiple rows
    # print(df.iloc[0:5])
    # print(df.iloc[:5])

    # find multiple rows along with selected columns (RnD)
    # print(df.iloc[0:5, 0])

    # update any value using row and column position
    # df.iloc[0, 0] = "new value"

    # find multiple rows along with selected columns (RnD, Administration)
    # print(df.iloc[0:5, 0:2])

# function3()

def function4():
    # read data from a csv file
    df = pd.read_csv('50_startups.csv')

    # find the startups from California state
    # print(df.query("State == 'California'"))

    # find the startups from California and Florida state
    # print(df.query("State == 'California' or 'Florida'"))
    # print(df[df['State'].isin(['California', 'Florida'])])

    # find the startups having RnD budget > 100671
    # print(df.query('RnD > 100000'))

# function4()

def function5():
    df = pd.DataFrame({
        'name': ['alice', 'bob', 'charlie'],
        'age': [20, 40, 60],
        'salary': [10, 20, 30],
        'city': ['pune', 'mumbai', 'satara']
    })

    print(df)
    print('-' * 80)

    # overwrite the existing values
    # if the column exists, the values will be overwritten
    df['salary'] = [30, 40, 50]

    # add a new column with explicit values
    df['email'] = ['alice@test.com', 'bob@test.com', 'charlie@test.com']
    print(df)
    print('-' * 80)

    # add a new column using existing one
    # - add new column named "bonus" using salary column
    # - every salary value will generate the bonus value
    # df['bonus'] = df['salary'] * 0.10
    df['bonus'] = df['salary'].apply(lambda s: s * 0.10)
    print(df)
    print('-' * 80)

    # add a new_salary based on existing salary + bonus
    df['new_salary'] = df['bonus'] + df['salary']
    print(df)
    print('-' * 80)

# function5()

def function6():
    df = pd.DataFrame({
        'name': ['alice', 'bob', 'charlie'],
        'age': [20, 40, 60],
        'salary': [10, 20, 30],
        'city': ['pune', 'mumbai', 'satara']
    })

    print(df)
    print('-' * 80)

    # remove city columns
    # note: using del keyword only one column can be removed from the df
    # del df['city']

    # axis = 0: row
    # axis = 1: column
    # note: by default, drop() does not modify the df, 
    #  rather it returns a new df with column removed
    df = df.drop('city', axis=1)

    # by passng inplace, drop will modify the same df
    # df.drop('city', axis=1, inplace=True)

    # remove multiple columns from df
    # df.drop(['city', 'salary'], axis=1, inplace=True)

    # remove the row with 0 index
    # df.drop(0, axis=0, inplace=True)

    # rename column salary to 'CTC'
    df.rename({'salary': 'CTC'}, axis=1, inplace=True)
    print(df)
    print('-' * 80)

    # save the current state of df to a file
    df.to_csv('new_data.csv')

function6()

def function7():
    # read the titanic data
    df = pd.read_csv('./titanic.csv')
    # print(df)

    # get the general information about the df
    # df.info()

    # read first 5 records
    # print(df.head())

    # check if the df has any NaN values
    # print(df.isna())
    # print(df.isna().sum())

    # remove columns having NaN values
    # note: even if a single value is missing (NaN) in a column,
    #   that column gets removed
    # print(df.columns)
    # df.dropna(axis=1, inplace=True)
    # print(df.columns)

    # remove rows having NaN values
    # note: even if a single value is missing (NaN) in a row,
    #   that row gets removed
    # print(df.shape)
    # df.dropna(axis=0, inplace=True)
    # print(df.shape)

    # impute or replace the NA value with replacement value
    # statistical approach:
    # - replace the NA values with mean/mode/median
    # print(df['body'])
    # print(df['body'].fillna('replacement_value'))

    # impute or replace the NA value with mean value of age
    print(df['age'].fillna(df['age'].mean()))

# function7()