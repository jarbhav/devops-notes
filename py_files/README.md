# What are Pools

Pools are ideal for applications where you want to protect your number of workers. Imagine you run a function in an API that creates 5 workers to handle the provided data. What if your API suddenly receives 500 requests in a single second? Creating 2.500 workers that all perform heavy tasks may kill your computer.

Pools prevent your computer from being killed like that by limiting the number of workers that can be created. In the API example, you might want to create a pool with a maximum of 50 workers. What happens when 500 requests come in? Only 50 workers get created. Remember that each request takes 5 workers? This means that only the first 10 requests get handled. Once a worker is done and returns to the pool it can be sent out again.

In summary: pools make sure that no more than a certain number of workers are active at any given time.

[Documentation](https://docs.python.org/3/library/concurrent.futures.html)

>***Threading is more suitable for IO-type tasks*** (waiting concurrently) while ***processes are best suited for CPU-heavy tasks*** (using more CPU’s)

# Packages
A package is a collection of various modules with a path attribute.

# Python Modules
Python modules serve as an organizational unit of Python code. They are a bunch of related code grouped together.

You can have functions, classes or variables inside a Python module.

# Python Libraries
A Python library is a collection of modules and packages.

> The `heavy_function` folder is a `package` which contains two modules `cpu_heavy` and `io_heavy`, they have functions. The package also contains `__init__.py` which is responsible for importing the two modules. The files starting with 0 are using these modules.

# Python Data Structures

Apart from builtin data structures like list, tuple, dictionary and set, in the collections module we have other data structures like:

## [namedtuple()](https://docs.python.org/3/library/collections.html#collections.namedtuple)
Named tuples assign meaning to each position in a tuple and allow for more readable, self-documenting code. They can be used wherever regular tuples are used, and they add the ability to access fields by name instead of position index.
```python
>>> Book = namedtuple('Book', ['id', 'title', 'authors'])
>>> b1 = Book('11', 'AB', 'XY')
>>> b1.id
'11'
>>> b1.title
'AB'
>>> b1.authors
'XY'
```

## [deque](https://docs.python.org/3/library/collections.html#collections.deque)
Doubly ended queue
```
>>> dq = deque('AaBbCc')
>>> dq
deque(['A', 'a', 'B', 'b', 'C', 'c'])
>>> dq.pop()
'c'
>>> dq.popleft()
'A'
>>> dq
deque(['a', 'B', 'b', 'C'])
>>> dq.append('D')
>>> dq.appendleft('A')
>>> dq
deque(['A', 'a', 'B', 'b', 'C', 'D'])
>>> 

```
## [ChainMap](https://docs.python.org/3/library/collections.html#collections.ChainMap)
```python
baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
list(ChainMap(adjustments, baseline))
['music', 'art', 'opera']

```
## [Counter](https://docs.python.org/3/library/collections.html#collections.Counter)
```python
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
cnt
Counter({'blue': 3, 'red': 2, 'green': 1})

```
## [OrderedDict](https://docs.python.org/3/library/collections.html#collections.OrderedDict)
Python OrderedDict is a dict subclass that maintains the items insertion order. When we iterate over an OrderedDict, items are returned in the order they were inserted. A regular dictionary doesn’t track the insertion order.

[Other major differences](https://docs.python.org/3/library/collections.html#ordereddict-objects:~:text=Some%20differences%20from%20dict%20still%20remain)

## [defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)
```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)

sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

```python
s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = defaultdict(set)
for k, v in s:
    d[k].add(v)

sorted(d.items())
[('blue', {2, 4}), ('red', {1, 3})]
```