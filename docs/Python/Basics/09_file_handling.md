---
title: Python File Handling
description: Python allows us to read, write, create and delete files.
keywords: [Python File Handling, creating files in python, deleting files in python, modifying files in python, reading files in python]
author: Juma Shafara
date: "2023-11"
---

![Photo by DATAIDEA](../../assets/banner4.png)

Python allows us to read, write, create and delete files. This process is called file handling. This is what we will discuss in this lesson

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

### The `open()` function
The `open()` function allows us to read, create and update files

It takes 2 parameters:

- `file` - the file or file path to be opened
- `mode` - the mode in which a file is opened for

The mode is a string that can either be any of the following:

Mode  | Meaning
------|--------
`'r'` | Open a file for reading
`'w'` | Open a file for writing, creates the file if it does not exist
`'a'` | Open a file for writing, appends to the end of the file
`'x'` | Open a file for creating, fails if file already exists

## Python File reading
To better explain this, let us say we have a folder named `my_folder`.

Inside `my_folder` we have the following files:

- `demo.txt`
- `main_code.py`

The content of the `demo.txt` file is the following

```
Hello World!
I love Python
```
Now our goal is to read the content of the `demo.txt` file and then print it using the `main_code.py` file

To achieve this, we will use the `open()` function with `'r'` mode.


```python
# this is main code

file = open(
    file='demo.txt',
    mode='r'
)
content = file.read()
print(content)
```

    Hello World!
    I love Python


### Reading Lines

We can also read each line using the `readline()` method.


```python
# this is main_code.py

file = open(
    file='demo.txt',
    mode='r'
)

first_line = file.readline()
second_line = file.readline()

print('First line:', first_line)
print('Second line:', second_line)
```

    First line: Hello World!
    
    Second line: I love Python


## Writing a File
In simplest terms, writing a file means modifying the content of a file or creating it if it doesnot exist yet.

In Python, there are 2 modes to write to file.

- `'w'` - overwrites content of a file, creates file if it does not exist
- `'a'` - appends content to the end of a file, creates the file if it does not exist

**Example**
To better explain this, lets say we have a folder named `my_folder`. Inside `my_folder` we have the following files

- `demo.txt`
- `main_code.py`

The content of the `demo.txt` file is the following

```
I love Python
```
In this example, we will use the `'w'` mode which will overwrite(replace) the content of the file


```python
# this is main_code.py

file = open(
    file='demo.txt',
    mode='w'
)
file.write('I love JavaScript')
file.close()
```

When the above code is run, the content of the file `demo.txt` will be this:
```
I love JavaScript
```

Another example, this time we will use the `a` mode which will append or add content to the end of the file


```python
# this is main_code.py

file = open(
    file='demo.txt',
    mode='a'
)
file.write(' and JavaScript')
file.close()
```

When the above script is run, the content of the `demo.txt` file will be this:
```
I love Python and JavaScript
```

## Deleting a file
To delete a file, use the `os` module. The `os` modules contains the `remove()` method which we can use to delete files.


```python
# this is main_code.py

# import os

# os.remove('demo.txt')
```

## Exercise

24. Develop a simple telephone directory which saves your friends contact information in a
file named directory.txt. The program should have a menu similar to the following:
```
----------------Menu-------------------------
1. Add new friend.
2. Display contact info.
3. Exit
------------------------------------------------
Enter menu number:
```
When you press “1” it should request you to enter following data:
```
---------New friend info--------
Name : Saman
Phone-No: 011-2123456
e-Mail : saman@cse.mrt.ac.lk
```
After adding new contact information it should again display the menu. When you press “2” it should
display all the contact information stored in the directory.txt file as follows:

```
--------------Contact info---------------
Name            Tel-No          e-Mail
Kamala          077-7123123     kamala@yahoo.com
Kalani          033-4100101     kalani@gmail.com
Saman           011-2123456     saman@cse.mrt.ac.lk
-----------------------------------------
```

<h2>What's on your mind? Put it in the comments!</h2>
<script src="https://utteranc.es/client.js"
        repo="dataideaorg/dataidea-science"
        issue-term="pathname"
        theme="github-light"
        crossorigin="anonymous"
        async>
</script>
