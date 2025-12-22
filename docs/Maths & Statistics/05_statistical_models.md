---
title: Statistical Models
author: Juma Shafara
date: "2024-02"
date-modified: "2025-02-09"
description: Statistical models are mathematical representations of relationships between variables in a dataset. Learn to build, evaluate, and interpret linear and logistic regression models. 
keywords: [statistical models, linear regression, logistic regression, statsmodels.api, statistics, model evaluation, assumptions, diagnostics]
---

![Photo by DATAIDEA](../../../assets/banner4.png)

## Introduction

Statistical models are mathematical representations of relationships between variables in a dataset. These models are used to make predictions, infer causal relationships, and understand patterns in data. This module focuses on two fundamental models: linear regression and logistic regression.

## Learning Objectives

By the end of this module, you will be able to:

- Understand when to use linear vs logistic regression
- Build linear and logistic regression models using Python
- Check and validate model assumptions
- Interpret model coefficients and outputs
- Evaluate model performance using appropriate metrics
- Diagnose and address common model problems

## Prerequisites

Before starting this module, you should be familiar with:
- [Descriptive Statistics](02_descriptive_statistics.md)
- [Probability Foundations](03_probability_foundations.md)
- [Inferential Statistics](04_inferential_statistics.md)
- Basic Python programming with NumPy and Pandas

```python
## Uncomment and run this cell to install the packages
# !pip install pandas numpy statsmodels matplotlib seaborn scikit-learn
```

```python
import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report
```

## 1. Linear Regression

**Linear regression** models the relationship between one or more independent variables (predictors) and a continuous dependent variable (outcome).

### Model Equation

For simple linear regression (one predictor):

$$y = \beta_0 + \beta_1 x + \epsilon$$

For multiple linear regression:

$$y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + ... + \beta_n x_n + \epsilon$$

where:
- $y$ is the dependent variable
- $x_i$ are independent variables
- $\beta_0$ is the intercept
- $\beta_i$ are coefficients (slopes)
- $\epsilon$ is the error term

### Assumptions of Linear Regression

1. **Linearity**: The relationship between X and Y is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of errors
4. **Normality**: Errors are normally distributed
5. **No multicollinearity**: Predictors are not highly correlated (for multiple regression)

### Building a Linear Regression Model

```python
# Generate example data
np.random.seed(42)
n = 100

# Create features
X1 = np.random.randn(n)
X2 = np.random.randn(n)

# True relationship: y = 2 + 3*X1 + 1.5*X2 + noise
y = 2 + 3*X1 + 1.5*X2 + np.random.randn(n) * 0.5

# Prepare data for statsmodels (needs constant term)
X = pd.DataFrame({'X1': X1, 'X2': X2})
X = sm.add_constant(X)  # Adds intercept term

# Fit the model
model = sm.OLS(y, X).fit()

# Print summary
print(model.summary())
```

### Interpreting Linear Regression Output

```python
# Key metrics from summary:
print(f"\nR-squared: {model.rsquared:.4f}")
print(f"Adjusted R-squared: {model.rsquared_adj:.4f}")
print(f"F-statistic: {model.fvalue:.4f}")
print(f"F-statistic p-value: {model.f_pvalue:.4f}")

# Coefficients
print("\nCoefficients:")
print(model.params)

# Confidence intervals
print("\n95% Confidence Intervals:")
print(model.conf_int())
```

**Key Interpretations:**
- **R-squared**: Proportion of variance in y explained by the model (0 to 1, higher is better)
- **Adjusted R-squared**: R-squared adjusted for number of predictors (penalizes overfitting)
- **F-statistic**: Tests if model is significantly better than intercept-only model
- **Coefficients**: Change in y for one-unit change in predictor (holding others constant)
- **p-values**: Significance of each coefficient

### Model Diagnostics

```python
# 1. Residuals vs Fitted Values (check for homoscedasticity)
fitted = model.fittedvalues
residuals = model.resid

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.scatter(fitted, residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Residuals')
plt.title('Residuals vs Fitted Values')
plt.grid(True, alpha=0.3)

# 2. Q-Q Plot (check for normality of residuals)
from scipy import stats
plt.subplot(1, 3, 2)
stats.probplot(residuals, dist="norm", plot=plt)
plt.title('Q-Q Plot (Normality Check)')
plt.grid(True, alpha=0.3)

# 3. Scale-Location Plot (check for homoscedasticity)
plt.subplot(1, 3, 3)
sqrt_abs_residuals = np.sqrt(np.abs(residuals))
plt.scatter(fitted, sqrt_abs_residuals, alpha=0.6)
plt.xlabel('Fitted Values')
plt.ylabel('√|Standardized Residuals|')
plt.title('Scale-Location Plot')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### Evaluating Model Performance

```python
# Split data for evaluation
X_train, X_test, y_train, y_test = train_test_split(
    X.drop('const', axis=1), y, test_size=0.2, random_state=42
)

# Fit on training data
X_train_sm = sm.add_constant(X_train)
model_train = sm.OLS(y_train, X_train_sm).fit()

# Predict on test data
X_test_sm = sm.add_constant(X_test)
y_pred = model_train.predict(X_test_sm)

# Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse:.4f}")
print(f"Root Mean Squared Error: {rmse:.4f}")
print(f"R-squared: {r2:.4f}")

# Visualize predictions
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Actual vs Predicted Values')
plt.grid(True, alpha=0.3)
plt.show()
```

### Common Issues and Solutions

**1. Multicollinearity**
```python
# Check for multicollinearity using correlation matrix
correlation_matrix = X.drop('const', axis=1).corr()
print("Correlation Matrix:")
print(correlation_matrix)

# High correlation (>0.8) indicates multicollinearity
# Solution: Remove one of the highly correlated variables or use regularization
```

**2. Non-linear Relationships**
```python
# If relationship is non-linear, consider:
# - Polynomial features
# - Transformations (log, sqrt)
# - Non-linear models
```

**3. Outliers**
```python
# Detect outliers using residuals
standardized_residuals = residuals / np.std(residuals)
outliers = np.abs(standardized_residuals) > 3

print(f"Number of outliers: {outliers.sum()}")
# Solution: Investigate outliers, consider robust regression
```

## 2. Logistic Regression

**Logistic regression** is used when the dependent variable is binary (0/1, Yes/No, Success/Failure). It models the probability of the outcome.

### Model Equation

The logistic function (sigmoid) transforms linear combination to probabilities:

$$P(y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + ... + \beta_n x_n)}}$$

Or in log-odds form:

$$\log\left(\frac{P(y=1)}{1-P(y=1)}\right) = \beta_0 + \beta_1 x_1 + ... + \beta_n x_n$$

### Assumptions of Logistic Regression

1. **Binary outcome**: Dependent variable is binary
2. **Independence**: Observations are independent
3. **Linearity**: Log-odds are linear in predictors
4. **No multicollinearity**: Predictors are not highly correlated
5. **Large sample size**: Generally need n ≥ 10 per predictor

### Building a Logistic Regression Model

```python
# Generate example data for logistic regression
np.random.seed(42)
n = 200

# Create features
X1 = np.random.randn(n)
X2 = np.random.randn(n)

# True relationship: log-odds = -1 + 2*X1 + 1.5*X2
log_odds = -1 + 2*X1 + 1.5*X2
prob = 1 / (1 + np.exp(-log_odds))  # Sigmoid function

# Generate binary outcome
y = (np.random.rand(n) < prob).astype(int)

# Prepare data
X = pd.DataFrame({'X1': X1, 'X2': X2})
X = sm.add_constant(X)

# Fit logistic regression model
logit_model = sm.Logit(y, X).fit()

# Print summary
print(logit_model.summary())
```

### Interpreting Logistic Regression Output

```python
# Coefficients are in log-odds scale
print("Coefficients (log-odds):")
print(logit_model.params)

# Convert to odds ratios
odds_ratios = np.exp(logit_model.params)
print("\nOdds Ratios:")
print(odds_ratios)

# Interpretation example
print(f"\nFor X1:")
print(f"  Coefficient: {logit_model.params['X1']:.4f}")
print(f"  Odds Ratio: {odds_ratios['X1']:.4f}")
print(f"  Interpretation: One unit increase in X1 multiplies odds by {odds_ratios['X1']:.4f}")
```

**Key Interpretations:**
- **Coefficients**: Change in log-odds for one-unit change in predictor
- **Odds Ratio**: Multiplicative change in odds (e^(coefficient))
- **Pseudo R-squared**: Measures model fit (McFadden's, Nagelkerke's)
- **Log-likelihood**: Measure of model fit (higher is better)

### Model Evaluation for Classification

```python
# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X.drop('const', axis=1), y, test_size=0.2, random_state=42, stratify=y
)

# Fit on training data
X_train_sm = sm.add_constant(X_train)
logit_train = sm.Logit(y_train, X_train_sm).fit()

# Predict probabilities
X_test_sm = sm.add_constant(X_test)
y_pred_proba = logit_train.predict(X_test_sm)

# Convert to binary predictions (using 0.5 threshold)
y_pred = (y_pred_proba >= 0.5).astype(int)

# Evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ROC Curve
from sklearn.metrics import roc_curve, auc
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.grid(True, alpha=0.3)
plt.show()
```

### Model Diagnostics for Logistic Regression

```python
# 1. Check for separation (perfect prediction)
# If model has very large coefficients, may indicate separation

# 2. Residuals analysis (deviance residuals)
deviance_residuals = logit_model.resid_dev

plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.scatter(logit_model.fittedvalues, deviance_residuals, alpha=0.6)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Fitted Values')
plt.ylabel('Deviance Residuals')
plt.title('Deviance Residuals vs Fitted Values')
plt.grid(True, alpha=0.3)

# 3. Influence measures
influence = logit_model.get_influence()
cooks_d = influence.cooks_distance[0]

plt.subplot(1, 2, 2)
plt.scatter(range(len(cooks_d)), cooks_d, alpha=0.6)
plt.axhline(y=4/len(cooks_d), color='r', linestyle='--', label='Threshold')
plt.xlabel('Observation')
plt.ylabel("Cook's Distance")
plt.title("Cook's Distance (Influence)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

## 3. Model Comparison and Selection

### Information Criteria

```python
# AIC (Akaike Information Criterion) - lower is better
# BIC (Bayesian Information Criterion) - lower is better

print("Linear Regression:")
print(f"  AIC: {model.aic:.2f}")
print(f"  BIC: {model.bic:.2f}")

print("\nLogistic Regression:")
print(f"  AIC: {logit_model.aic:.2f}")
print(f"  BIC: {logit_model.bic:.2f}")

# Compare models using AIC/BIC (only for same type of outcome)
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

# Using scikit-learn for easier cross-validation
lr_sklearn = LogisticRegression()
X_features = X.drop('const', axis=1)

# 5-fold cross-validation
cv_scores = cross_val_score(lr_sklearn, X_features, y, cv=5, scoring='accuracy')
print(f"Cross-validation scores: {cv_scores}")
print(f"Mean CV accuracy: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")
```

## Key Takeaways

1. **Linear regression** is for continuous outcomes; **logistic regression** is for binary outcomes.

2. **Always check assumptions** before interpreting results; violations can lead to incorrect conclusions.

3. **Model diagnostics** help identify problems like non-linearity, heteroscedasticity, and outliers.

4. **Interpret coefficients carefully**: 
   - Linear regression: change in outcome per unit change in predictor
   - Logistic regression: change in log-odds (or odds ratio) per unit change in predictor

5. **Use appropriate evaluation metrics**:
   - Regression: MSE, RMSE, R²
   - Classification: Accuracy, Precision, Recall, F1-score, ROC-AUC

6. **Cross-validation** helps assess model generalizability to new data.

## Applications in Data Science

- **Predictive modeling**: Forecast continuous or categorical outcomes
- **Feature importance**: Identify which predictors matter most
- **Causal inference**: Understand relationships (with caution)
- **Risk assessment**: Predict probabilities of events
- **A/B testing**: Compare treatment effects

## Next Steps

Now that you understand statistical models, you can explore:
- [Advanced Linear Algebra](06_linear_algebra_advanced.md) for dimensionality reduction techniques
- Machine Learning models for more complex relationships
- Time series models for temporal data

## Conclusion

Statistical models provide powerful tools for understanding relationships in data. This module covered:
- Building and interpreting linear regression models
- Building and interpreting logistic regression models
- Model diagnostics and assumption checking
- Model evaluation and comparison
- Common issues and solutions

Remember: A good model is not just about high R² or accuracy—it should be interpretable, generalizable, and based on sound statistical principles.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-dark"
        crossorigin="anonymous"
        async>
</script>
