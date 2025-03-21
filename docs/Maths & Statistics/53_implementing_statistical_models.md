---
title: Statistical Models
author: Juma Shafara
date: "2024-02"
date-modified: "2024-07-25"
description: Statistical models are mathematical representations of relationships between variables in a dataset. Python provides a wide range of tools for statistical modeling and inference. 
keywords: [statistical models, linear regression, logistic regression, statsmodels.api, statistics]
---

![Photo by DATAIDEA](../../assets/banner4.png)


```python
## Uncomment and run this cell to install the packages
# !pip install pandas numpy statsmodels
```

## Implementing Statistical Models in Python

#### Statistical models
Statistical models are mathematical representations of relationships between variables in a dataset. These models are used to make predictions, infer causal relationships, and understand patterns in data. Statistical modeling involves formulating hypotheses about the data generating process, estimating model parameters from observed data, and evaluating the fit of the model to the data.

The statsmodels.api library in Python provides a wide range of tools for statistical modeling and inference. It allows users to build, estimate, and analyze various statistical models using a simple and intuitive interface.


```python
import statsmodels.api as sm
import numpy as np
```

1. **Linear Regression**:
   - Linear regression is used to model the relationship between one or more independent variables and a continuous dependent variable.



```python
# Generate example data
np.random.seed(0)
X = np.random.rand(100, 2)  # Two independent variables
```


```python
# Dependent variable with noise

y = 2 * X[:, 0] + 3 * X[:, 1] + np.random.normal(0, 1, 100)  
```


```python
# Add constant term for intercept
X = sm.add_constant(X)
```


```python
# Fit linear regression model
model = sm.OLS(y, X).fit()
```


```python
# Print model summary
print(model.summary())
```

                                OLS Regression Results                            
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.440
    Model:                            OLS   Adj. R-squared:                  0.428
    Method:                 Least Squares   F-statistic:                     38.06
    Date:                Wed, 17 Apr 2024   Prob (F-statistic):           6.31e-13
    Time:                        12:22:26   Log-Likelihood:                -140.25
    No. Observations:                 100   AIC:                             286.5
    Df Residuals:                      97   BIC:                             294.3
    Df Model:                           2                                         
    Covariance Type:            nonrobust                                         
    ==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const          0.2554      0.277      0.922      0.359      -0.294       0.805
    x1             1.4260      0.356      4.011      0.000       0.720       2.132
    x2             2.8054      0.351      8.004      0.000       2.110       3.501
    ==============================================================================
    Omnibus:                        1.210   Durbin-Watson:                   2.349
    Prob(Omnibus):                  0.546   Jarque-Bera (JB):                0.703
    Skew:                           0.122   Prob(JB):                        0.704
    Kurtosis:                       3.330   Cond. No.                         5.58
    ==============================================================================
    
    Notes:
    [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



```python
0.2554/0.277 
```




    0.9220216606498195



- R-squared measures how well the independant variables explain the variability of the dependant variable
- F-Statistic measures the significance of the regression model
- t-statistic for each coefficient measures the significance level of each independent variable


2. **Logistic Regression**:
   - Logistic regression is used when the dependent variable is binary (e.g., 0 or 1, True or False).



```python
# Generate example data for logistic regression
np.random.seed(0)
X = np.random.rand(100, 2)  # Two independent variables
# Generate binary outcome variable based on a threshold
threshold = 0.6
y = (2 * X[:, 0] + 3 * X[:, 1] > threshold).astype(int)

# Add constant term for intercept
X = sm.add_constant(X)

# Fit logistic regression model
logit_model = sm.Logit(y, X).fit()

# Print model summary
print(logit_model.summary())
```

    Warning: Maximum number of iterations has been exceeded.
             Current function value: 0.000000
             Iterations: 35
                               Logit Regression Results                           
    ==============================================================================
    Dep. Variable:                      y   No. Observations:                  100
    Model:                          Logit   Df Residuals:                       97
    Method:                           MLE   Df Model:                            2
    Date:                Wed, 17 Apr 2024   Pseudo R-squ.:                   1.000
    Time:                        13:05:57   Log-Likelihood:            -1.1958e-06
    converged:                      False   LL-Null:                       -9.8039
    Covariance Type:            nonrobust   LLR p-value:                 5.524e-05
    ==============================================================================
                     coef    std err          z      P>|z|      [0.025      0.975]
    ------------------------------------------------------------------------------
    const        -70.8342   4.95e+04     -0.001      0.999   -9.71e+04     9.7e+04
    x1           196.7613   1.92e+05      0.001      0.999   -3.76e+05    3.76e+05
    x2           488.7691   7.23e+05      0.001      0.999   -1.42e+06    1.42e+06
    ==============================================================================
    
    Complete Separation: The results show that there iscomplete separation or perfect prediction.
    In this case the Maximum Likelihood Estimator does not exist and the parameters
    are not identified.


    /home/jumashafara/venvs/dataanalysis/lib/python3.10/site-packages/statsmodels/base/model.py:607: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals
      warnings.warn("Maximum Likelihood optimization failed to "




These examples demonstrate how to implement linear regression and logistic regression using `statsmodels.api`. The summary output provides detailed information about the model parameters, goodness-of-fit measures, and statistical significance of predictors. This can be useful for interpreting the results and assessing the performance of the models.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
