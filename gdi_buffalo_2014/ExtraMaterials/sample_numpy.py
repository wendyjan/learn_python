"""
Filename: sample_numpy.py

Author: Wendy Jansson



This file shows a sample of numpy.

numpy is a Python library that is excellent for working with arrays and matrices.

numpy works much faster than Python lists for matrix operations.

Learn more at http://www.numpy.org/

And check out all the great examples at http://wiki.scipy.org/Numpy_Example_List

See how numpy is nicer than just Python by reading
http://stackoverflow.com/questions/21539950/python-multiply-list-of-lists-element-wise


***NOTE you must have a library called "numpy" installed for this to work!***

If you don't have numpy, Python will raise an ImportError.

Download and install the Anaconda distribution of Python to get numpy easily,
along with a lot of other great libraries.

"""
import numpy

if __name__ == "__main__":

    # Python list from 2 to 10 in increments of 1
    mySlowPythonList = range(2, 11, 1)
    print ("Here is my slow Python list: ")
    print (mySlowPythonList)
    
    # numpy array from 2 to 11 in increments of 1
    myFastNumpyArray = numpy.arange(2, 11, 1)
    print ("Here is the faster array I made using numpy.arange(start, stop, increment): ")
    print (myFastNumpyArray)

    # numpy array from 2 to 11 with 9 evenly-spaced samples
    anotherFastNumpyArray = numpy.linspace(2, 11, 9)
    print ("Here is another fast array I made using numpy.linspace(start, stop, numberOfSamples): ")
    print (anotherFastNumpyArray)

    # Let's see some matrix operations.
    a = numpy.array([[1,2,3],[2,3,4],[3,4,5]])
    numpy.prod(a,axis=1)
    print("Fast matrix operation!!")
    print(a)
