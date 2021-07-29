# Session 12 Readme file.

### Only the difference in the code from previous week's assignment are shown!

## Changes made to the test file (test_session12.py)
- renamed some of the properties like interior_angle to int_angle etc.

## Link to Colab file

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mmgxa/P3A12/blob/main/session12.ipynb)

## Objective
The objective of this assignment is to implement lazy versions of the Polygon Class and Polygon Sequence Class.

Also, the Polygon Sequence Class must be an iterable - not an iterator (which is implemented via a subclass). Hence, our Polygon Sequence must not have the `__next__` method.



## Modifications Made from Last Week

Last week we already turned the Polygon Sequence into an iterable

### Polygon Class

The properties were turned from a non-lazy to lazy version.

**Non-lazy version:**

```python
@property
def interior_angle(self):
	return (self._n - 2) * 180 / self._n
```

**Lazy version:**   
(note the line `self.int_angle_i = None` in the `__init__` function)
```python
@property
def int_angle(self) -> float:
	if self.int_angle_i is not None:
		return self.int_angle_i
	else:
		self.int_angle_i = (self.n_edge - 2)*(180/self.n_edge)
		return self.int_angle_i
```


### Polygon Sequence Class

Inside the iterator of the sequence iterator, we have the `__next__` method. This is a lazy method.

```python
def __next__(self):
	if self.i > self.max_edges:
		raise StopIteration
	else:
		pol = Polygon(self.i, self.common_circumradius)
		self.i += 1
		return pol
```

That is, the polygons are created 'on-the-fly'.