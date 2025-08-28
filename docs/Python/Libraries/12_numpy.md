---
title: Numpy Crash Course
author: Juma Shafara
date: "2024-01"
date-modified: "2024-08-14"
description: This crash course will teach you the basics and intermediate concepts of the Numpy Library
keywords: [numpy, data types, array mathematics, aggregate functions, Subsetting, Slicing, Indexing]
---


<!-- ![Photo by DATAIDEA](../../assets/banner4.png) -->

## Objective

In this lesson, you will learn all you need to know to get moving with numpy. ie:

<ul class="cursored-list">
<li><a href="#what-is-numpy"><i class="bi bi-cursor"></i> What is Numpy</a></li> 
<li><a href="#inspecting-our-arrays"><i class="bi bi-cursor"></i> Inspecting Numpy arrays</a></li> 
<li><a href="#array-mathematics"><i class="bi bi-cursor"></i> Performing array mathematics</a></li> 
<li><a href="#subsetting-slicing-and-indexing"><i class="bi bi-cursor"></i> Subsetting, Slicing and Indexing arrays</a></li> 
<li><a href="#array-manipulation"><i class="bi bi-cursor"></i> Array manipulation</a></li> 
</ul>

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

## What is Numpy
<i class="bi bi-cursor"></i> Numpy is a python package used for scientific computing

<i class="bi bi-cursor"></i> Numpy provides arrays which are greater and faster alternatives to traditional python lists. An array is a group of elements of the same data type

<i class="bi bi-cursor"></i> A standard numpy array is required to have elements of the same data type.


```python
# Uncomment and run this cell to install numpy
# !pip install numpy
```

## Inspecting our arrays

To use numpy, we'll first import it (you must have it installed for this to work)


```python
# import numpy module
import numpy as np
```

We can check the version we'll be using by using the `__version__` method


```python
# checking the numpy version
np.__version__
```




    '1.26.3'



Numpy gives us a more powerful Python List alternative data structure called a Numpy ndarray, we creat it using the `array()` from numpy


```python
# creating a numpy array
num_arr = np.array([1, 2, 3, 4])
```

The object that's created by `array()` is called `ndarray`.
This can be shown by checking the type of the object using `type()`


```python
# Checking type of object
type(num_arr)
```




    numpy.ndarray



#### Data Types
The table below describes some of the most common data types we use in numpy

Data Type | Description
----------|-----------
`np.int64`|Signed 64-bit integer types
`np.float32`|Standard double-precision floating point
`np.complex`|Complex numbers represented by 128 floats
`np.bool`|Boolean type storing `True` and `False` values
`np.object`|Python object type
`np.string_`|Fixed-length string type
`np.unicode_`|Fixed-length unicode type

We can check the shape of a numpy array by using the `shape` attribute as demonstrated below


```python
# shape of array
num_arr.shape
```




    (4,)



**Dimensions**

Similarly, we find the the number of dimensions in our array using the `ndim` attribute. A dimension in NumPy refers to the number of axes or levels of depth in an array, determining its shape (e.g., 2D for a matrix, 3D for a tensor).


```python
# finding the number of dimensions
num_arr.ndim
```




    1



**Length**

In NumPy, the length refers to the size of the first axis (dimension) of an array, which is the number of elements along that axis. We can use the `len()` method to find the length.


```python
# number of elements in array
len(num_arr)
```




    4



**Size**

Size in NumPy refers to the total number of elements in an array across all dimensions. We can use the size of a numpy array using the `size` attribute


```python
# another way to get the number of elements
num_arr.size
```




    4



**Data Type**(`dtype`)

`dtype` in NumPy refers to the data type of the elements stored in an array, such as `int`, `float`, `bool`, etc.


```python
# finding data type of array elements
print(num_arr.dtype.name)
```

    int64


**Converting Array Data Types**

We cas use `astype()` method to convert an array from one type to another.


```python
# converting an array
float_arr = np.array([1.2, 3.5, 7.0])

# use astype() to convert to a specific
int_arr = float_arr.astype(int)

print(f'Array: {float_arr}, Data Type: {float_arr.dtype}')
print(f'Array: {int_arr}, Data Type: {int_arr.dtype}')
```

    Array: [1.2 3.5 7. ], Data Type: float64
    Array: [1 3 7], Data Type: int64


### Ask for help


```python
np.info(np.ndarray.shape)
```


```python
?np.ndarray.shape
```

## Array mathematics

Numpy has out of the box tools to help us perform some import mathematical operations

#### Arithmetic Operations

Arithmetic operations in NumPy are element-wise operations like addition, subtraction, multiplication, and division that can be performed directly between arrays or between an array and a scalar.


```python
# creating arrays
array1 = np.array([1, 4, 6, 7])
array2 = np.array([3, 5, 3, 1])
```


```python
# subtract
difference1 = array2 - array1
print('difference1 =', difference1)

# another way
difference2 = np.subtract(array2, array1)
print('difference2 =', difference2)
```

As we may notice, numpy does element-wise operations for ordinary arithmetic operations


```python
# sum
summation1 = array1 + array2
print('summation1 =', summation1)

# another way
summation2 = np.add(array1, array2)
print('summation2 =', summation2)
```

#### Trigonometric operations

Trigonometric operations in NumPy are functions like `np.sin()`, `np.cos()`, and `np.tan()` that perform element-wise trigonometric calculations on arrays.


```python
# sin
print('sin(array1) =', np.sin(array1))
# cos
print('cos(array1) =', np.cos(array1))
# log
print('log(array1) =', np.log(array1))
```


```python
# dot product
array1.dot(array2)
```

Given matrices A and B, the `dot` operation mulitiplies A with the transpose of B

**Research:**

<i class="bi bi-cursor"></i> another way to dot matrices (arrays)

#### Comparison

In NumPy, comparison operators perform element-wise comparisons on arrays and return boolean arrays of the same shape, where each element indicates True or False based on the corresponding element-wise comparison.


```python
array1 == array2
```


```python
array1 > 3
```

#### Aggregate functions

NumPy provides several aggregate functions that perform operations across the elements of an array and return a single scalar value.


```python
# average
mean = array1.mean()
print('Mean: ', mean)

# min
minimum = array1.min()
print('Minimum: ', minimum)

# max
maximum = array1.max()
print('Maximum: ', maximum)

# corrcoef
correlation_coefficient = np.corrcoef(array1, array2)
print('Correlation Coefficient: ', correlation_coefficient)

standard_deviation = np.std(array1)
print('Standard Deviation: ', standard_deviation)
```

**Research:**

<i class="bi bi-cursor"></i> copying arrays (you might meet `view()`, `copy()`) 

## Subsetting, Slicing and Indexing
<i class="bi bi-cursor"></i> Indexing is the technique we use to access individual elements in an array. 0 represents the first element, 1 the represents second element and so on.

<i class="bi bi-cursor"></i> Slicing is used to access elements of an array using a range of two indexes. The first index is the start of the range while the second index is the end of the range. The indexes are separated by a colon ie `[start:end]`


```python
# Creating numpy arrays of different dimension
# 1D array
arr1 = np.array([1, 4, 6, 7])
print('Array1 (1D): \n', arr1)

# 2D array
arr2 = np.array([[1.5, 2, 3], [4, 5, 6]]) 
print('Array2 (2D): \n', arr2)

#3D array
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                 [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]) 
print('Array3 (3D): \n', arr3)
```

    Array1 (1D): 
     [1 4 6 7]
    Array2 (2D): 
     [[1.5 2.  3. ]
     [4.  5.  6. ]]
    Array3 (3D): 
     [[[ 1  2  3]
      [ 4  5  6]
      [ 7  8  9]]
    
     [[10 11 12]
      [13 14 15]
      [16 17 18]]]



```python
# find the dimensions of an array
print('Array1 (1D):', arr1.shape)
print('Array2 (2D):', arr2.shape)
print('Array3 (3D):', arr3.shape)
```

    Array1 (1D): (4,)
    Array2 (2D): (2, 3)
    Array3 (3D): (2, 3, 3)


#### Indexing


```python
# accessing items in a 1D array
arr1[2]
```




    6




```python
# accessing items in 2D array
arr2[1, 2]
```




    6.0




```python
# accessing in a 3D array
arr3[0, 1, 2]
```




    6



#### slicing


```python
# slicing 1D array
arr1[0:3]
```




    array([1, 4, 6])




```python
# slicing a 2D array
arr2[1, 1:]
```




    array([5., 6.])




```python
# slicing a 3D array
first = arr3[0, 2]
second = arr3[1, 0]

np.concatenate((first, second))
```




    array([ 7,  8,  9, 10, 11, 12])



#### Boolean Indexing

Boolean indexing in NumPy allows you to select elements from an array based on a boolean condition or a boolean array of the same shape. The elements corresponding to True values in the boolean array/condition are selected, while those corresponding to False are discarded. 


```python
# boolean indexing
arr1[arr1 < 5]
```

**Research:**

<i class="bi bi-cursor"></i> Fancy Indexing

## Array manipulation

NumPy provides a wide range of functions that allow you to change the shape, dimensions, and structure of arrays to suit your needs


```python
print(arr2)
```

    [[1.5 2.  3. ]
     [4.  5.  6. ]]



```python
# transpose
arr2_transpose1 = np.transpose(arr2) 
print('Transpose1: \n', arr2_transpose1)

# another way
arr2_transpose2 = arr2.T
print('Transpose2: \n', arr2_transpose2)
```

    Transpose1: 
     [[1.5 4. ]
     [2.  5. ]
     [3.  6. ]]
    Transpose2: 
     [[1.5 4. ]
     [2.  5. ]
     [3.  6. ]]



```python
# combining arrays
first = arr3[0, 2]
second = arr3[1, 0]

np.concatenate((first, second))
```




    array([ 7,  8,  9, 10, 11, 12])




```python
test_arr1 = np.array([[7, 8, 9], [10, 11, 12]])
test_arr2 = np.array([[1, 2, 3], [4, 5, 6]])

np.concatenate((test_arr1, test_arr2), axis=1)
```




    array([[ 7,  8,  9,  1,  2,  3],
           [10, 11, 12,  4,  5,  6]])



### Some homework

**Research:**
    
Adding/Removing Elements
<i class="bi bi-cursor"></i>  `resize()`

<i class="bi bi-cursor"></i>  `append()`

<i class="bi bi-cursor"></i>  `insert()`

<i class="bi bi-cursor"></i>  `delete()`
  
Changing array shape
<i class="bi bi-cursor"></i>  `ravel()`

<i class="bi bi-cursor"></i>  `reshape()`


```python
# stacking 
# np.vstack((a,b))
# np.hstack((a,b))
# np.column_stack((a,b))
# np.c_[a, b]
```


```python
# splitting arrays
# np.hsplit()
# np.vsplit()
```

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>


