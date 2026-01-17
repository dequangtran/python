import numpy

arr0 = numpy.array(0)
print("Dimention", arr0.ndim, arr0)

arr1 = numpy.array([1, 2, 3, 4, 5])
print("Dimention", arr1.ndim, arr1)

arr2 = numpy.array([[1,2,3], [1, 2, 3], [1, 2, 3]])
print("Dimention", arr2.ndim, arr2)

arr3 = numpy.array([[[1,2, 3], [1,2,3]], [[4,5, 6], [4,5,6]], [[7,8,9], [7,8,9]]])
print("Dimention", arr3.ndim, arr3)

slice0 = arr3[1:3, 1:, 1:3]
print("Slice", slice0)