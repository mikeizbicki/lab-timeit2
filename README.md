# Lab: timeit (Part 2)

## Part I - Completing last week's lab

<!--
For the first part of this lab, you will work with a partner.
You will modify last week's lab repo to include the big-O notation table that was commented out.
Each person will modify their partner's repo and submit the changes as a pull request.
-->

1. Find a partner.

1. Try to fork your partner's repo from last week.
    (Recall that this repo was forked from my upstream repo <https://github.com/mikeizbicki/lab-timeit>,
    and so the url will look the same just with their username.)

    You'll notice that GitHub doesn't let you fork this repo:
    you've already forked my repo, and GitHub doesn't let you have multiple forks of the same repo.
    To work around this problem, you will have to:

    1. Create a duplicate copy of your own lab-timeit repo that is not a fork of my repo.
        Follow the instructions at <https://docs.github.com/en/repositories/creating-and-managing-repositories/duplicating-a-repository>.
        It does not matter what you name your duplicate repo.

    1. Once your partner has their duplicate repo created, fork it.

1. Clone the newly created fork onto the lambda server.

1. Edit the `README.md` file to:
    
    1. Remove the comments around the big-O notation table.
    1. Fill in the correct runtimes in each box of the table using big-O notation.

1. Submit a pull request to your partner's repo,
   and accept the pull request that your partner submits to your repo.

## Part II

(You no longer need a partner, but you're encouraged to keep working together.)

For the second part of this lab, you will measure the runtime performance of the sequential and binary search algorithms in the `notes.py` file.
There will be two tables to complete.
Fork this repo, and make all changes in your own forked repo.
When done, ensure that you push the changes back onto github.

### Runtime vs N

Recall that sequential search has a worst case runtime of $\Theta(n)$ and binary search has a worst case runtime of $\Theta(\log n)$.
We will prove these facts in class next week.
In this assignment we will see just how much better the logarithmic runtime is than the linear runtime as $n$ grows large.

The following terminal command measures the runtime of the `binary_search_itr` function from the `notes.py` file on a list of length `n=65536`:
```
$ python3 -m timeit \
    'import notes; n = 65536; xs = list(range(-n,n))' \
    'notes.binary_search_itr(xs,5)'
```

> **NOTE:**
> The backslash `\` in the command above signifies that the command continues onto the next line.
> Recall that the `\` is used to "escape" characters to change their meaning.
> In this case, the character that follows the `\` is a newline character (rendered as `\n` in python),
> and the `\` above signifies that the newline character should be interpreted as ordinary whitespace and not the end of a command.
> Therefore, the command above is functionally equivalent to
> ```
> $ python3 -m timeit -s 'import notes; n = 65536; xs = list(range(-n,n))' 'notes.binary_search_rec(xs,5)'
> ```
> But the first command is easier to read.

For each cell in the table below:
Modify the command above for the corresponding search function and value of `n`;
measure the runtime and enter it into the table.

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
> $ for i in $(seq 0 22); do
>     echo "i=$i"
> done
> ```
> Notice:
> 1. When you enter a multiline command in bash, your prompt will probably change to `>`.
>       It is traditional not to display this "multiline prompt" when writing commands.
> 1. The `$i` gets substituted with each value between 0 and 22.
>       This is different than python, where the last value in the range is included).
> 
> We can put the timeit command inside of this for loop as well to run all of the appropriate timeit calls.
> The final command will look something like:
> ```
> $ for i in $(seq 0 22); do
>     echo "i=$i"
>     python3 -m timeit \
>         -s "import notes; n = 2**$i; xs = list(range(-n,n))" \
>         "notes.binary_search_rec(xs,5)"
> done
> ```
> But you'll have to modify it for the other table column.

You should observe that:
1. Binary search is much faster for large $n$, but for small $n$ sequential search may be faster.
1. Multiplying `n` times 2 gives a *multiplicative* slowdown for sequential search (by a factor of 2),
  but an additive slowdown for binary search.

  You should ensure that this multiplicative vs additive slowdown makes sense to you based on the properties of logarithms.

At [FAANG](https://en.wikipedia.org/wiki/Big_Tech#FAANG)-type companies,
they are searching through datasets of size `n>1000000000000000` (15+ zeros).
It should hopefully be clear from these examples that the logarithmic runtime is absolutely essential for any realtime queries of datasets of this size.

### Measuring combinations of data structure / implementation

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
The array type is included in the numpy library.
You create an array by first importing the library,
and then calling the `array` constructor on an iterable (i.e. list-like container):
```
>>> import numpy
>>> numpy.array([1, 2, 3, 4, 5])
array([1, 2, 3, 4, 5])
>>> numpy.array(range(1,6))
array([1, 2, 3, 4, 5])
```
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
>>> [1, 2] + [3, 4]
[4, 6]
>>> [1, 2]*2
[2, 4]
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

The following terminal command measures the runtime of the `binary_search_itr` command from the `notes.py` file on an array of length `n=100000`:
```
$ python3 -m timeit \
    -s 'import notes; import numpy; n = 65536; xs = numpy.array(range(-n,n))' \
    'notes.binary_search_itr(xs,5)'
```

For each cell in the table below:
Modify the command above for the corresponding search function and container type;
measure the runtime and enter it into the table.

|                            | `array`  | `list`  | `tuple`     | `deque`       |
| -------------------------- | ---------| --------|------------ | ------------- |
| `sequential_search_itr`    |          |         |             |               |
| `sequential_search_itr2`   |          |         |             |               |
| `sequential_search_rec`    |  ---     | ---     |  ---        |  ---          |
| `binary_search_itr`        |          |         |             |               |
| `binary_search_rec`        |          |         |             |               |
| `binary_search_rec2`       |          |         |             |  ---          |

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

Submit the url to your new lab-timeit repo and your forked version of this repo to sakai.
