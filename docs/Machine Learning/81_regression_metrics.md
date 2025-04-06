---
title: Regression Metrics
keywords: [Regression Metrics, Mean Absolute Error, Mean Square Error, Root Mean Squared Error, R-Squared (Coefficient of Determination)]
description: Learn several metrics to evaluate the performance of regression models
author: Juma Shafara
date: "2024-03"
---

![Photo by DATAIDEA](../../assets/banner4.png)

In regression tasks, the goal is to predict continuous numerical values. Scikit-learn provides several metrics to evaluate the performance of regression models. In this notebook, we will look at the following

- Mean Absolute Error
- Mean Square Error
- Root Mean Squared Error
- R-Squared (Coefficient of Determination)

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
# True labels
y_true = [2.5, 3.7, 5.1, 4.2, 6.8]
# Predicted labels
y_pred = [2.3, 3.5, 4.9, 4.0, 6.5]
```

## Mean Absolute Error (MAE):
   - MAE measures the average absolute errors between predicted values and actual values.
   - Imagine you're trying to hit a target with darts. The MAE is like calculating the average distance between where your darts hit and the bullseye. You just sum up how far each dart landed from the center (without caring if it was too short or too far) and then find the average. The smaller the MAE, the closer your predictions are to the actual values.
   - Formula: $$\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_{\text{true}} - y_{\text{pred}}|$$


```python
from sklearn.metrics import mean_absolute_error

# Calculate Mean Absolute Error (MAE)
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error (MAE):", mae)
```

    Mean Absolute Error (MAE): 0.21999999999999992


## Mean Squared Error (MSE):
   - MSE measures the average of the squares of the errors between predicted values and actual values.
   - This is similar to MAE, but instead of just adding up the distances, you square them before averaging. Squaring makes bigger differences more noticeable (by making them even bigger), so MSE penalizes larger errors more than smaller ones.
   - Formula: $$\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_{\text{true}} - y_{\text{pred}})^2$$


```python
from sklearn.metrics import mean_squared_error

# Calculate Mean Squared Error (MSE)
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error (MSE):", mse)
```

    Mean Squared Error (MSE): 0.04999999999999997


## Root Mean Squared Error (RMSE):
   - RMSE is the square root of the MSE, providing a more interpretable scale since it's in the same units as the target variable.
   - It's just like MSE, but we take the square root of the result. This brings the error back to the same scale as the original target variable, which makes it easier to interpret. RMSE gives you an idea of how spread out your errors are in the same units as your data.
   - Formula: $$\text{RMSE} = \sqrt{\text{MSE}}$$


```python
from sklearn.metrics import root_mean_squared_error

# Calculate Root Mean Squared Error (RMSE)
rmse = root_mean_squared_error(y_true, y_pred,)
print("Root Mean Squared Error (RMSE):", rmse)
```

    Root Mean Squared Error (RMSE): 0.2236067977499789


## R-squared (Coefficient of Determination)**:
   - R-squared measures the proportion of the variance in the dependent variable that is predictable from the independent variables.
   - This tells you how well your model's predictions match the actual data compared to a simple average. If R-squared is 1, it means your model perfectly predicts the target variable. If it's 0, it means your model is no better than just predicting the mean of the target variable. So, the closer R-squared is to 1, the better your model fits the data.
   - Formula: $$R^2 = 1 - \frac{\sum_{i=1}^{n} (y_{\text{true}} - y_{\text{pred}})^2}{\sum_{i=1}^{n} (y_{\text{true}} - \bar{y}_{\text{true}})^2}$$
   
   - where $$ \bar{y}_{\text{true}}$$ is the mean of the observed data.



```python
from sklearn.metrics import r2_score

# Calculate R-squared (Coefficient of Determination)
r2 = r2_score(y_true, y_pred)
print("R-squared (R2 Score):", r2)
```

    R-squared (R2 Score): 0.975896644812958


Understanding these metrics can help you assess the performance of your regression model and make necessary adjustments to improve its accuracy.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
