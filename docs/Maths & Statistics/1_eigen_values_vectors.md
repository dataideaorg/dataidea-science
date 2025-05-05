## **Lesson: Understanding Eigenvalues and Eigenvectors**

### **Learning Objectives**

By the end of this lesson, you will be able to:

* Define eigenvalues and eigenvectors.
* Compute eigenvalues and eigenvectors of a 2x2 matrix.
* Understand the significance of these concepts in linear algebra and data science.

---

### **What Are Eigenvalues and Eigenvectors?**

Let’s consider a square matrix $A$. An **eigenvector** $\vec{v}$ and its corresponding **eigenvalue** $\lambda$ satisfy the equation:

$$
A \vec{v} = \lambda \vec{v}
$$

Where:

* $A$ is an $n \times n$ matrix.
* $\vec{v}$ is a **non-zero** vector.
* $\lambda$ is a **scalar** (just a number).

💡 **Intuition**: The vector $\vec{v}$ doesn't change its direction when multiplied by matrix $A$; it only gets stretched or compressed by $\lambda$.

---

### **Step-by-Step Computation**

Let’s work with this matrix:

$$
A = \begin{bmatrix}
2 & 1 \\
1 & 2
\end{bmatrix}
$$

---

### **Step 1: Characteristic Equation**

To find the eigenvalues, we solve:

$$
\det(A - \lambda I) = 0
$$

Where $I$ is the identity matrix. Subtract $\lambda I$ from $A$:

$$
A - \lambda I = 
\begin{bmatrix}
2 - \lambda & 1 \\
1 & 2 - \lambda
\end{bmatrix}
$$

Compute the determinant:

$$
\det = (2 - \lambda)^2 - 1 = \lambda^2 - 4\lambda + 3
$$

Solve the characteristic equation:

$$
\lambda^2 - 4\lambda + 3 = 0
\Rightarrow \lambda = 3 \text{ or } 1
$$

---

### **Step 2: Find Eigenvectors**

#### For $\lambda = 3$:

Solve $(A - 3I)\vec{v} = 0$:

$$
\begin{bmatrix}
-1 & 1 \\
1 & -1
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
= 0
\Rightarrow -x + y = 0 \Rightarrow y = x
$$

So the eigenvector is any scalar multiple of:

$$
\vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}
$$

---

#### For $\lambda = 1$:

Solve $(A - I)\vec{v} = 0$:

$$
\begin{bmatrix}
1 & 1 \\
1 & 1
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
= 0
\Rightarrow x + y = 0 \Rightarrow y = -x
$$

So the eigenvector is any scalar multiple of:

$$
\vec{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
$$

---

### **Final Result**

* **Eigenvalues**:

  $$
  \lambda_1 = 3, \quad \lambda_2 = 1
  $$

* **Eigenvectors**:

  $$
  \vec{v}_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}, \quad \vec{v}_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}
  $$

---

### **Why It Matters (Applications)**

* In **Principal Component Analysis (PCA)**, we use eigenvectors of the covariance matrix to identify directions of maximum variance.
* In **machine learning**, eigenvalues help reduce dimensionality and noise.
* In **differential equations**, eigenvalues determine system stability.

---

### **Step 3: Implement in Python**

Let’s verify our work using Python and NumPy.

```python
import numpy as np

# Define the matrix A
A = np.array([[2, 1],
              [1, 2]])

# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Display results
print("Eigenvalues:")
print(eigenvalues)

print("\nEigenvectors (columns):")
print(eigenvectors)
```

---

### **Expected Output**

The output should be:

```
Eigenvalues:
[3. 1.]

Eigenvectors (columns):
[[ 0.70710678 -0.70710678]
 [ 0.70710678  0.70710678]]
```

💡 **Note**:

* The eigenvectors are normalized (unit vectors).
* The columns of the output matrix are the eigenvectors corresponding to each eigenvalue.

---

### **Interpreting the Output**

* **Eigenvalues**: `3` and `1` match our manual calculation.
* **Eigenvectors**:

  * The first column $\begin{bmatrix} 0.707 \\ 0.707 \end{bmatrix}$ is equivalent to $\begin{bmatrix} 1 \\ 1 \end{bmatrix}$ normalized.
  * The second column $\begin{bmatrix} -0.707 \\ 0.707 \end{bmatrix}$ corresponds to $\begin{bmatrix} 1 \\ -1 \end{bmatrix}$ normalized.

---

### **Key Takeaway**

Python can be used to quickly and accurately compute eigenvalues and eigenvectors, which is especially helpful for larger matrices or data sets.
