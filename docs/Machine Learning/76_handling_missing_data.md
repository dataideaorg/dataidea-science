---
title: Handling Missing Data
keywords: [handling missing data, handling missing data in python, python data analysis, dataidea, machine learning, data preprocessing, sklearn data preprocessing]
description: n this notebook, we look into the top four missing data imputation methods
author: Juma Shafara
date: "2024-03"
---

![Photo by DATAIDEA](../../../assets/banner4.png)

## Introduction:

Missing data is a common hurdle in data analysis, impacting the reliability of insights drawn from datasets. Python offers a range of solutions to address this issue, some of which we discussed in the earlier weeks. In this notebook, we look into the top four missing data imputation methods:

- SimpleImputer
- KNNImputer
- IterativeImputer 
- Datawig

We'll explore these essential techniques, using sklearn and the weather dataset.

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


```python
# install the libraries for this demonstration
# ! pip install -U dataidea
```


```python
import pandas as pd
import dataidea as di
```

`loadDataset` allows us to load datasets inbuilt in the dataidea library


```python
weather = di.loadDataset('weather') 
weather
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
weather.isna().sum()
```




    day            0
    temperature    4
    windspead      4
    event          2
    dtype: int64



Let's demonstrate how to use the top three missing data imputation methods—SimpleImputer, KNNImputer, and IterativeImputer—using the simple weather dataset.


```python
# select age from the data
temp_wind = weather[['temperature', 'windspead']].copy()
```


```python
temp_wind_imputed = temp_wind.copy()
```

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8076040302380238"
     crossorigin="anonymous"></script>
<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## SimpleImputer from scikit-learn:
   - **Usage**: SimpleImputer is a straightforward method for imputing missing values by replacing them with a constant, mean, median, or most frequent value along each column.
   - **Pros**:
     - Easy to use and understand.
     - Can handle both numerical and categorical data.
     - Offers flexibility with different imputation strategies.
   - **Cons**:
     - It doesn't consider relationships between features.
     - May not be the best choice for datasets with complex patterns of missingness.
   - **Example**:


```python
from sklearn.impute import SimpleImputer

simple_imputer = SimpleImputer(strategy='mean')
temp_wind_simple_imputed = simple_imputer.fit_transform(temp_wind)

temp_wind_simple_imputed_df = pd.DataFrame(temp_wind_simple_imputed, columns=temp_wind.columns)
```

Let's have a look at the outcome


```python
temp_wind_simple_imputed_df
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
      <th>temperature</th>
      <th>windspead</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33.2</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.0</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>33.2</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.0</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>5</th>
      <td>33.2</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>33.2</td>
      <td>8.4</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34.0</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>40.0</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



### Exercise:
1. Try out the SimpleImputer with different imputation strategies like mode, constant 
2. Choose and try some imputation techniques on categorical data

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8076040302380238"
     crossorigin="anonymous"></script>
<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## KNNImputer from scikit-learn:
   - **Usage**: 
      - KNNImputer imputes missing values using k-nearest neighbors, replacing them with the mean value of the nearest neighbors.
      - You can read more about the KNNImputer from [the sklearn official docs site](https://scikit-learn.org/stable/modules/generated/sklearn.impute.KNNImputer)
   - **Pros**:
     - Considers relationships between features, making it suitable for datasets with complex patterns of missingness.
     - Can handle both numerical and categorical data.
   - **Cons**:
     - Computationally expensive for large datasets.
     - Requires careful selection of the number of neighbors (k).

<div class="alert text-white rounded" style="background: #3a6e68;"><h4>Note!</h4><p>By default, the KNNImputer uses 'nan' values as missing data and the 'nan_euclidean' metric to calculate the distances between values.</p></div>

   - **Example**:


```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=2)
temp_wind_knn_imputed = knn_imputer.fit_transform(temp_wind)

temp_wind_knn_imputed_df = pd.DataFrame(temp_wind_knn_imputed, columns=temp_wind.columns)
```

If we take a look at the outcome


```python
weather
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



<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8076040302380238"
     crossorigin="anonymous"></script>
<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

### Filling a single column independently using the `KNNImputer` 

To use the KNNImputer for a single independ column, you can use the index as the other column instead, this will result into equal *euclidean* distances resulting into the use of the *physical neighbors* in the data table.


```python
from sklearn.impute import KNNImputer

knn_imputer = KNNImputer(n_neighbors=2)
windspead_imputed = knn_imputer.fit_transform(weather[['windspead']].reset_index())

windspead_imputed
```




    array([[ 0. ,  6. ],
           [ 1. ,  9. ],
           [ 2. ,  8. ],
           [ 3. ,  7. ],
           [ 4. ,  8. ],
           [ 5. ,  7.5],
           [ 6. , 10. ],
           [ 7. ,  8. ],
           [ 8. , 12. ]])




```python
# we can fill it back in the weather data
weather['windspead'] = windspead_imputed[:, 1]

# now looking at the data
weather
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
      <td>8.0</td>
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
      <td>8.0</td>
      <td>Rain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>08/01/2017</td>
      <td>NaN</td>
      <td>7.5</td>
      <td>Sunny</td>
    </tr>
    <tr>
      <th>6</th>
      <td>09/01/2017</td>
      <td>NaN</td>
      <td>10.0</td>
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



### Exercise

- Try out the KNNImputer with different numbers of neighbors and compare the results
- Findo out how to use KNNImputer to fill categorical data

<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8076040302380238"
     crossorigin="anonymous"></script>
<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## IterativeImputer from scikit-learn:
   - **Usage**: IterativeImputer models each feature with missing values as a function of other features and uses that estimate for imputation. It iteratively estimates the missing values.
   - **Pros**:
     - Takes into account relationships between features, making it suitable for datasets with complex missing patterns.
     - More robust than SimpleImputer for handling missing data.
   - **Cons**:
     - Can be computationally intensive and slower than SimpleImputer.
     - Requires careful tuning of model parameters.
   - **Example**:


```python
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

iterative_imputer = IterativeImputer()
temp_wind_iterative_imputed = iterative_imputer.fit_transform(temp_wind)

temp_wind_iterative_imputed_df = pd.DataFrame(temp_wind_iterative_imputed, columns=temp_wind.columns)

temp_wind_iterative_imputed_df
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
      <th>temperature</th>
      <th>windspead</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.000000</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>33.967053</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31.410210</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>32.049421</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35.245474</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>40.000000</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



You can also choose an estimator of your choice, let's try a `Linear Regression` model


```python
from sklearn.linear_model import LinearRegression
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

# set estimator to an instance of a model
iterative_imputer = IterativeImputer(estimator=LinearRegression())
temp_wind_iterative_imputed = iterative_imputer.fit_transform(temp_wind)

temp_wind_iterative_imputed_df = pd.DataFrame(temp_wind_iterative_imputed, columns=temp_wind.columns)

temp_wind_iterative_imputed_df
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
      <th>temperature</th>
      <th>windspead</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>32.000000</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>34.125000</td>
      <td>9.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>28.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>31.041667</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>32.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>31.812500</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>6</th>
      <td>35.666667</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>7</th>
      <td>34.000000</td>
      <td>8.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>40.000000</td>
      <td>12.0</td>
    </tr>
  </tbody>
</table>
</div>



<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8076040302380238"
     crossorigin="anonymous"></script>
<!-- inline_horizontal -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-8076040302380238"
     data-ad-slot="9021194372"
     data-ad-format="auto"
     data-full-width-responsive="true"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script>

## Datawig:

Datawig is a library specifically designed for imputing missing values in tabular data using deep learning models.


```python
# import datawig

# # Impute missing values
# df_imputed = datawig.SimpleImputer.complete(weather)
```

These top imputation methods offer different trade-offs in terms of computational complexity, handling of missing data patterns, and ease of use. The choice between them depends on the specific characteristics of the dataset and the requirements of the analysis.

## Homework
- Try out these techniques for categorical data

<div class="p-3">
<p class=pb-1>
Don't miss out on any updates and developments! Subscribe to the DATAIDEA Newsletter it's easy and safe.
</p>
<iframe src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no" style="margin: 0; border-radius: 0px !important; background-color: transparent; width: 100%;" ></iframe>
</div>

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
