import requests

link = 'https://icanhazip.com'
responce = requests.get(link)
print(responce.status_code)
print(responce.text)


import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
print(arr + 5)
print(arr ** 2)
print(numpy.sum(arr))

matrix = numpy.array([[1, 2, 3], [4, 5, 6]])
print(matrix)

