# Lab: timeit (Part 2)

In this lab you will measure the runtime of the sequential and binary search algorithms in the `notes.py` file.
The main takeaway from this assignment is that:
binary search has a runtime of $O(\log n)$, which is *very* fast.
It scales to internet-sized datasets.

<img src=img/logn.png width=200px />

You will also practice a bit more git and learn how to plot and view graphs on the lambda server.
The assignment will have you editing this repo at various points.
Fork this repo, and make all changes in your own forked repo.

You are not required to work with a partner on this lab,
but you are encouraged to do so.

## Part 1: Runtime vs N

Recall that sequential search has a worst case runtime of $\Theta(n)$ and binary search has a worst case runtime of $\Theta(\log n)$.
We will prove these facts in class next week.
In this assignment we will see just how much better the logarithmic runtime is than the linear runtime as $n$ grows large.

The following terminal command measures the runtime of the `binary_search_itr` function from the `notes.py` file on a list of length `n=65536`:
```
$ python3 -m timeit \
    -s 'import notes; n = 65536; xs = list(range(-n,n))' \
    'notes.binary_search_itr(xs,5)'
```

> **NOTE:**
> The backslash `\` in the command above signifies that the command continues onto the next line.
> Recall that the `\` is used to "escape" characters to change their meaning.
> In this case, the character that follows the `\` is a newline character (rendered as `\n` in python),
> and the `\` above signifies that the newline character should be interpreted as ordinary whitespace and not the end of a command.
> Therefore, the command above is functionally equivalent to
> ```
> $ python3 -m timeit -s 'import notes; n = 65536; xs = list(range(-n,n))' 'notes.binary_search_itr(xs,5)'
> ```
> But the first command is easier to read.

For each cell in the table below:
Modify the command above for the corresponding search function and value of `n`;
measure the runtime and enter it into the table.
(See the hint below the table before doing it all manually.)

|                | `sequential_search_itr`   | `binary_search_rec`   |
| -------------- | ------------------------- | --------------------- | 
| `n=2**0`       |                           |                       |
| `n=2**1`       |                           |                       |
| `n=2**2`       |                           |                       |
| `n=2**3`       |                           |                       |
| `n=2**4`       |                           |                       |
| `n=2**5`       |                           |                       |
| `n=2**6`       |                           |                       |
| `n=2**7`       |                           |                       |
| `n=2**8`       |                           |                       |
| `n=2**9`       |                           |                       |
| `n=2**10`      |                           |                       |
| `n=2**11`      |                           |                       |
| `n=2**12`      |                           |                       |
| `n=2**13`      |                           |                       |
| `n=2**14`      |                           |                       |
| `n=2**15`      |                           |                       |
| `n=2**16`      |                           |                       |
| `n=2**17`      |                           |                       |
| `n=2**18`      |                           |                       |
| `n=2**19`      |                           |                       |
| `n=2**20`      |                           |                       |
| `n=2**21`      |                           |                       |
| `n=2**22`      |                           |                       |

> **HINT:**
> You don't have to run all of these tests manually.
> The bash shell has a built-in for loop feature that you can use.
> To see how this feature works, run the command
> ```
> $ for i in 1 2 3 4 5; do
>     echo "i=$i"
> done
> ```
> Notice:
> 1. When you enter a multiline command in bash, your prompt will probably change to `>`.
>       It is traditional not to display this "multiline prompt" when writing commands.
> 1. The `$i` gets substituted with each value 1 2 3 4 5.
>
> Obviously, typing out all the numbers from 0 to 22 is a pain and not something us error-prone humans should be doing.
> Fortunately, the shell has a command `seq` that works like python's `range`.
> Try running
> ```
> $ seq 0 22
> ```
> and observe that this prints all the numbers from 0 to 22 inclusive.
> (`seq` behaves differently than python's `range` this way.)
>
> We loop over the results of `seq` using the *command substitution* syntax `$( ... )`.
> This syntax takes the output of whatever command is within the parenthesis and "pastes" it wherever the parentheses are.
> So if we modify the for loop to
> ```
> $ for i in $(seq 0 22); do
>     echo "i=$i"
> done
> ```
> we will loop over all the numbers we need for the table.
>
> Finally, you can automate your table generation procedure by putting the python time it command within the loop.
> We can put the timeit command inside of this for loop as well to run all of the appropriate timeit calls.
>
> **Exercise:**
> Combine the for loop and timeit commands into a single command.
> You will still want to echo the value of `$i`,
> just add the timeit command below the echo.
> You should modify the `python3 -m timeit ...` code above so that the section `n = 65536` is replaced by `n = 2**$i`.

<!--
Solution:
```
$ for i in $(seq 0 22); do
    echo "i=$i"
    python3 -m timeit \
        -s "import notes; n = 2**$i; xs = list(range(-n,n))" \
        "notes.binary_search_rec(xs,5)"
done
```
-->

You should observe that:
1. Binary search is much faster for large $n$, but for small $n$ sequential search may be faster.
1. Multiplying `n` times 2 gives a *multiplicative* slowdown for sequential search (by a factor of 2),
  but an additive slowdown for binary search.

  You should ensure that this multiplicative vs additive slowdown makes sense to you based on the properties of logarithms.

At [FAANG](https://en.wikipedia.org/wiki/Big_Tech#FAANG)-type companies,
they are searching through datasets of size `n>1000000000000000` (15+ zeros).
It should hopefully be clear from these examples that the logarithmic runtime is absolutely essential for any realtime queries of datasets of this size.

## Part 2: Plotting the results

It is hard to visualize raw table outputs like you have above.
So in this section we will plot them visually.
We'll start with some example data just to practice the mechanics,
then you'll plot the real data by yourself.

### Part 2a: example data

First, we will practice generating plots and viewing them on a remote server.
The file `example.csv` contains some example data that we will plot, and `plot.py` contains code for plotting it.
Quickly skim these files:
```
$ cat example.csv
$ cat plot.py
```

Observe that there are no png files in your folder:
```
$ ls
```
Then run the plot command and observe that it creates a png file:
```
$ python3 plot.py example.csv
$ ls
```

Now the question is, how do you view the file?
The terminal only supports text, and so there is no direct way to do it in the terminal.
There are many workarounds to this problem that people have developed,
but the simplest for our purposes is to just upload to github.

Observe that the image below has a broken link:

<img src=first_example.png width=400px>

Also observe that it is looking for a file named `first_example.png`
(you'll have to look at the markdown source, find the `img` html tag and the `src` attribute).
This file does not exist, and that's why github renders it as a broken image.

We will use the `img` tag above to view our `example.csv` data.
First rename the png file that `plot.py` created to `first_example.png` using the `mv` command.
Then add/commit/push the changes to github.
You should be able to refresh this page and see the image displayed above.

### Part 2b: real data

Now that you know how to create and view plots,
you are ready to visualize your own runtimes.
The runtimes will display in the image below once you complete the necessary steps:

<img src=runtimes.png width=400px>

The steps are:

1. Create a file `myruntimes.csv` that contains the contents of your markdown table from Part 1.

2. Call `plot.py` on this new data.

3. `mv` the created png to the right location, and add/commit/push to github.

The plot above is a log-log plot, so interpreting it requires some practice.
But the plot should make it obvious that `binary_search_rec` is much faster than 
`sequential_search_itr` as $n$ gets large.

## Part 3: Measuring combinations of data structure / implementation

We will now compare the runtime of binary search on four of python's container types: list, deque, tuple, and array.

We've already covered the list/deque types in class.
The tuple type is one that you've probably also seen.
In python,
it's denoted using parentheses instead of square brackets.
```
>>> xs = (1, 2, 3, 4, 5)
```
Tuples can also be created by omitting the parenthesis entirely or using the `tuple` function like so:
```
>>> xs = 1, 2, 3, 4, 5
>>> xs = tuple(range(1,6))
```
Tuples can be indexed and sliced just like lists in python, but they are immutable.
This means that they cannot be updated (for example with the `append` method),
and are therefore slightly more efficient.

The array type is likely one that you haven't seen before,
since it is not usually introduced in intro programming courses.
The array type is included in the numpy library for scientific computing.
You create an array by first importing the library,
and then calling the `array` constructor on an iterable (i.e. list-like container):
```
>>> import numpy
>>> numpy.array([1, 2, 3, 4, 5])
array([1, 2, 3, 4, 5])
>>> numpy.array(range(1,6))
array([1, 2, 3, 4, 5])
```

> **NOTE:**
> numpy is not built-in to python and needs to be pip installed.
> But it is also a large package that takes up >100mb.
> So on the lambda server, if you try to install it, you will get an error about running out of disk space because your accounts only have 100mb allocated to them.
> Fortunately, it is pre-installed on the lambda server global environment.
> Therefore, you must not have an active venv for numpy to work.
> If you currently are inside a venv, you can run `deactivate` to leave.

The array supports a very similar interface as a list.
For example, you can index and slice just like in a list:
```
>>> xs = numpy.array(range(1,6))
>>> xs[3]
4
>>> xs[3:]
array([4, 5])
```
The purpose of the array is to support numerical computations from linear algebra,
and it behaves differently than lists with respect to the `+` and `*` operators.
Lists use "container algebra" operations:
```
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
>>> [1, 2]*2
[1, 2, 1, 2]
```
and arrays use "vector algebra" operations:
```
>>> numpy.array([1, 2]) + numpy.array([3, 4])
array([4, 6])
>>> numpy.array([1, 2]) * 2
array([2, 4])
```
In this problem, the important difference will be that:
1. list slices make a copy and take time O(k), where k is the size of the slice;
1. array slices do not make a copy and take time O(1).
To see that array slices do not make a copy,
run the following sequence of commands:
```
>>> xs = numpy.array([1, 2, 3, 4, 5])
>>> xs
array([1, 2, 3, 4, 5])
>>> ys = xs[3:]
>>> ys
array([4, 5])
>>> ys[0] = -1
>>> ys[1] = -2
>>> xs
array([ 1,  2,  3, -1, -2])
```

> **NOTE:**
> If it's not obvious to you how the commands above would generate different output if `xs` were a list,
> then you should also run them for `xs = [1, 2, 3, 4, 5]` before continuing.

The following terminal command measures the runtime of the `binary_search_itr` command from the `notes.py` file on an array of length `n=65536`:
```
$ python3 -m timeit \
    -s 'import notes; import numpy; n = 65536; xs = numpy.array(range(-n,n))' \
    'notes.binary_search_itr(xs,5)'
```

For each cell in the table below:
Modify the command above for the corresponding search function and container type;
measure the runtime and enter it into the table.
If you get a stack overflow, then put `---` in the table.

|                            | `array`  | `list`  | `tuple`     | `deque`       |
| -------------------------- | ---------| --------|------------ | ------------- |
| `sequential_search_itr`    |          |         |             |               |
| `sequential_search_itr2`   |          |         |             |               |
| `sequential_search_rec`    |          |         |             |               |
| `binary_search_itr`        |          |         |             |               |
| `binary_search_rec`        |          |         |             |               |
| `binary_search_rec2`       |          |         |             |               |

You should notice that:
1. for the `array` container, all implementations of binary search work well
1. for the `list` container, the binary search that relies on slicing is slow
1. the `tuple` container behaves just like the list container
1. binary search provides no speed up for the `deque` container;
  the `deque` container also does not support slicing, and so the `binary_search_rec2` function will have a type error
1. the `sequential_search_rec` gets a `RecursionError` for large `n` values;
  this is one of the reasons we tend to prefer for loops over recursion when possible

We will prove all of these statements formally next week in class by showing that the runtimes are:

|                            | `array`  | `list`  | `tuple`     | `deque`       |
| -------------------------- | ---------| --------|------------ | ------------- |
| `sequential_search_itr`    | O(n)     | O(n)    | O(n)        | O(n)          |
| `sequential_search_itr2`   | O(n)     | O(n)    | O(n)        | O(n^2)        |
| `sequential_search_rec`    | ---      | ---     | ---         | ---           |
| `binary_search_itr`        | O(log n) | O(log n)| O(log n)    | O(n)          |
| `binary_search_rec`        | O(log n) | O(log n)| O(log n)    | O(n)          |
| `binary_search_rec2`       | O(log n) | O(n)    | O(n)        | ---           |

## Submission

Submit the url to your repo to canvas.
