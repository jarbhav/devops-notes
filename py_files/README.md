# What are Pools

Pools are ideal for applications where you want to protect your number of workers. Imagine you run a function in an API that creates 5 workers to handle the provided data. What if your API suddenly receives 500 requests in a single second? Creating 2.500 workers that all perform heavy tasks may kill your computer.

Pools prevent your computer from being killed like that by limiting the number of workers that can be created. In the API example, you might want to create a pool with a maximum of 50 workers. What happens when 500 requests come in? Only 50 workers get created. Remember that each request takes 5 workers? This means that only the first 10 requests get handled. Once a worker is done and returns to the pool it can be sent out again.

In summary: pools make sure that no more than a certain number of workers are active at any given time.

>***Threading is more suitable for IO-type tasks*** (waiting concurrently) while ***processes are best suited for CPU-heavy tasks*** (using more CPU’s)

# Packages
A package is a collection of various modules with a path attribute.

# Python Modules
Python modules serve as an organizational unit of Python code. They are a bunch of related code grouped together.

You can have functions, classes or variables inside a Python module.

# Python Libraries
A Python library is a collection of modules and packages.