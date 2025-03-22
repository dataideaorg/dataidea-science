---
title: Normalization vs Standardization
keywords: [normalization, standardization, rescaling]
author: Juma Shafara
date: "2024-03"
description: This Jupyter Notebook provides an overview of the importance of data normalization and standardization in preparing data for analysis and modeling
---

![Photo by DATAIDEA](../../assets/banner4.png)

#### Introduction:
In data analysis and machine learning, preprocessing steps such as data normalization and standardization are crucial for improving the performance and interpretability of models.

This Jupyter Notebook provides an overview of the importance of data normalization and standardization in preparing data for analysis and modeling.


```python
import numpy as np
import dataidea as di
```

## Normalization

1. **Normalization**: Normalization typically refers to scaling numerical features to a common scale, often between 0 and 1. This is usually done by subtracting the minimum value and then dividing by the range (maximum - minimum). Normalization is useful when the distribution of the data does not follow a Gaussian distribution (Normal Distribution).


```python
# Data Normalization without libraries:
def minMaxScaling(data):
    min_val = min(data)
    max_val = max(data)
    
    scaled_data = []
    for value in data:
        scaled = (value - min_val) / (max_val - min_val)
        scaled_data.append(scaled)
    return scaled_data
```


```python
# Example data
data = np.array([10, 20, 30, 40, 50])
normalized_data = minMaxScaling(data)
print("Normalized data (Min-Max Scaling):", normalized_data)
```

    Normalized data (Min-Max Scaling): [0.0, 0.25, 0.5, 0.75, 1.0]



```python
from sklearn.preprocessing import MinMaxScaler

# Sample data
data = np.array([[1, 2], [3, 4], [5, 6]])

# Create the scaler
scaler = MinMaxScaler()

# Fit the scaler to the data and transform the data
normalized_data = scaler.fit_transform(data)

print("Original data:")
print(data)
print("\nNormalized data:")
print(normalized_data)
```

    Original data:
    [[1 2]
     [3 4]
     [5 6]]
    
    Normalized data:
    [[0.  0. ]
     [0.5 0.5]
     [1.  1. ]]


Let's now try on a real world dataset!


```python
boston_data = di.loadDataset('boston')
boston_data.head()
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
      <th>CRIM</th>
      <th>ZN</th>
      <th>INDUS</th>
      <th>CHAS</th>
      <th>NOX</th>
      <th>RM</th>
      <th>AGE</th>
      <th>DIS</th>
      <th>RAD</th>
      <th>TAX</th>
      <th>PTRATIO</th>
      <th>B</th>
      <th>LSTAT</th>
      <th>MEDV</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.00632</td>
      <td>18.0</td>
      <td>2.31</td>
      <td>0</td>
      <td>0.538</td>
      <td>6.575</td>
      <td>65.2</td>
      <td>4.0900</td>
      <td>1</td>
      <td>296.0</td>
      <td>15.3</td>
      <td>396.90</td>
      <td>4.98</td>
      <td>24.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0.02731</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>6.421</td>
      <td>78.9</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>396.90</td>
      <td>9.14</td>
      <td>21.6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.02729</td>
      <td>0.0</td>
      <td>7.07</td>
      <td>0</td>
      <td>0.469</td>
      <td>7.185</td>
      <td>61.1</td>
      <td>4.9671</td>
      <td>2</td>
      <td>242.0</td>
      <td>17.8</td>
      <td>392.83</td>
      <td>4.03</td>
      <td>34.7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.03237</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>6.998</td>
      <td>45.8</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>394.63</td>
      <td>2.94</td>
      <td>33.4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.06905</td>
      <td>0.0</td>
      <td>2.18</td>
      <td>0</td>
      <td>0.458</td>
      <td>7.147</td>
      <td>54.2</td>
      <td>6.0622</td>
      <td>3</td>
      <td>222.0</td>
      <td>18.7</td>
      <td>396.90</td>
      <td>5.33</td>
      <td>36.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
boston_scaler = MinMaxScaler()
normalized_data = boston_scaler.fit_transform(boston_data[['CRIM', 'AGE', 'TAX']])
np.set_printoptions(suppress=True)
normalized_data
```




    array([[0.        , 0.64160659, 0.20801527],
           [0.00023592, 0.78269825, 0.10496183],
           [0.0002357 , 0.59938208, 0.10496183],
           ...,
           [0.00061189, 0.90731205, 0.16412214],
           [0.00116073, 0.88980433, 0.16412214],
           [0.00046184, 0.80226571, 0.16412214]])



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

## Standardization

2. **Standardization**: Standardization, often implemented with a method like z-score standardization, transforms the data to have a mean of 0 and a standard deviation of 1. This means that the data will have a Gaussian distribution (if the original data had a Gaussian distribution). 


```python
def zScoreNormalization(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    standardized_data = [(x - mean) / std_dev for x in data]
    return standardized_data
```


```python
# Example data
data = [10, 20, 30, 40, 50]
standardized_data = zScoreNormalization(data)
print("Standardized data (Z-Score Normalization):", standardized_data)
```

    Standardized data (Z-Score Normalization): [-1.414213562373095, -0.7071067811865475, 0.0, 0.7071067811865475, 1.414213562373095]


In Python, we can also typically use the `StandardScaler` from the `sklearn.preprocessing` module to standardize data.


```python
from sklearn.preprocessing import StandardScaler

# Sample data
data = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])

# Create the scaler
scaler = StandardScaler()

# Fit the scaler to the data and transform the data
standardized_data = scaler.fit_transform(data)

print("Original data:")
print(data)
print("\nStandardized data:")
print(standardized_data)

```

    Original data:
    [[1 2 3]
     [3 4 5]
     [5 6 7]]
    
    Standardized data:
    [[-1.22474487 -1.22474487 -1.22474487]
     [ 0.          0.          0.        ]
     [ 1.22474487  1.22474487  1.22474487]]



```python
boston_scaler = StandardScaler()
standardized_data = boston_scaler.fit_transform(boston_data[['CRIM', 'AGE', 'TAX']])
np.set_printoptions(suppress=True)
standardized_data
```




    array([[-0.41978194, -0.12001342, -0.66660821],
           [-0.41733926,  0.36716642, -0.98732948],
           [-0.41734159, -0.26581176, -0.98732948],
           ...,
           [-0.41344658,  0.79744934, -0.80321172],
           [-0.40776407,  0.73699637, -0.80321172],
           [-0.41500016,  0.43473151, -0.80321172]])



#### Importance:

1. Data Normalization:
   - Uniform Scaling: Ensures all features are scaled to a similar range, preventing dominance by features with larger scales.
   - Improved Convergence: Facilitates faster convergence in optimization algorithms by making the loss surface more symmetric.
   - Interpretability: Easier interpretation as values are on a consistent scale, aiding in comparison and understanding of feature importance.


2. Data Standardization:
   - Mean Centering: Transforms data to have a mean of 0 and a standard deviation of 1, simplifying interpretation of coefficients in linear models.
   - Handling Different Scales: Useful when features have different scales or units, making them directly comparable.
   - Reducing Sensitivity to Outliers: Less affected by outliers compared to normalization, leading to more robust models.
   - Maintaining Information: Preserves relative relationships between data points without altering the distribution shape.

## Which one? 
The choice between normalization and standardization depends on your data and the requirements of your analysis. Here are some guidelines to help you decide:

1. **Normalization**:
   - Use normalization when the scale of features is meaningful and should be preserved.
   - Normalize data when you're working with algorithms that require input features to be on a similar scale, such as algorithms using distance metrics like k-nearest neighbors or clustering algorithms like K-means.
   - If the distribution of your data is not Gaussian and you want to scale the features to a fixed range, normalization might be a better choice.

2. **Standardization**:
   - Use standardization when the distribution of your data is Gaussian or when you're unsure about the distribution.
   - Standardization is less affected by outliers compared to normalization, making it more suitable when your data contains outliers.
   - If you're working with algorithms that assume your data is normally distributed, such as linear regression, logistic regression, standardization is typically preferred.

In some cases, you might experiment with both approaches and see which one yields better results for your specific dataset and analysis. Additionally, it's always a good practice to understand your data and the underlying assumptions of the algorithms you're using to make informed decisions about data preprocessing techniques.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
