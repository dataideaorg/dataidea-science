---
title: ANOVA for Feature Selection
keywords: [
    "ANOVA for feature selection",
    "Feature selection techniques",
    "Data Science tutorial",
    "Machine learning feature selection",
    "ANOVA in data science",
    "Univariate feature selection",
    "Fantasy Premier League dataset analysis",
    "SelectKBest example",
    "Statistical tests for feature selection",
    "F-statistic in ANOVA",
    "Python feature selection",
    "Scikit-learn SelectKBest",
    "Analysis of Variance",
    "Machine learning with ANOVA",
    "Data science programming"
]
description: In this notebook, we demonstrate how ANOVA (Analysis of Variance) can be used to identify better features for machine learning models
author: Juma Shafara
date: "2023-03"
---

![Photo by DATAIDEA](../../assets/banner4.png)

In this notebook, we demonstrate how ANOVA (Analysis of Variance) can be used to identify better features for machine learning models. We'll use the Fantasy Premier League (FPL) dataset to show how ANOVA helps in selecting features that best differentiate categories.


```python
# Uncomment the line below if you need to install the dataidea package
# !pip install -U dataidea
```

First, we'll import the necessary packages: `scipy` for performing ANOVA, `dataidea` for loading the FPL dataset, and `SelectKBest` from `scikit-learn` for univariate feature selection based on statistical tests.


```python
import scipy as sp
from sklearn.feature_selection import SelectKBest, f_classif
import dataidea as di
```

Let's load the FPL dataset and preview the top 5 rows.


```python
# Load FPL dataset
fpl = di.loadDataset('fpl') 

# Preview the top 5 rows
fpl.head(n=5)
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
      <th>First_Name</th>
      <th>Second_Name</th>
      <th>Club</th>
      <th>Goals_Scored</th>
      <th>Assists</th>
      <th>Total_Points</th>
      <th>Minutes</th>
      <th>Saves</th>
      <th>Goals_Conceded</th>
      <th>Creativity</th>
      <th>Influence</th>
      <th>Threat</th>
      <th>Bonus</th>
      <th>BPS</th>
      <th>ICT_Index</th>
      <th>Clean_Sheets</th>
      <th>Red_Cards</th>
      <th>Yellow_Cards</th>
      <th>Position</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Bruno</td>
      <td>Fernandes</td>
      <td>MUN</td>
      <td>18</td>
      <td>14</td>
      <td>244</td>
      <td>3101</td>
      <td>0</td>
      <td>36</td>
      <td>1414.9</td>
      <td>1292.6</td>
      <td>1253</td>
      <td>36</td>
      <td>870</td>
      <td>396.2</td>
      <td>13</td>
      <td>0</td>
      <td>6</td>
      <td>MID</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Harry</td>
      <td>Kane</td>
      <td>TOT</td>
      <td>23</td>
      <td>14</td>
      <td>242</td>
      <td>3083</td>
      <td>0</td>
      <td>39</td>
      <td>659.1</td>
      <td>1318.2</td>
      <td>1585</td>
      <td>40</td>
      <td>880</td>
      <td>355.9</td>
      <td>12</td>
      <td>0</td>
      <td>1</td>
      <td>FWD</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mohamed</td>
      <td>Salah</td>
      <td>LIV</td>
      <td>22</td>
      <td>6</td>
      <td>231</td>
      <td>3077</td>
      <td>0</td>
      <td>41</td>
      <td>825.7</td>
      <td>1056.0</td>
      <td>1980</td>
      <td>21</td>
      <td>657</td>
      <td>385.8</td>
      <td>11</td>
      <td>0</td>
      <td>0</td>
      <td>MID</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Heung-Min</td>
      <td>Son</td>
      <td>TOT</td>
      <td>17</td>
      <td>11</td>
      <td>228</td>
      <td>3119</td>
      <td>0</td>
      <td>36</td>
      <td>1049.9</td>
      <td>1052.2</td>
      <td>1046</td>
      <td>26</td>
      <td>777</td>
      <td>315.2</td>
      <td>13</td>
      <td>0</td>
      <td>0</td>
      <td>MID</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Patrick</td>
      <td>Bamford</td>
      <td>LEE</td>
      <td>17</td>
      <td>11</td>
      <td>194</td>
      <td>3052</td>
      <td>0</td>
      <td>50</td>
      <td>371.0</td>
      <td>867.2</td>
      <td>1512</td>
      <td>26</td>
      <td>631</td>
      <td>274.6</td>
      <td>10</td>
      <td>0</td>
      <td>3</td>
      <td>FWD</td>
    </tr>
  </tbody>
</table>
</div>



ANOVA helps us determine if there's a significant difference between the means of different groups. We use it to select features that best show the difference between categories. Features with higher F-statistics are preferred.

### ANOVA for Goals Scored

We will create groups of goals scored by each player position (forwards, midfielders, defenders, and goalkeepers) and run an ANOVA test.


```python
# Create groups of goals scored for each player position
forwards_goals = fpl[fpl.Position == 'FWD']['Goals_Scored']
midfielders_goals = fpl[fpl.Position == 'MID']['Goals_Scored']
defenders_goals = fpl[fpl.Position == 'DEF']['Goals_Scored']
goalkeepers_goals = fpl[fpl.Position == 'GK']['Goals_Scored']

# Perform the ANOVA test for the groups
f_statistic, p_value = sp.stats.f_oneway(forwards_goals, midfielders_goals, defenders_goals, goalkeepers_goals)
print("F-statistic:", f_statistic)
print("p-value:", p_value)
```

    F-statistic: 33.281034594400445
    p-value: 3.9257634156019246e-20


We observe an *F-statistic* of `33.281` and a *p-value* of `3.926e-20`, indicating a significant difference at multiple confidence levels.

### ANOVA for Assists

Next, we'll create groups for assists and run an ANOVA test.


```python
# Create groups of assists for each player position
forwards_assists = fpl[fpl.Position == 'FWD']['Assists']
midfielders_assists = fpl[fpl.Position == 'MID']['Assists']
defenders_assists = fpl[fpl.Position == 'DEF']['Assists']
goalkeepers_assists = fpl[fpl.Position == 'GK']['Assists']

# Perform the ANOVA test for the groups
f_statistic, p_value = sp.stats.f_oneway(forwards_assists, midfielders_assists, defenders_assists, goalkeepers_assists)
print("F-statistic:", f_statistic)
print("p-value:", p_value)
```

    F-statistic: 19.263717036430815
    p-value: 5.124889288362087e-12


We observe an *F-statistic* of `19.264` and a *p-value* of `5.125e-12`, again indicating significance.

### Comparing Results

Both features show significant F-statistics, but goals scored has a higher value, indicating it is a better feature for differentiating player positions.

### Using SelectKBest for Feature Selection

We can also use `SelectKBest` from `scikit-learn` to automate this process.


```python
# Use scikit-learn's SelectKBest (with f_classif)
test = SelectKBest(score_func=f_classif, k=1)

# Fit the model to the data
fit = test.fit(fpl[['Goals_Scored', 'Assists']], fpl.Position)

# Get the F-statistics
scores = fit.scores_

# Select the best feature
features = fit.transform(fpl[['Goals_Scored', 'Assists']])

# Get the indices of the selected features (optional)
selected_indices = test.get_support(indices=True)

# Print indices and scores
print('Feature Scores: ', scores)
print('Selected Features Indices: ', selected_indices)
```

    Feature Scores:  [33.28103459 19.26371704]
    Selected Features Indices:  [0]


The `0th` feature (Goals Scored) is selected as the best feature based on the F-statistics.

### Summary

In this notebook, we demonstrated how to use ANOVA for feature selection in the Fantasy Premier League dataset. By comparing the F-statistics of different features, we identified that 'Goals Scored' is a more significant feature than 'Assists' for differentiating player positions. Using `SelectKBest` from `scikit-learn`, we confirmed that 'Goals Scored' is the best feature among the two. This method can be applied to other datasets and features to enhance the performance of machine learning models.


<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
