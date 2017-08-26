def rotate(matrix):
	"""Rotate `matrix` clockwise (in place)."""
	n = len(matrix)
	# for each layer
	for layer in range(n // 2):
		# for each index in layer
		first = layer; last = n - layer - 1
		for index in range(last-first):
			# save the top left entry
			tmp = matrix[first][first+index]
			# bottom_left -> top_left
			matrix[first][first+index] = matrix[last-index][first]
			# bottom_right -> bottom_left
			matrix[last-index][first] = matrix[last][last-index]
			# top_right -> bottom_right
			matrix[last][last-index] = matrix[first+index][last]
			# top_left -> top_right
			matrix[first+index][last] = tmp

# Test on a 3x3 matrix
import numpy as np

matrix = np.random.randint(low=0, high=5, size=(3, 3))
print('Original matrix')
print(matrix)
rotate(matrix)
print('Rotated matrix')
print(matrix)