---
title: Descriptive Statistics
author: Juma Shafara
date: "2024-02"
date-modified: "2024-08-23"
description: Descriptive statistics is a branch of statistics that deals with the presentation and summary of data in a meaningful and informative way.
keywords: [descriptive statistics, "what is descriptive statistics", Measures of central tendency, mean, median, mode, Measures of variability, range, variance,standard deviation, Measures of distribution shape, skewness, kurtosis, Measures of association, quantify the relationship between variables, coefficients]
---

![Photo by DATAIDEA](../../assets/banner4.png)


```python
#| hide
#| default_exp statistics
```


```python
## Uncomment and run this cell to install the packages
# !pip install --upgrade dataidea
```

## Descriptive Statistics and Summary Metrics

In this notebook, we will learn to obtain important values that describe our data including:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Measures of central tendency</li> 
<li><i class="bi bi-cursor"></i> Measures of variability</li> 
<li><i class="bi bi-cursor"></i> Measures of distribution shape</li> 
<li><i class="bi bi-cursor"></i> Measures of association</li> 
</ul>


```python
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
```

This notebook has been modified to use the Nobel Price Laureates Dataset which you can download from [opendatasoft](https://public.opendatasoft.com/explore/dataset/nobel-prize-laureates/export/?disjunctive.category)


```python
# load the dataset (modify the path to point to your copy of the dataset)
data = pd.read_csv('../assets/nobel_prize_year.csv')
data = data[data.Gender != 'org'] # removing organizations
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
      <th>Year</th>
      <th>Gender</th>
      <th>Category</th>
      <th>birth_year</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>505</th>
      <td>2014</td>
      <td>male</td>
      <td>Physics</td>
      <td>1929</td>
      <td>85</td>
    </tr>
    <tr>
      <th>318</th>
      <td>1952</td>
      <td>male</td>
      <td>Literature</td>
      <td>1885</td>
      <td>67</td>
    </tr>
    <tr>
      <th>883</th>
      <td>1933</td>
      <td>male</td>
      <td>Literature</td>
      <td>1870</td>
      <td>63</td>
    </tr>
    <tr>
      <th>481</th>
      <td>1995</td>
      <td>male</td>
      <td>Peace</td>
      <td>1908</td>
      <td>87</td>
    </tr>
    <tr>
      <th>769</th>
      <td>2005</td>
      <td>male</td>
      <td>Peace</td>
      <td>1942</td>
      <td>63</td>
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
Before we continue, I have a humble request, to be among the first to hear about future updates of the course materials, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
(formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe class="newsletter-frame" src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no">
</iframe>
</div>
</div>

## What is Descriptive Statistics

Descriptive statistics is a branch of statistics that deals with the presentation and summary of data in a meaningful and informative way. Its primary goal is to describe and summarize the main features of a dataset. 

Commonly used measures in descriptive statistics include:

1. **Measures of central tendency:** These describe the center or average of a dataset and include metrics like mean, median, and mode.

2. **Measures of variability:** These indicate the spread or dispersion of the data and include metrics like range, variance, and standard deviation.

3. **Measures of distribution shape:** These describe the distribution of data points and include metrics like skewness and kurtosis.

4. **Measures of association:** These quantify the relationship between variables and include correlation coefficients.

Descriptive statistics provide simple summaries about the sample and the observations that have been made.

### 1. **Measures of central tendency ie Mean, Median, Mode**:
**The Center of the Data:**

The center of the data is where most of the values are concentrated.

<i class="bi bi-cursor"></i> **Mean:** It is the average value of a dataset calculated by summing all values(numerical) and dividing by the total count.


```python
mean_value = np.mean(data.age)
print("Mean:", mean_value)
```

    Mean: 60.21383647798742


<i class="bi bi-cursor"></i> **Median:** It is the middle value of a dataset when arranged in ascending order. If there is an even number of observations, the median is the average of the two middle values.


```python
median_value = np.median(data.age)
print("Median:", median_value)
```

    Median: 60.0


<i class="bi bi-cursor"></i> **Mode:** It is the value that appears most frequently in a dataset.


```python
mode_value = sp.stats.mode(data.age)[0]
print("Mode:", mode_value)
```

    Mode: 56


**Homework:**

<i class="bi bi-cursor"></i> Other ways to find mode (ie using pandas and numpy)


### 2. **Measures of variability**
**The Variation of the Data:**

The variation of the data is how spread out the data are around the center.

**a) Variance and Standard Deviation**:

<i class="bi bi-cursor"></i> **Variance:** It measures the spread of the data points around the mean.


```python
# how to implement the variance and standard deviation using numpy
variance_value = np.var(data.age)
print("Variance:", variance_value)
```

    Variance: 159.28551085795658


<i class="bi bi-cursor"></i> **Standard Deviation:** It is the square root of the variance, providing a measure of the average distance between each data point and the mean.


```python
std_deviation_value = np.std(data.age)
print("Standard Deviation:", std_deviation_value)
```

    Standard Deviation: 12.620836377116873


<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Summary</h4><p>In summary, variance provides a measure of dispersion in squared units, while standard deviation provides a measure of dispersion in the original units of the data</p></div>


<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>Smaller variances and standard deviation values mean that the data has values similar to each other and closer to the mean and the vice versa is true</p></div>


```python
plt.hist(x=data.age, bins=20, edgecolor='black')
# add standard deviation lines
plt.axvline(mean_value, color='red', linestyle='--', label='Mean')
plt.axvline(mean_value+std_deviation_value, color='orange', linestyle='--', label='1st std Dev')
plt.axvline(mean_value-std_deviation_value, color='orange', linestyle='--')
plt.title('Age of Nobel Prize Winners')
plt.ylabel('Frequency')
plt.xlabel('Age')
# Adjust the position of the legend
plt.legend(loc='upper left')

plt.show()
```


    
![png](output_26_0.png)
    


b) **Range and Interquartile Range (IQR)**:

<i class="bi bi-cursor"></i> **Range:** It is the difference between the maximum and minimum values in a dataset. It is simplest measure of variation


```python
# One way to obtain range
min_age = min(data.age)
max_age = max(data.age)
age_range = max_age - min_age
print('Range:', age_range)
```

    Range: 80



```python
# Calculating the range using numpy
range_value = np.ptp(data.age)
print("Range:", range_value)
```

    Range: 80


<i class="bi bi-cursor"></i> **Interquartile Range (IQR):** It is the range between the first quartile (25th percentile) and the third quartile (75th percentile) of the dataset.

**Quartiles:**

**Calculating Quartiles**

The quartiles (Q0,Q1,Q2,Q3,Q4) are the values that separate each quarter.

Between Q0 and Q1 are the 25% lowest values in the data. Between Q1 and Q2 are the next 25%. And so on.

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Q0 is the smallest value in the data.</li> 
<li><i class="bi bi-cursor"></i> Q1 is the value separating the first quarter from the second quarter of the data.</li> 
<li><i class="bi bi-cursor"></i> Q2 is the middle value (median), separating the bottom from the top half.</li> 
<li><i class="bi bi-cursor"></i> Q3 is the value separating the third quarter from the fourth quarter</li> 
<li><i class="bi bi-cursor"></i> Q4 is the largest value in the data.</li> 
</ul>


```python
# Calculate the quartile
quartiles = np.quantile(a=data.age, q=[0, 0.25, 0.5, 0.75, 1])

print('Quartiles:', quartiles)
```

    Quartiles: [17. 51. 60. 69. 97.]


**Percentiles:**

Percentiles are values that separate the data into 100 equal parts.

For example, The 95th percentile separates the lowest 95% of the values from the top 5%

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> The 25th percentile (P25%) is the same as the first quartile (Q1).</li> 
<li><i class="bi bi-cursor"></i> The 50th percentile (P50%) is the same as the second quartile (Q2) and the median.</li> 
<li><i class="bi bi-cursor"></i> The 75th percentile (P75%) is the same as the third quartile (Q3)</li> 
</ul>

**Calculating Percentiles with Python**

To get all the percentile values, we can use `np.percentile()` method and pass in the data, and the list of the percentiles as showed below.


```python
# Getting many percentiles
percentiles = np.percentile(data.age, [25, 50, 75])
print(f'Percentiles: {percentiles}')
```

    Percentiles: [51. 60. 69.]


To get a single percentile value, we can again use the `np.percentile()` method and pass in the data, and a the specicific percentile you're interested in eg:


```python
# Getting one percentile at a time
first_quartile = np.percentile(a=data.age, q=25) # 25th percentile
middle_percentile = np.percentile(data.age, 50)
third_quartile = np.percentile(data.age, 75) # 75th percentile

print('Q1: ', first_quartile)
print('Q2: ', middle_percentile)  
print('Q3: ', third_quartile)
```

    Q1:  51.0
    Q2:  60.0
    Q3:  69.0


<div class="alert text-white rounded" style="background: #3a6e68;"><h4>Note!</h4><p>Note also that we can be able to use the `np.quantile()` method  to calculate the percentiles which makes logical sense as all the values mark a fraction(percentage) of the data</p></div>



```python
percentiles = np.quantile(a=data.age, q=[0.25, 0.50, 0.75])
print('Percentiles:', percentiles)
```

    Percentiles: [51. 60. 69.]


Now we can be able to obtain the interquartile range as the difference between the third and first quartiles as predefined.


```python
# obtain the interquartile
iqr_value = third_quartile - first_quartile
print('Interquartile range: ', iqr_value)
```

    Interquartile range:  18.0


Note: *Quartiles and percentiles are both types of quantiles*

<!-- Alert -->
<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Summary</h4><p>While the range gives an overview of the entire spread of the data from lowest to highest, the interquartile range focuses s`pecifically on the spread of the middle portion of the data, making it more robust against outliers.</p></div>

### 3. **Measures of distribution shape ie Skewness and Kurtosis**:
**The shape of the Data:**

The shape of the data refers to how the data are bounded on either side of the center.

<i class="bi bi-cursor"></i> **Skewness:** It measures the asymmetry of the distribution.


```python
# let's get skew from scipy
skewness_value = sp.stats.skew(data.age)
print("Skewness:", skewness_value)
```

    Skewness: -0.028324578326524283


**How to interpret Skewness:**

<i class="bi bi-cursor"></i> Positive skewness (> 0) indicates that the tail on the right side of the distribution is longer than the left side (right skewed). 

<i class="bi bi-cursor"></i> Negative skewness (< 0) indicates that the tail on the left side of the distribution is longer than the right side (left skewed). 


```python
# Plot the histogram
# Set density=True for normalized histogram
plt.hist(x=data.age, bins=20, density=True, edgecolor='black')  

# Create a normal distribution curve
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = sp.stats.norm.pdf(x, mean_value, std_deviation_value)
plt.plot(x, p, 'k', linewidth=2)  
# 'k' indicates black color, you can change it to any color

# Labels and legend
plt.xlabel('Age')
plt.ylabel('Probability Density')
plt.title('Histogram with Normal Distribution Curve')
plt.legend(['Normal Distribution', 'Histogram'])

plt.show()
```


    
![png](output_51_0.png)
    


<i class="bi bi-cursor"></i> **Kurtosis:** It measures the peakedness or flatness of the distribution.


```python
# let's get kurtosis from scipy
kurtosis_value = sp.stats.kurtosis(data.age)
print("Kurtosis:", kurtosis_value)
```

    Kurtosis: -0.3811155702676823


**How to interpret Kurtosis:**

<i class="bi bi-cursor"></i> A kurtosis of 3 indicates the normal distribution (mesokurtic), also known as Gaussian distribution.

<i class="bi bi-cursor"></i> Positive kurtosis (> 3) indicates a distribution with heavier tails and a sharper peak than the normal distribution. This is called leptokurtic.

<i class="bi bi-cursor"></i> Negative kurtosis (< 3) indicates a distribution with lighter tails and a flatter peak than the normal distribution. This is called platykurtic.

<div class="alert text-white rounded"><h4><i class="bi bi-info-circle-fill"></i> Note!</h4><p>In simple terms, skewness tells you if your data is leaning more to one side or the other, while kurtosis tells you if your data has heavy or light tails and how sharply it peaks.</p></div>

### 4. **Measures of association**

a). **Correlation**

<i class="bi bi-cursor"></i> Correlation measures the relationship between two numerical variables.

**Correlation Matrix**

<i class="bi bi-cursor"></i> A correlation matrix is simply a table showing the correlation coefficients between variables

**Correlation Matrix in Python**

We can use the `corrcoef()` function in Python to create a correlation matrix.


```python
# Generate example data
x = np.array([1, 1, 3, 5, 15])
y = np.array([2, 4, 6, 8, 10])

correlation_matrix = np.corrcoef(x, y)

correlation_matrix_df = pd.DataFrame(
    correlation_matrix, 
    columns=['x', 'y'], 
    index=['x', 'y']
    )
correlation_matrix_df
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
      <th>x</th>
      <th>y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>x</th>
      <td>1.000000</td>
      <td>0.867722</td>
    </tr>
    <tr>
      <th>y</th>
      <td>0.867722</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>



**Correlation Coefficient**:

<i class="bi bi-cursor"></i> The correlation coefficient measures the strength and direction of the linear relationship between two continuous variables.

<i class="bi bi-cursor"></i> t ranges from -1 to 1, where:
<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> 1 indicates a perfect positive linear relationship, eg complementary good bread and blueband, battery and torch, fuel and car</li> 
<li><i class="bi bi-cursor"></i> -1 indicates a perfect negative linear relationship, eg substitute goods like tea and coffee</li> 
<li><i class="bi bi-cursor"></i> 0 indicates no linear relationship, eg phones and socks, house and mouse</li> 
</ul>


```python
# Calculate correlation coefficient
correlation = np.corrcoef(x, y)[0, 1]
print("Correlation Coefficient:", correlation)
```

    Correlation Coefficient: 0.8677218312746245


**Correlation vs Causality:**

Correlation measures the numerical relationship between two varaibles

A high correlation coefficient (close to 1), does not mean that we can for sure conclude an actual relationship between two variables.

A classic example:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> During the summer, the sale of ice cream at a beach increases</li> 
<li><i class="bi bi-cursor"></i> Simultaneously, drowning accidents also increase as well</li> 
</ul>
  
Does this mean that increase of ice cream sale is a direct cause of increased drowning accidents?

**Measures of Association for Categorical Variables**

b) **Contingency Tables and Chi-square Test for Independence**:

<i class="bi bi-cursor"></i> Contingency tables are used to summarize the relationship between two categorical variables by counting the frequency of observations for each combination of categories.

<i class="bi bi-cursor"></i> Chi-square test for independence determines whether there is a statistically significant association between the two categorical variables.


```python
demo_data = data[['Gender', 'Category']]

# We drop all the missing values just for demonstration purposes
demo_data = demo_data.dropna()
```

Obtain the cross tabulation of Gender and Category. The cross tabulation is also known as the contingency table


```python
# cross tab
gender_category_tab = pd.crosstab(
    demo_data.Gender, 
    demo_data.Category
    )

# Let's have a look at the outcome
gender_category_tab
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
      <th>Category</th>
      <th>Chemistry</th>
      <th>Economics</th>
      <th>Literature</th>
      <th>Medicine</th>
      <th>Peace</th>
      <th>Physics</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>female</th>
      <td>8</td>
      <td>2</td>
      <td>17</td>
      <td>13</td>
      <td>18</td>
      <td>5</td>
    </tr>
    <tr>
      <th>male</th>
      <td>181</td>
      <td>87</td>
      <td>102</td>
      <td>212</td>
      <td>90</td>
      <td>219</td>
    </tr>
  </tbody>
</table>
</div>



### Test of Independence:
   This test is used to determine whether there is a significant association between two categorical variables.

   Formula:
   $$χ² = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
   where:
   - $O_{ij}$ = Observed frequency for each cell in the contingency table
   - $E_{ij}$ = Expected frequency for each cell under the assumption of independence



```python
chi2_stat, p_value, dof, expected = sp.stats.chi2_contingency(gender_category_tab)

print('Chi-square Statistic:', chi2_stat)
print('p-value:', p_value)
print('Degrees of freedom (dof):', dof)
# print('Expected:', expected)
```

    Chi-square Statistic: 40.7686907732235
    p-value: 1.044840181761602e-07
    Degrees of freedom (dof): 5


**Interpretation of Chi2 Test Results:**

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> The Chi-square statistic measures the difference between the observed frequencies in the contingency table and the frequencies that would be expected if the variables were independent.</li> 
<li><i class="bi bi-cursor"></i> The p-value is the probability of obtaining a Chi-square statistic as extreme as, or more extreme than, the one observed in the sample, assuming that the null hypothesis is true (i.e., assuming that there is no association between the variables).</li> 
<li><i class="bi bi-cursor"></i> A low p-value indicates strong evidence against the null hypothesis, suggesting that there is a significant association between the variables.</li> 
<li><i class="bi bi-cursor"></i> A high p-value indicates weak evidence against the null hypothesis, suggesting that there is no significant association between the variables.</li> 
</ul>

c. **Measures of Association for Categorical Variables**:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Measures like Cramer's V or phi coefficient quantify the strength of association between two categorical variables.</li> 
<li><i class="bi bi-cursor"></i> These measures are based on chi-square statistics and the dimensions of the contingency table.</li> 
</ul>

### The formula for Cramer's V is:

$$V = \sqrt{\frac{χ²}{n(k - 1)}}$$

Where:
- $χ²$ is the chi-square statistic from the chi-square test of independence.
- $n$ is the total number of observations in the contingency table.
- $k$ is the minimum of the number of rows and the number of columns in the contingency table.

Cramer's V is a normalized measure of association, making it easier to interpret compared to the raw chi-square statistic. A larger value of Cramer's V indicates a stronger association between the variables.


```python
#| hide
#| export

import numpy as np

def cramersV(contingency_table):
    
    chi2_statistic = sp.stats.chi2_contingency(contingency_table)[0]
    total_observations = contingency_table.sum().sum()
    phi2 = chi2_statistic / total_observations
    rows, columns = contingency_table.shape
    
    return np.sqrt(phi2/ min(rows-1, columns-1))
```


```python
from dataidea.statistics import cramersV
```


```python
cramersV(contingency_table=gender_category_tab)
```




    0.20672318859163366




```python
#| hide
#| export

import pandas as pd
import scipy as sp

def cramersVCorrected(contingency_table):
    
    chi2_statistic = sp.stats.chi2_contingency(contingency_table)[0]
    total_observations = contingency_table.sum().sum()
    phi2 = chi2_statistic / total_observations
    rows, columns = contingency_table.shape
    phi2_corrected = max(0, phi2 - ((columns-1)*(rows-1))/(total_observations-1))
    rows_corrected = rows - ((rows-1)**2)/(total_observations-1)
    columns_corrected = columns - ((columns-1)**2)/(total_observations-1)
    
    return np.sqrt(phi2_corrected / min((columns_corrected-1), (rows_corrected-1)))
```


```python
from dataidea.statistics import cramersVCorrected
```


```python
cramersVCorrected(gender_category_tab)
```




    0.19371955249110775



Cramer's V is measure of association between two categorical variables. It ranges from 0 to 1 where: 

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> 0 indicates no association between the variables</li> 
<li><i class="bi bi-cursor"></i> 1 indicates a perfect association between the variables</li> 
</ul>

Here's an interpretation of the Cramer's V:

<ul class="cursored-list">
<li><i class="bi bi-cursor"></i> Small effect: Around 0.1</li> 
<li><i class="bi bi-cursor"></i> Medium effect: Around 0.3</li> 
<li><i class="bi bi-cursor"></i> Large effect: Around 0.5 or greater</li> 
</ul>

#### Frequency Tables
Frequency means the number of times a value appears in the data. A table can quickly show us how many times each value appears. If the data has many different values, it is easier to use intervals of values to present them in a table.

Here's the age of the 934 Nobel Prize winners up until the year 2020. IN the table, each row is an age interval of 10 years

Age Interval | Frequency
-------------|-----------
10-19 |	1
20-29 |	2
30-39 |	48
40-49 |	158
50-59 |	236
60-69 |	262
70-79 |	174
80-89 |	50
90-99 |	3

**Note:** *The intervals for the values are also called bin*

### Further Reading

Chapter 3 of *An Introduction to Statistical Methods and Data Analysis 7th Edition_New*


```python
#| hide
import nbdev; nbdev.nbdev_export()
```

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
