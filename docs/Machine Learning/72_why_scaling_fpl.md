---
title: Why re-scale data (fpl)? 
author: Juma Shafara
keywords: [kmeans clustering, re-scaling data, standard scaler]
description: In this notebook, we’ll use Kmeans clustering to demonstrate the importance of scaling data
date: "2024-04"
---

![Photo by DATAIDEA](../../../assets/banner4.png)

In this notebook, we'll use **Kmeans clustering** to demonstrate the importance of scaling data

**K-means clustering** is an unsupervised machine learning algorithm used for partitioning a dataset into K distinct, non-overlapping clusters. The goal of K-means is to minimize the sum of squared distances between data points and their respective cluster centroids.

Here's how the K-means algorithm works:

1. Pick K random objects as the initial cluster centers.
2. Classify each object into the cluster whose center is closest to the point.
3. For each cluster of classified objects, compute the centroid (mean).
4. Now reclassify each object using the centroids as cluster centers.
5. Calculate the total variance of the clusters (this is the measure of goodness).
6. Repeat steps 1 to 6 a few more times and pick the cluster centers with the lowest total variance.

Here's a video showing the above steps: https://www.youtube.com/watch?v=4b5d3muPQmA

First, let's import the necessary libraries and load the Iris dataset:


```python
from dataidea.packages import pd, plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from dataidea.datasets import loadDataset
```


```python
fpl_data = loadDataset('fpl')
```

We can be able to load it like this because it inbuilt in the dataidea package

Now let's pick out a few numeric columns that we might consider moving forward


```python
fpl_sample = fpl_data[['Goals_Scored', 'Assists','Total_Points', 
                       'Minutes', 'Saves', 'Goals_Conceded', 
                       'Creativity', 'Influence'
                      ]]
```


```python
fpl_sample.head()
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
      <th>Goals_Scored</th>
      <th>Assists</th>
      <th>Total_Points</th>
      <th>Minutes</th>
      <th>Saves</th>
      <th>Goals_Conceded</th>
      <th>Creativity</th>
      <th>Influence</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>14</td>
      <td>244</td>
      <td>3101</td>
      <td>0</td>
      <td>36</td>
      <td>1414.9</td>
      <td>1292.6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>23</td>
      <td>14</td>
      <td>242</td>
      <td>3083</td>
      <td>0</td>
      <td>39</td>
      <td>659.1</td>
      <td>1318.2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>22</td>
      <td>6</td>
      <td>231</td>
      <td>3077</td>
      <td>0</td>
      <td>41</td>
      <td>825.7</td>
      <td>1056.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>17</td>
      <td>11</td>
      <td>228</td>
      <td>3119</td>
      <td>0</td>
      <td>36</td>
      <td>1049.9</td>
      <td>1052.2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>17</td>
      <td>11</td>
      <td>194</td>
      <td>3052</td>
      <td>0</td>
      <td>50</td>
      <td>371.0</td>
      <td>867.2</td>
    </tr>
  </tbody>
</table>
</div>



## Clustering without Scaling

Next, let's perform K-means clustering on the original dataset without scaling the features:


```python
# Apply K-means clustering without scaling
kmeans_unscaled = KMeans(n_clusters=4, random_state=42)
kmeans_unscaled.fit(fpl_sample)

# Get the cluster centers and labels
centroids_unscaled = kmeans_unscaled.cluster_centers_
labels_unscaled = kmeans_unscaled.labels_
```

Let's see the performance


```python
# Visualize clusters without scaling
plt.figure(figsize=(10, 6))

plt.scatter(fpl_sample.Assists, fpl_sample.Goals_Scored, c=labels_unscaled, cmap='viridis',)

plt.show()
```


    
![png](output_16_0.png)
    


You'll notice that the clusters may not seem well-separated or meaningful. This is because the features of the Iris dataset have different scales, 

## Clustering after Scaling

Now, let's repeat the process after scaling the features using StandardScaler:


```python
# Scale the features
scaler = StandardScaler()
fpl_sample_scaled = scaler.fit_transform(fpl_sample)

# Transform scaled features back to DataFrame
fpl_sample_scaled_dataframe = pd.DataFrame(fpl_sample_scaled, columns=fpl_sample.columns)

# Apply K-means clustering on scaled features
kmeans_scaled = KMeans(n_clusters=4, random_state=42)
kmeans_scaled.fit(fpl_sample_scaled)

# Get the cluster centers and labels
centroids_scaled = kmeans_scaled.cluster_centers_
labels_scaled = kmeans_scaled.labels_
```


```python
# Visualize clusters without scaling
plt.figure(figsize=(10, 6))

plt.scatter(fpl_sample_scaled_dataframe.Assists, 
            fpl_sample_scaled_dataframe.Goals_Scored, 
            c=labels_scaled, cmap='viridis')

plt.show()
```


    
![png](output_21_0.png)
    


You should see clearer and more meaningful clusters after scaling the features, demonstrating the importance of feature scaling for K-means clustering, especially when dealing with datasets with features of different scales.

## Take away

If the data doesn't follow a standard scale, meaning the features have different scales or variances, it can lead to some issues when applying K-means clustering:

1. **Unequal feature influence**: Features with larger scales or variances can dominate the clustering process. Since K-means relies on Euclidean distance, features with larger scales will contribute more to the distance calculation, potentially biasing the clustering results towards those features.

2. **Incorrect cluster shapes**: K-means assumes that clusters are isotropic (spherical) and have similar variances along all dimensions. If the data has features with different scales, clusters may be stretched along certain dimensions, leading to suboptimal cluster assignments.

3. **Convergence speed**: Features with larger scales can cause centroids to move more quickly towards areas with denser data, potentially affecting the convergence speed of the algorithm.

By scaling the data before clustering, you ensure that each feature contributes equally to the distance calculations, helping to mitigate the issues associated with different feature scales. This can lead to more accurate and reliable clustering results.

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

<p class=pb-1>
To be among the first to hear about future updates, simply enter your email below, follow us on <a href="https://x.com/dataideaorg"><i class="bi bi-twitter-x"></i>
 (formally Twitter)</a>, or subscribe to our <a href="https://www.youtube.com/@dataidea-science"><i class="bi bi-youtube"></i> YouTube channel</a>.
</p>
<iframe src="https://embeds.beehiiv.com/5fc7c425-9c7e-4e08-a514-ad6c22beee74?slim=true" data-test-id="beehiiv-embed" height="52" frameborder="0" scrolling="no" style="margin: 0; border-radius: 0px !important; background-color: transparent; width: 100%;" ></iframe>
