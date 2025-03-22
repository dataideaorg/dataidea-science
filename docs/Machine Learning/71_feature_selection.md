---
title: Feature Selection
description: Feature selection is a process where you automatically select those features in your data that contribute most to the prediction variable
keywords: [feature selection]
author: Juma Shafara
date: "2024-03"
date-modified: "2024-07-25"
---

![Photo by DATAIDEA](../../assets/banner4.png)

## What is Feature Selection

Feature selection is a process where you automatically select those features in your data that contribute most to the prediction variable or output in which you are interested.

Having irrelevant features in your data can decrease the accuracy of many models, especially linear algorithms like linear and logistic regression.

Three benefits of performing feature selection before modeling your data are:

- Reduces Overfitting: Less redundant data means less opportunity to make decisions based on noise.
- Improves Accuracy: Less misleading data means modeling accuracy improves.
- Reduces Training Time: Less data means that algorithms train faster.

You can learn more about feature selection with scikit-learn in the article [Feature selection](https://scikit-learn.org/stable/modules/feature_selection.html).


```python
import pandas as pd
from sklearn.model_selection import train_test_split
from dataidea.datasets import loadDataset
```


```python
data = loadDataset('../assets/demo_cleaned.csv', 
                    inbuilt=False, file_type='csv')
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
      <th>age</th>
      <th>gender</th>
      <th>marital_status</th>
      <th>address</th>
      <th>income</th>
      <th>income_category</th>
      <th>job_category</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>55</td>
      <td>f</td>
      <td>1</td>
      <td>12</td>
      <td>72.0</td>
      <td>3.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>56</td>
      <td>m</td>
      <td>0</td>
      <td>29</td>
      <td>153.0</td>
      <td>4.0</td>
      <td>3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>24</td>
      <td>m</td>
      <td>1</td>
      <td>4</td>
      <td>26.0</td>
      <td>2.0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>45</td>
      <td>m</td>
      <td>0</td>
      <td>9</td>
      <td>76.0</td>
      <td>4.0</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>44</td>
      <td>m</td>
      <td>1</td>
      <td>17</td>
      <td>144.0</td>
      <td>4.0</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
data = pd.get_dummies(data, columns=['gender'], 
                      dtype='int', drop_first=True)
data.head(n=5)
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
      <th>marital_status</th>
      <th>address</th>
      <th>income</th>
      <th>income_category</th>
      <th>job_category</th>
      <th>gender_m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>55</td>
      <td>1</td>
      <td>12</td>
      <td>72.0</td>
      <td>3.0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>56</td>
      <td>0</td>
      <td>29</td>
      <td>153.0</td>
      <td>4.0</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>24</td>
      <td>1</td>
      <td>4</td>
      <td>26.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>45</td>
      <td>0</td>
      <td>9</td>
      <td>76.0</td>
      <td>4.0</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>44</td>
      <td>1</td>
      <td>17</td>
      <td>144.0</td>
      <td>4.0</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



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

## Univariate Feature Selection Techniques
Statistical tests can be used to select those features that have the strongest relationship with the output variable.

The scikit-learn library provides the `SelectKBest` class that can be used with a suite of different statistical tests to select a specific number of features.

Many different statistical tests can be used with this selection method. For example the *ANOVA F-value* method is appropriate for numerical inputs and categorical data. This can be used via the f_classif() function. We will select the 4 best features using this method in the example below.


```python
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import f_regression
```

Let's first separate our data into features ie `X` and outcome ie `y` as below.


```python
X = data.drop('marital_status', axis=1)
y = data.marital_status
```

### Numeric or Continuous Features with Categorical Outcome
Beginning with the numeric columns, let's find which of them best contributes to the outcome variable


```python
X_numeric = X[['age', 'income', 'address']].copy()
```


```python
# create a test object from SelectKBest
test = SelectKBest(score_func=f_classif, k=2)

# fit the test object to the data
fit = test.fit(X_numeric, y)

# get the scores and features
scores = fit.scores_

# get the selected indices
features = fit.transform(X_numeric)
selected_indices = test.get_support(indices=True)

# print the scores and features
print('Feature Scores: ', scores)
print('Selected Features Indices: ', selected_indices)
```

    Feature Scores:  [1.34973748 1.73808724 0.02878244]
    Selected Features Indices:  [0 1]


This shows us that the best 2 features to use to differentiate between the groups in our outcome are `[0, 1]` ie `age` and `income`

### Numeric Features with Numeric Outcome
Let's selecting the input features `X`, and the output (outcome), `y`


```python
# pick numeric input and output
X = data[['age', 'address']].copy()
y = data.income
```

We will still use the `SelectKBest` class but with our `score_func` as `f_regression` instead. 


```python
test = SelectKBest(score_func=f_regression, k=1)

# Fit the test to the data
fit = test.fit(X, y)

# get scores
test_scores = fit.scores_

# summarize selected features
features = fit.transform(X)

# Get the selected feature indices
selected_indices = fit.get_support(indices=True)

print('Feature Scores: ', test_scores)
print('Selected Features Indices: ', selected_indices)
```

    Feature Scores:  [25.18294605 23.43115992]
    Selected Features Indices:  [0]


Here, we can see that `age` is selected because it returns the higher f_statistic between the two features

### Both input and outcome Categorical

Let's begin by selecting out only the categorical features to make our `X` set and set `y` as categorical


```python
# selecting categorical features
X = data[['gender_m', 'income_category', 'job_category']].copy()

# selecting categorical outcome
y = data.marital_status
```

Now we shall again use `SelectKBest` but with the `score_func` as `chi2`.


```python
from sklearn.feature_selection import chi2
```


```python
test = SelectKBest(score_func=chi2, k=2)
fit = test.fit(X, y)
scores = fit.scores_
features = fit.transform(X)
selected_indices = fit.get_support(indices=True)

print('Feature Scores: ', scores)
print('Selected Features Indices: ', selected_indices)
```

    Feature Scores:  [0.20921223 0.61979264 0.00555967]
    Selected Features Indices:  [0 1]


Note: When using the Chi-Square (chi2) as the the score function for feature selection, you use the Chi-Square statistic.

Again, we can see that the features with higher f_statistic scores have been selected

- `f_classif` is most applicable where the input features are continuous and the outcome is categorical.
- `f_regression` is most applicable where the input features are continuous and the outcome is continuous.
- `chi2` is best for when the both the input and outcome are categorical.

## Recursive Feature Elimination
The Recursive Feature Elimination (or RFE) works by recursively removing attributes and building a model on those attributes that remain.

It uses the model accuracy to identify which attributes (and combination of attributes) contribute the most to predicting the target attribute.

You can learn more about the RFE class in the [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.RFE.html).

### Logistic Regression


```python
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
```


```python
X = data.drop('marital_status', axis=1)
y = data.marital_status
```


```python
# feature extraction
model = LogisticRegression()
rfe = RFE(model)
fit = rfe.fit(X, y)

print("Num Features: %d" % fit.n_features_)
print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)
```

    Num Features: 3
    Selected Features: [False False False  True  True  True]
    Feature Ranking: [2 3 4 1 1 1]



```python
X.head()
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
      <th>address</th>
      <th>income</th>
      <th>income_category</th>
      <th>job_category</th>
      <th>gender_m</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>55</td>
      <td>12</td>
      <td>72.0</td>
      <td>3.0</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>56</td>
      <td>29</td>
      <td>153.0</td>
      <td>4.0</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>24</td>
      <td>4</td>
      <td>26.0</td>
      <td>2.0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>45</td>
      <td>9</td>
      <td>76.0</td>
      <td>4.0</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>44</td>
      <td>17</td>
      <td>144.0</td>
      <td>4.0</td>
      <td>3</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



From the operation above, we can observe features that bring out the best from the `LogisticRegression` model ranked from `1` as most best and bigger numbers as less.

## Feature Importance
Bagged decision trees like Random Forest and Extra Trees can be used to estimate the importance of features.

In the example below we construct a ExtraTreesClassifier classifier for the Pima Indians onset of diabetes dataset. You can learn more about the ExtraTreesClassifier class in the scikit-learn API.

### Extra Trees Classifier


```python
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier
```


```python
# feature extraction
model = ExtraTreesClassifier()
model.fit(X, y)

# see the best features
print(model.feature_importances_)
```

    [0.29058207 0.24978811 0.26342117 0.06763375 0.08501043 0.04356447]


### Random Forest Classifier


```python
# feature extraction
model = RandomForestClassifier()
model.fit(X, y)

# see the best features
print(model.feature_importances_)
```

    [0.28927782 0.2515934  0.28839236 0.06166801 0.06610313 0.04296528]


more about random forest [here](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
