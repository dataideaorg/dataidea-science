---
title: Data Cleaning
author: Juma Shafara
date: "2024-01"
date-modified: "2024-07-25"
description: we’ll be using numpy and pandas, to explore some techniques we can use to manipulate and clean a dataset. 
keywords: []
---

![Photo by DATAIDEA](../../assets/banner4.png)

## Cleaning the weather dataset

In this notebook, we'll be using numpy and pandas, to explore some techniques we can use to manipulate and clean a dataset. We'll be using the `weather dataset` which I developed specifically for the purpose of this lesson.

<!-- Newsletter -->
<div class="newsletter">
<div class="newsletter-heading">
<h4><i class="bi bi-info-circle-fill"></i> Don't Miss Any Updates!</h4>
</div>
<div class="newsletter-body">
<p>
Before we continue, we have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
(formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no">
</iframe>
</div>
</div>

Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool whereas Numpy is the fundamental package for scientific computing with Python.

To continue with this notebook, you must have python, pandas and numpy installed.


```python
## Uncomment and run this cell to install pandas and numpy
#!pip install pandas numpy
```


```python
# import the libraries
import pandas as pd
import numpy as np
from dataidea.datasets import loadDataset
```

Let's check the versions of python, numpy and pandas we'll be using for this notebook


```python
# checking python version
print('Python Version: ',)
!python --version
```

    Python Version: 
    Python 3.10.12



```python
# Checking numpy and pandas versions
print('Pandas Version: ', pd.__version__)
print('Numpy Version: ', np.__version__)
```

    Pandas Version:  2.2.2
    Numpy Version:  1.26.4


Let's load the dataset. We'll be using a weather dataset that imagined for learning purposes.


```python
# load the dataset
weather_data = loadDataset('weather')
```

We can sample out random rows from the dataset using the `sample()` method, we can use the `n` parameter to specify the number of rows to sample


```python
# sample out random values from the dataset
weather_data.sample(n=5)
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



From our quick our sample, we can already observe some probles with the data that will need fixing

Display some info about the dataset eg number of entries, count of non-null values and variable datatypes using the `info()` method


```python
# get quick dataframe info
weather_data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 9 entries, 0 to 8
    Data columns (total 4 columns):
     #   Column       Non-Null Count  Dtype  
    ---  ------       --------------  -----  
     0   day          9 non-null      object 
     1   temperature  5 non-null      float64
     2   windspead    5 non-null      float64
     3   event        7 non-null      object 
    dtypes: float64(2), object(2)
    memory usage: 416.0+ bytes


We can count all missing values in each column in our dataframe by using `dataframe.isna().sum()`, eg


```python
# count missing values in each column
weather_data.isna().sum()
```




    day            0
    temperature    4
    windspead      4
    event          2
    dtype: int64



We can use a boolean-indexing like technique to find all rows in a dataset with missing values in a specific column.


```python
# get rows with missing data in temperature
weather_data[weather_data.temperature.isna()]
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# get rows with missing data in event column
weather_data[weather_data.event.isna()]
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



For the next part, we would like to demonstrate forward fill (`ffill()`) and  backward fill (`bfill`), we first create two copies of the dataframe to avoid modifying our original copy in memory.
- `ffill()` fills the missing values with the previous valid value in the column
- `bfill()` fills the missing values with the next valid value in the column

Let's create 2 copies of our dataframe and test out each of these concepts on either of the copies

For the first copy, let's fill NaN values in the `event` column with `ffill()`


```python
# fill with the previous valid value
weather_data['event'] = weather_data.event.ffill()
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



From the returned dataframe we can observe that the `NaN` values in `event` have been replaced with their corresponding non-null values orccurring earlier than them ie Snow at row 3 and Sunny at row 6 

**Exercise:** Demonstrate how to replace missing values with the `bfill()` method

### Choosing Between `ffill` and `bfill`

- **Context**: Choose based on the context and the logical assumption that fits the nature of your data. If the past influences the present, use `ffill`. If the future influences the present, use `bfill`.
- **Data Patterns**: Consider the patterns in your data and what makes sense for your specific analysis or model. Ensure that the method you choose maintains the integrity and meaning of your data. 

### Fill with a specific value

We can modify (or fill) a specific value in the dataframe by using the `loc[]` method. This picks the value by its row (index) and column names. Assigning it a new value modifies it in the dataframe as illustrated below


```python
# modify a specific value in the dataframe
weather_data.loc[1, 'temperature'] = 29
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>29.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



Observe that the missing value in row 1 and `temperature` has been replaced with 29

We can use the `fillna()` method to replace all missing values in a column with a specific value as demostrated value


```python
# replace missing values in temperature column with mean
weather_data['temperature'] = weather_data.temperature.fillna(
    value=weather_data.temperature.mean()
)
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>29.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>32.5</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>32.5</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>32.5</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



**Exercise:** Demonstrate some technniques to replace missing data for numeric, and categorical data using the `fillna()`

We can also use the `fillna()` method to fill missing values in multiple columns by passing in the dictionary of key/value pairs of column-name and value to replace. To demonstrate this, let's first reload a fresh dataframe with missing data


```python
weather_data = loadDataset('weather')
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Replace missing values in temperature, column and event
weather_data.fillna(value={
    'temperature': weather_data.temperature.mean(), 
    'windspead': weather_data.windspead.max(), 
    'event': weather_data.event.bfill()
    }, inplace=True)

# Now let's look at our data
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>29.0</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>12.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>32.5</td>
      <td>7.0</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>12.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>32.5</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>32.5</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



We can optionally drop all rows with missing values using the `dropna()` method. To demonstrate this, let's first reload a fresh dataframe with missing data


```python
weather_data = loadDataset('weather')
weather_data
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>04/01/2017</td>
      <td>NaN</td>
      <td>9.0</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>2</th>
      <td>05/01/2017</td>
      <td>28.0</td>
      <td>NaN</td>
      <td>Snow</td>
    </tr>
    <tr>
      <th>3</th>
      <td>06/01/2017</td>
      <td>NaN</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>07/01/2017</td>
      <td>32.0</td>
      <td>NaN</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Drop all rows with missing values
weather_data.dropna()
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
      <th>day</th>
      <th>temperature</th>
      <th>windspead</th>
      <th>event</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>01/01/2017</td>
      <td>32.0</td>
      <td>6.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>7</th>
      <td>10/01/2017</td>
      <td>34.0</td>
      <td>8.0</td>
      <td>Cloudy</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11/01/2017</td>
      <td>40.0</td>
      <td>12.0</td>
      <td>Sunny</td>
    </tr>
  </tbody>
</table>
</div>



In the next chapter we'll look at some data visualization tools in Python

## Congratulations!

Congratulations on finishing this lesson. In this lesson, you have learned various methods of handling missing data including:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Finding missing values</li> 
<li><i class="bi bi-cursor"></i> bfill and ffill</li> 
<li><i class="bi bi-cursor"></i> filling with a specific value</li> 
<li><i class="bi bi-cursor"></i> min, max and mean values</li> 
</ul>

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
