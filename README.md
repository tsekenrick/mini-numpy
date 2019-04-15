## Mini numpy
This library was written to emulate some of the functionality of numpy. It is then used to perform analysis on data about favored halloween candies, and is intended as a study on effective use of list comprehensions and lambda functions.

* List Comprehensions
	1. [Generate list with the indices that have a match between the LabelledList's labels and the list passed in as an argument](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/tabletools.py#L91)
	2. [Generate list of booleans, comparing elements at each index of scalar and self.values, returning true if they are the same](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/tabletools.py#L125)
	3. [Generate list of return values of a function being that is called with the args being the elements of self.values](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/tabletools.py#L141)
	4. [Select elements at specific indices of self.values(i) based on values from matches](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/tabletools.py#L209)
* Lambdas
	1. [In line 175: Used to return True if first 5 char of x is 'Reese'](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/candy.ipynb#L175)
	2. [In line 228: Used to return True if x has length less than 10](https://github.com/tsekenrick/mini-numpy/blob/b4d2d67c7876a4f92741880a9cee44beb4a6afec/candy.ipynb#L228)
    * Note that line numbers indicated are when viewing in source blob mode.
