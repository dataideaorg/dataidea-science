---
title: Probability Foundations
author: Juma Shafara
date: "2025-02-09"
date-modified: "2025-02-09"
description: Learn fundamental probability theory including sample spaces, conditional probability, Bayes' theorem, and independence with Python examples.
keywords: [probability, conditional probability, Bayes theorem, independence, sample space, events, data science]
---

![Photo by DATAIDEA](../../../assets/banner4.png)

## Introduction

Probability is the foundation of statistics and data science. It provides the mathematical framework for quantifying uncertainty and making predictions based on data. This module covers essential probability concepts that you'll use throughout your data science journey.

## Learning Objectives

By the end of this module, you will be able to:

- Understand and work with sample spaces and events
- Calculate probabilities using basic probability rules
- Apply conditional probability to solve real-world problems
- Use Bayes' theorem for probabilistic reasoning
- Identify and work with independent events
- Apply probability concepts using Python

## Prerequisites

Before starting this module, you should be familiar with:
- Basic Python programming
- Set theory basics (union, intersection)
- [Descriptive Statistics](02_descriptive_statistics.md) concepts

## 1. Sample Spaces and Events

### Sample Space

A **sample space** (denoted by S or Ω) is the set of all possible outcomes of a random experiment.

**Example:** When flipping a coin, the sample space is S = {Heads, Tails}

```python
# Sample space for a coin flip
sample_space_coin = {'Heads', 'Tails'}
print("Sample space for coin flip:", sample_space_coin)

# Sample space for rolling a die
sample_space_die = {1, 2, 3, 4, 5, 6}
print("Sample space for die roll:", sample_space_die)
```

### Events

An **event** is a subset of the sample space. It represents a collection of outcomes we're interested in.

**Example:** When rolling a die, the event "rolling an even number" is E = {2, 4, 6}

```python
# Event: rolling an even number
sample_space = {1, 2, 3, 4, 5, 6}
even_numbers = {2, 4, 6}
print("Event: Even numbers =", even_numbers)

# Event: rolling a number greater than 4
greater_than_4 = {5, 6}
print("Event: Numbers > 4 =", greater_than_4)
```

## 2. Basic Probability Rules

### Probability of an Event

The probability of an event E, denoted P(E), is a number between 0 and 1 that represents the likelihood of that event occurring.

**Key Properties:**
- 0 ≤ P(E) ≤ 1
- P(S) = 1 (probability of sample space is always 1)
- P(∅) = 0 (probability of impossible event is 0)

### Classical Probability

For equally likely outcomes, the probability of an event E is:

$$P(E) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}$$

```python
# Probability of rolling an even number on a fair die
sample_space = {1, 2, 3, 4, 5, 6}
even_numbers = {2, 4, 6}

# Classical probability
prob_even = len(even_numbers) / len(sample_space)
print(f"P(Even number) = {prob_even}")
```

### Complement Rule

The probability of the complement of event E (not E) is:

$$P(E^c) = 1 - P(E)$$

```python
# Probability of NOT rolling an even number
prob_not_even = 1 - prob_even
print(f"P(Not even) = {prob_not_even}")
```

### Addition Rule

For two events A and B:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

If A and B are mutually exclusive (cannot occur together):

$$P(A \cup B) = P(A) + P(B)$$

```python
# Example: Probability of rolling an even number OR a number greater than 4
sample_space = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6}
greater_than_4 = {5, 6}

# Intersection (numbers that are both even AND > 4)
intersection = even & greater_than_4  # {6}
print(f"Intersection: {intersection}")

# Union (numbers that are even OR > 4)
union = even | greater_than_4  # {2, 4, 5, 6}
print(f"Union: {union}")

# Using addition rule
prob_even = len(even) / len(sample_space)
prob_gt4 = len(greater_than_4) / len(sample_space)
prob_intersection = len(intersection) / len(sample_space)

prob_union = prob_even + prob_gt4 - prob_intersection
print(f"P(Even OR > 4) = {prob_union}")

# Verify by direct calculation
prob_union_direct = len(union) / len(sample_space)
print(f"Direct calculation: {prob_union_direct}")
```

## 3. Conditional Probability

**Conditional probability** is the probability of an event occurring given that another event has already occurred.

The conditional probability of A given B is:

$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

where P(B) > 0.

```python
import numpy as np

# Example: Probability of drawing a heart given that we drew a red card
# In a standard deck: 52 cards, 26 red (13 hearts + 13 diamonds), 13 hearts

# P(Heart | Red) = P(Heart ∩ Red) / P(Red)
# Since all hearts are red: P(Heart ∩ Red) = P(Heart) = 13/52
# P(Red) = 26/52

prob_heart_given_red = (13/52) / (26/52)
print(f"P(Heart | Red) = {prob_heart_given_red}")

# Example with data
# Simulating card draws
np.random.seed(42)
deck = ['H'] * 13 + ['D'] * 13 + ['C'] * 13 + ['S'] * 13  # Hearts, Diamonds, Clubs, Spades
red_cards = ['H'] * 13 + ['D'] * 13

# Simulate drawing cards
n_simulations = 10000
red_draws = 0
heart_given_red = 0

for _ in range(n_simulations):
    card = np.random.choice(deck)
    if card in red_cards:
        red_draws += 1
        if card == 'H':
            heart_given_red += 1

# Empirical conditional probability
if red_draws > 0:
    emp_prob = heart_given_red / red_draws
    print(f"Empirical P(Heart | Red) ≈ {emp_prob:.3f}")
```

### Real-World Example: Medical Testing

```python
# Example: Disease testing
# Suppose 1% of population has a disease
# Test is 99% accurate (99% true positive, 99% true negative)

# P(Disease) = 0.01
# P(Test Positive | Disease) = 0.99
# P(Test Negative | No Disease) = 0.99

prob_disease = 0.01
prob_positive_given_disease = 0.99
prob_negative_given_no_disease = 0.99

# P(Test Positive | No Disease) = 1 - P(Test Negative | No Disease)
prob_positive_given_no_disease = 1 - prob_negative_given_no_disease

# P(Test Positive) using law of total probability
prob_positive = (prob_positive_given_disease * prob_disease + 
                prob_positive_given_no_disease * (1 - prob_disease))

print(f"P(Test Positive) = {prob_positive:.4f}")
```

## 4. Bayes' Theorem

**Bayes' theorem** allows us to update probabilities based on new information. It's fundamental to many machine learning algorithms and statistical inference.

$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

Where:
- P(A|B) is the posterior probability
- P(B|A) is the likelihood
- P(A) is the prior probability
- P(B) is the marginal probability

```python
# Continuing the medical testing example
# What is P(Disease | Test Positive)?

# Using Bayes' theorem
# P(Disease | Test Positive) = P(Test Positive | Disease) * P(Disease) / P(Test Positive)

prob_disease_given_positive = (prob_positive_given_disease * prob_disease) / prob_positive

print(f"P(Disease | Test Positive) = {prob_disease_given_positive:.4f}")
print(f"\nEven with a 99% accurate test, if you test positive,")
print(f"there's only a {prob_disease_given_positive*100:.1f}% chance you actually have the disease!")
print(f"This is because the disease is rare (1% prevalence).")
```

### Law of Total Probability

Before using Bayes' theorem, we often need to calculate P(B) using the law of total probability:

$$P(B) = P(B|A_1) \cdot P(A_1) + P(B|A_2) \cdot P(A_2) + ... + P(B|A_n) \cdot P(A_n)$$

where A₁, A₂, ..., Aₙ form a partition of the sample space.

```python
# Example: Probability of drawing different colored balls from urns
# Urn 1: 3 red, 2 blue
# Urn 2: 1 red, 4 blue
# We randomly select an urn (50% chance each), then draw a ball

# P(Red) = P(Red | Urn1) * P(Urn1) + P(Red | Urn2) * P(Urn2)
prob_urn1 = 0.5
prob_urn2 = 0.5

prob_red_given_urn1 = 3/5  # 3 red out of 5 total
prob_red_given_urn2 = 1/5  # 1 red out of 5 total

prob_red = prob_red_given_urn1 * prob_urn1 + prob_red_given_urn2 * prob_urn2
print(f"P(Red) = {prob_red}")

# Now, if we draw a red ball, what's the probability it came from Urn 1?
# P(Urn1 | Red) = P(Red | Urn1) * P(Urn1) / P(Red)
prob_urn1_given_red = (prob_red_given_urn1 * prob_urn1) / prob_red
print(f"P(Urn1 | Red) = {prob_urn1_given_red:.3f}")
```

## 5. Independence

Two events A and B are **independent** if the occurrence of one does not affect the probability of the other:

$$P(A \cap B) = P(A) \cdot P(B)$$

Equivalently:

$$P(A|B) = P(A)$$

```python
# Example: Independent events
# Flipping a coin and rolling a die are independent

prob_heads = 0.5
prob_six = 1/6

# P(Heads AND Six) = P(Heads) * P(Six) (if independent)
prob_both = prob_heads * prob_six
print(f"P(Heads AND Six) = {prob_both}")

# Example: Dependent events
# Drawing two cards from a deck without replacement
# P(Second card is Ace | First card is Ace) ≠ P(Second card is Ace)

# First draw
prob_first_ace = 4/52  # 4 aces in 52 cards

# If first card is an ace, 3 aces remain in 51 cards
prob_second_ace_given_first = 3/51

# If first card is not an ace, 4 aces remain in 51 cards
prob_second_ace_given_not_first = 4/51

print(f"\nDependent events:")
print(f"P(Second Ace | First Ace) = {prob_second_ace_given_first:.4f}")
print(f"P(Second Ace | First Not Ace) = {prob_second_ace_given_not_first:.4f}")
print(f"These are different, so the events are dependent!")
```

## 6. Common Probability Distributions

### Discrete Distributions

**Uniform Distribution (Discrete)**
- All outcomes are equally likely
- Example: Rolling a fair die

```python
import matplotlib.pyplot as plt
import numpy as np

# Uniform distribution for a fair die
outcomes = [1, 2, 3, 4, 5, 6]
probabilities = [1/6] * 6

plt.bar(outcomes, probabilities, color='skyblue', edgecolor='black')
plt.title('Uniform Distribution: Fair Die')
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.ylim(0, 0.2)
plt.show()
```

**Binomial Distribution**
- Models the number of successes in n independent trials
- Parameters: n (number of trials), p (probability of success)

```python
from scipy.stats import binom

# Binomial: Number of heads in 10 coin flips
n, p = 10, 0.5
x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y, color='lightgreen', edgecolor='black', alpha=0.7)
plt.title('Binomial Distribution: 10 Coin Flips')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.show()
```

### Continuous Distributions

**Normal Distribution**
- Bell-shaped, symmetric distribution
- Parameters: μ (mean), σ (standard deviation)

```python
from scipy.stats import norm

# Normal distribution
mu, sigma = 0, 1
x = np.linspace(-4, 4, 100)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, 'b-', linewidth=2)
plt.title('Normal Distribution (μ=0, σ=1)')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.show()
```

## Key Takeaways

1. **Sample spaces** contain all possible outcomes; **events** are subsets of interest.

2. **Conditional probability** P(A|B) represents the probability of A given B has occurred.

3. **Bayes' theorem** allows us to update probabilities with new information, which is fundamental to many machine learning algorithms.

4. **Independent events** don't affect each other's probabilities: P(A ∩ B) = P(A) · P(B).

5. **Probability distributions** describe how probabilities are distributed across outcomes.

## Applications in Data Science

- **Naive Bayes classifiers** use Bayes' theorem for classification
- **Bayesian inference** updates beliefs with evidence
- **A/B testing** uses probability to make decisions
- **Risk assessment** in finance and insurance
- **Recommendation systems** use probabilistic models

## Next Steps

Now that you understand probability foundations, you're ready to learn about [Inferential Statistics](04_inferential_statistics.md), where we'll use probability to make inferences about populations from samples.

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-dark"
        crossorigin="anonymous"
        async>
</script>

