import numpy as np

## Creating a rank 1 Array
arrR1 = np.array([1, 2, 3])
print("Array with Rank 1: \n",arrR1)

## Creating a rank 2 Array
arrR2 = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with Rank 2: \n", arrR2)

## Creating an array from tuple
arrT = np.array((1, 3, 2))
print("\nArray created from a passed tuple:\n", arrT) 

## Printing a range of Array with the use of slicing method
sliced_arr = arr[:2, ::2]
print ("Array with first 2 rows and alternate columns(0 and 2):\n", sliced_arr)

## Printing elements at specific Indices
Index_arr = arr[[1, 1, 0, 3], 
                [3, 2, 1, 0]]
print ("\nElements at indices (1, 3), (1, 2), (0, 1), (3, 0):\n", Index_arr)

## Defining Array 1
a = np.array([[1, 2],
              [3, 4]])

## Defining Array 2
b = np.array([[4, 3],
              [2, 1]])
               
## Adding 1 to every element
print ("Adding 1 to every element:", a + 1)

## Subtracting 2 from each element
print ("\nSubtracting 2 from each element:", b - 2)

## sum of array elements
## Performing Unary operations
print ("\nSum of all array elements: ", a.sum())
 
## Adding two arrays
print ("\nArray sum:\n", a + b)

## First Array
arr1 = np.array([[4, 7], [2, 6]],dtype = np.float64)

## Second Array
arr2 = np.array([[3, 6], [2, 8]],dtype = np.float64) 
 
## Addition of two Arrays
Sum = np.add(arr1, arr2)
print("Addition of Two Arrays: ")
print(Sum)

## Addition of all Array elements using predefined sum method
Sum1 = np.sum(arr1)
print("\nAddition of Array elements: ")
print(Sum1)

## Square root of Array
Sqrt = np.sqrt(arr1)
print("\nSquare root of Array1 elements: ")
print(Sqrt)

## Transpose of Array using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)

## Converts array of binaries (0s and 1s) to an array of booleans (True and False)
matriz_binarios = np.array([[0, 1, 1],
                            [1, 0, 0],
                            [1, 0, 1]])

print(matriz_binarios.astype(bool))