---
title: Customer Analysis
keywords: [Customer Analysis, Data Visualization, Matplotlib, Pandas, Opendatasets]
description: In this notebook, I want to observe any trends related to customers.
author: Juma Shafara
date: "2024-07-08"
--- 

---
In this project, I want to look at customer data pulled from github and create some visuals in my jupyter notebook to observe any trends related to customers.

<!-- Newsletter -->
<div style="background-color: #008374; border:1px solid #008374; color: #fff; font-weight: 700; padding-left: 10px; padding-top: 5px; padding-bottom: 5px"><strong>Don't Miss Any Updates!</strong></div>
<div style="background-color: #f3f4f7; padding-left: 10px; padding-top: 10px; padding-bottom: 10px; padding-right: 10px">

<p style="color:rgb(36, 36, 36)">
Before we continue, we have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
 (formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>

<iframe src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no" style="margin: 0; border-radius: 0px !important; background-color: transparent; width: 100%;" ></iframe>
</div>


## Downloading the Dataset:

First we download our data sets from github.


```python
!pip install dataidea --upgrade --quiet
```


```python
import opendatasets as od

# download the dataset
dataset_url = 'https://raw.githubusercontent.com/Kaushik-Varma/Marketing_Data_Analysis/master/Marketing_Analysis.csv'
od.download(dataset_url)
```

    Using downloaded and verified file: ./Marketing_Analysis.csv


## Data Preparation and Cleaning

Get our dataset into a data frame, examine the tables to check for incorrect, inconsistent, or invalid entries. Handle other cleaning steps as necessary.


```python
#import the useful libraries.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read the data set of "Marketing Analysis" in data.
data= pd.read_csv("Marketing_Analysis.csv", low_memory=False)

# Printing the data
data.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>banking marketing</th>
      <th>Unnamed: 1</th>
      <th>Unnamed: 2</th>
      <th>Unnamed: 3</th>
      <th>Unnamed: 4</th>
      <th>Unnamed: 5</th>
      <th>Unnamed: 6</th>
      <th>Unnamed: 7</th>
      <th>Unnamed: 8</th>
      <th>Unnamed: 9</th>
      <th>Unnamed: 10</th>
      <th>Unnamed: 11</th>
      <th>Unnamed: 12</th>
      <th>Unnamed: 13</th>
      <th>Unnamed: 14</th>
      <th>Unnamed: 15</th>
      <th>Unnamed: 16</th>
      <th>Unnamed: 17</th>
      <th>Unnamed: 18</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>customer id and age.</td>
      <td>NaN</td>
      <td>Customer salary and balance.</td>
      <td>NaN</td>
      <td>Customer marital status and job with education...</td>
      <td>NaN</td>
      <td>particular customer before targeted or not</td>
      <td>NaN</td>
      <td>Loan types: loans or housing loans</td>
      <td>NaN</td>
      <td>Contact type</td>
      <td>NaN</td>
      <td>month of contact</td>
      <td>duration of call</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>outcome of previous contact</td>
      <td>response of customer after call happned</td>
    </tr>
    <tr>
      <th>1</th>
      <td>customerid</td>
      <td>age</td>
      <td>salary</td>
      <td>balance</td>
      <td>marital</td>
      <td>jobedu</td>
      <td>targeted</td>
      <td>default</td>
      <td>housing</td>
      <td>loan</td>
      <td>contact</td>
      <td>day</td>
      <td>month</td>
      <td>duration</td>
      <td>campaign</td>
      <td>pdays</td>
      <td>previous</td>
      <td>poutcome</td>
      <td>response</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>58</td>
      <td>100000</td>
      <td>2143</td>
      <td>married</td>
      <td>management,tertiary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>261 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>44</td>
      <td>60000</td>
      <td>29</td>
      <td>single</td>
      <td>technician,secondary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>151 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>33</td>
      <td>120000</td>
      <td>2</td>
      <td>married</td>
      <td>entrepreneur,secondary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>76 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>



## Cleaning the Data

Here we need to fix some of the columns/rows to make the data easier to use.


```python
#import the useful libraries.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Read the file in data without first two rows as it is of no use.
data = pd.read_csv("Marketing_Analysis.csv",skiprows = 2)

#print the head of the data frame.
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>customerid</th>
      <th>age</th>
      <th>salary</th>
      <th>balance</th>
      <th>marital</th>
      <th>jobedu</th>
      <th>targeted</th>
      <th>default</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
      <th>month</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>poutcome</th>
      <th>response</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>58.0</td>
      <td>100000</td>
      <td>2143</td>
      <td>married</td>
      <td>management,tertiary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>261 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>44.0</td>
      <td>60000</td>
      <td>29</td>
      <td>single</td>
      <td>technician,secondary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>151 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>33.0</td>
      <td>120000</td>
      <td>2</td>
      <td>married</td>
      <td>entrepreneur,secondary</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>yes</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>76 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>47.0</td>
      <td>20000</td>
      <td>1506</td>
      <td>married</td>
      <td>blue-collar,unknown</td>
      <td>no</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>92 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>33.0</td>
      <td>0</td>
      <td>1</td>
      <td>single</td>
      <td>unknown,unknown</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>unknown</td>
      <td>5</td>
      <td>may, 2017</td>
      <td>198 sec</td>
      <td>1</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Drop the customer id as it is of no use.
data.drop('customerid', axis = 1, inplace = True)

#Extract job  & Education in newly from "jobedu" column.
data['job']= data["jobedu"].apply(lambda x: x.split(",")[0])
data['education']= data["jobedu"].apply(lambda x: x.split(",")[1])

# Drop the "jobedu" column from the dataframe.
data.drop('jobedu', axis = 1, inplace = True)

# Printing the Dataset
data.sample(n=5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>age</th>
      <th>salary</th>
      <th>balance</th>
      <th>marital</th>
      <th>targeted</th>
      <th>default</th>
      <th>housing</th>
      <th>loan</th>
      <th>contact</th>
      <th>day</th>
      <th>month</th>
      <th>duration</th>
      <th>campaign</th>
      <th>pdays</th>
      <th>previous</th>
      <th>poutcome</th>
      <th>response</th>
      <th>job</th>
      <th>education</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>7369</th>
      <td>28.0</td>
      <td>60000</td>
      <td>1180</td>
      <td>married</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>29</td>
      <td>may, 2017</td>
      <td>637 sec</td>
      <td>3</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
      <td>technician</td>
      <td>secondary</td>
    </tr>
    <tr>
      <th>31281</th>
      <td>44.0</td>
      <td>100000</td>
      <td>483</td>
      <td>single</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>6</td>
      <td>mar, 2017</td>
      <td>3.45 min</td>
      <td>2</td>
      <td>199</td>
      <td>6</td>
      <td>success</td>
      <td>yes</td>
      <td>management</td>
      <td>tertiary</td>
    </tr>
    <tr>
      <th>736</th>
      <td>40.0</td>
      <td>20000</td>
      <td>-7</td>
      <td>married</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>6</td>
      <td>may, 2017</td>
      <td>410 sec</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
      <td>blue-collar</td>
      <td>primary</td>
    </tr>
    <tr>
      <th>45207</th>
      <td>71.0</td>
      <td>55000</td>
      <td>1729</td>
      <td>divorced</td>
      <td>yes</td>
      <td>no</td>
      <td>no</td>
      <td>no</td>
      <td>cellular</td>
      <td>17</td>
      <td>nov, 2017</td>
      <td>7.6 min</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>yes</td>
      <td>retired</td>
      <td>primary</td>
    </tr>
    <tr>
      <th>6297</th>
      <td>53.0</td>
      <td>60000</td>
      <td>6</td>
      <td>married</td>
      <td>yes</td>
      <td>no</td>
      <td>yes</td>
      <td>no</td>
      <td>unknown</td>
      <td>27</td>
      <td>may, 2017</td>
      <td>233 sec</td>
      <td>2</td>
      <td>-1</td>
      <td>0</td>
      <td>unknown</td>
      <td>no</td>
      <td>self-employed</td>
      <td>primary</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Checking the missing values
data.isnull().sum()
```




    age          20
    salary        0
    balance       0
    marital       0
    targeted      0
    default       0
    housing       0
    loan          0
    contact       0
    day           0
    month        50
    duration      0
    campaign      0
    pdays         0
    previous      0
    poutcome      0
    response     30
    job           0
    education     0
    dtype: int64




```python
# Dropping the records with age missing in data dataframe.
data = data[~data.age.isnull()].copy()

# Checking the missing values in the dataset.
data.isnull().sum()
```




    age           0
    salary        0
    balance       0
    marital       0
    targeted      0
    default       0
    housing       0
    loan          0
    contact       0
    day           0
    month        50
    duration      0
    campaign      0
    pdays         0
    previous      0
    poutcome      0
    response     30
    job           0
    education     0
    dtype: int64




```python
# Find the mode of month in data
month_mode = data.month.mode()[0]

# Fill the missing values with mode value of month in data.
data.month.fillna(month_mode, inplace = True)

# Let's see the null values in the month column.
data.month.isnull().sum()
```

    /tmp/ipykernel_39902/3697544734.py:5: FutureWarning: A value is trying to be set on a copy of a DataFrame or Series through chained assignment using an inplace method.
    The behavior will change in pandas 3.0. This inplace method will never work because the intermediate object on which we are setting values always behaves as a copy.
    
    For example, when doing 'df[col].method(value, inplace=True)', try using 'df.method({col: value}, inplace=True)' or df[col] = df[col].method(value) instead, to perform the operation inplace on the original object.
    
    
      data.month.fillna(month_mode, inplace = True)





    0




```python
#drop the records with response missing in data.
data = data[~data.response.isnull()].copy()
# Calculate the missing values in each column of data frame
data.isnull().sum()
```




    age          0
    salary       0
    balance      0
    marital      0
    targeted     0
    default      0
    housing      0
    loan         0
    contact      0
    day          0
    month        0
    duration     0
    campaign     0
    pdays        0
    previous     0
    poutcome     0
    response     0
    job          0
    education    0
    dtype: int64



## Exploratory Analysis and Visualization

Now we apply some data manipulation steps and explore some of the findings through the use of visuals. Hopefully we can then gain some useful insights from our data. 

## What kind of employment is most common in our data? 


```python
# Let's calculate the percentage of each job status category.
data.job.value_counts(normalize=True)

#plot the bar graph of percentage job categories
data.job.value_counts(normalize=True).plot.barh()
plt.show()

```


    
![png](output_16_0.png)
    


## What is the education level? 


```python
#calculate the percentage of each education category.
data.education.value_counts(normalize=True)

#plot the pie chart of education categories
data.education.value_counts(normalize=True).plot.pie()
plt.show()
```


    
![png](output_18_0.png)
    



```python
data.salary.describe()
```




    count     45161.000000
    mean      57004.849317
    std       32087.698810
    min           0.000000
    25%       20000.000000
    50%       60000.000000
    75%       70000.000000
    max      120000.000000
    Name: salary, dtype: float64



## What are the balances for individuals based on their age? 


```python
#plot the scatter plot of balance and salary variable in data
plt.scatter(data.salary,data.balance)
plt.show()

#plot the scatter plot of balance and age variable in data
data.plot.scatter(x="age",y="balance")
plt.show()
```


    
![png](output_21_0.png)
    



    
![png](output_21_1.png)
    


## What is correlating with balance? 


```python
#plot the pair plot of salary, balance and age in data dataframe.
sns.pairplot(data = data, vars=['salary','balance','age'])
plt.show()
```


    
![png](output_23_0.png)
    



```python
# Creating a matrix using age, salary, balance as rows and columns
data[['age','salary','balance']].corr()

#plot the correlation matrix of salary, balance and age in data dataframe.
sns.heatmap(data[['age','salary','balance']].corr(), annot=True, cmap = 'Greens')
plt.show()
```


    
![png](output_24_0.png)
    


## What is the salary range and averages for both response types? 


```python
#create response_rate of numerical data type where response "yes"= 1, "no"= 0
data['response_rate'] = np.where(data.response=='yes',1,0)
data.response_rate.value_counts()
```




    response_rate
    0    39876
    1     5285
    Name: count, dtype: int64



## What marital status has the highest response rate? 


```python
#plot the bar graph of marital status with average value of response_rate
data.groupby('marital')['response_rate'].mean().plot.bar()
plt.show()
```


    
![png](output_28_0.png)
    


## What combination of education and marital status has the largest response rate? 


```python
result = pd.pivot_table(data=data, index='education', columns='marital',values='response_rate')
print(result)

#create heat map of to show correlations betwenn education vs marital vs response_rate
sns.heatmap(result, annot=True, cmap = 'RdYlGn', center=0.117)
plt.show()
```

    marital    divorced   married    single
    education                              
    primary    0.138852  0.075601  0.106808
    secondary  0.103559  0.094650  0.129271
    tertiary   0.137415  0.129835  0.183737
    unknown    0.142012  0.122519  0.162879



    
![png](output_30_1.png)
    


## What is the average salary for each age group in the data? 


```python
#plot the bar graph of age groups with average salary for that group
bins = [18, 30, 40, 50, 60, 70, 120]
labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70+']
data['agerange'] = pd.cut(data.age, bins, labels = labels,include_lowest = True)

#plot the bar graph of average salary per age group
data.groupby('agerange')['salary'].mean().plot.bar()
plt.title('Avg Salary per Age',fontsize = 12)
plt.show()
```

    /tmp/ipykernel_39902/506738209.py:7: FutureWarning: The default of observed=False is deprecated and will be changed to True in a future version of pandas. Pass observed=False to retain current behavior or observed=True to adopt the future default and silence this warning.
      data.groupby('agerange')['salary'].mean().plot.bar()



    
![png](output_32_1.png)
    


Let us save and upload our work to Jovian before finishing up.

## Conclusions

What we can say from the visuals above are the following:

1. Approx. 60% of our customers are in the technician/management/blue collar category of work.
2. Half are high school graduates, and less than a third have higher education.
3. For people under 65, the balance is typically between 0-20000. For over 65, we see 0-10000 is the range. 
4. Heatmap supports the age-balance correlation to be stronger than salary-balance.
5. Reponse rate is highest for single highly educated and lowest for married and less educated individuals. 

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>


```python

```
