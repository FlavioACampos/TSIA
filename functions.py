# Programador:  Flavio Campos
# Descripcion:  Proyecto TSIA / Funciones
# Fecha:        2018-05-31
# Modificacion: 2021-10-18 / Se realiza limpieza de codigo (previa a refactoring)

def fuzzy_matrix_sum(fuzzy_matrix):
	"""Funcion sumatoria de valores de una matriz difusa.

	:fuzzy_matrix: matriz cuyas filas son valores difusos ([n, n, n])
	:return: regresa la suma de todos los valores difusos de la matriz
	"""
	tri_sum = [0, 0, 0]
	for fuzzy_row in fuzzy_matrix:
		for fuzzy_val in fuzzy_row:
			tri_sum[0] += fuzzy_val[0]
			tri_sum[1] += fuzzy_val[1]
			tri_sum[2] += fuzzy_val[2]
	return tri_sum

def fuzzy_row_sum(fuzzy_row):
	"""Funcion sumatoria de valores de una fila de matriz difusa.

	:fuzzy_row: fila con valores difusos [[n, n, n], ... [n, n, n]]
	:return: regresa la suma de todos los valores difusos de la fila
	"""
	tri_sum = [0, 0, 0]
	for fuzzy_val in fuzzy_row:
		tri_sum[0] += fuzzy_val[0]
		tri_sum[1] += fuzzy_val[1]
		tri_sum[2] += fuzzy_val[2]
	return tri_sum

def fuzzy_division(fuzzy_val_1, fuzzy_val_2):
	"""Funcion que divide dos numeros difusos.
	
	:fuzzy_val_1: valor difuso triangular (dividendo)
	:fuzzy_val_2: valor difuso triangular (divisor)
	:return: regresa el resultado de la operacion (valor difuso)
	"""
	fuzzy_val_2 = list(reversed(fuzzy_val_2))
	result = [val_1 / val_2 for val_1, val_2 in zip(fuzzy_val_1, fuzzy_val_2)] # weight
	return result

def fuzzy_multiplication(fuzzy_val_1, fuzzy_val_2):
	"""Funcion que multiplica dos numeros difusos.
	
	:fuzzy_val_1: valor difuso triangular
	:fuzzy_val_2: valor difuso triangular
	:return: regresa el resultado de la operacion (valor difuso)
	"""
	result = [val_1 * val_2 for val_1, val_2 in zip(fuzzy_val_1, fuzzy_val_2)] # aggregated_weight_value
	return result

def normal_to_fuzzy(matrix):
	"""Funcion que convierte una matriz de saaty de normal a difusa

	La conversion de los valores se realiza conforme a la Tabla 1 del doc
	
	:matrix: matriz original de saaty
	:return: matriz de saaty en su version difusa
	"""
	delta = 2 # distancia difusa (puede ser entre 0.5 y 2 para valores impares)
	fuzzy_matrix = []
	for row in matrix:
		new_row = []
		for val in row:
			if val == 1:
				new_element = [val, val, val+2]
			elif val in [3, 5, 7]:
				new_element = [val-2, val, val+2]
			elif val in [2, 4, 6, 8]:
				new_element = [val-1, val, val+1]
			elif val == 9:
				new_element = [val-2, val, val]
			elif val == 1/2:
				new_element = [1/3, 1/2, 1/1]
			elif val == 1/3:
				new_element = [1/5, 1/3, 1/1]
			elif val == 1/4:
				new_element = [1/5, 1/4, 1/3]
			elif val == 1/5:
				new_element = [1/7, 1/5, 1/3]
			elif val == 1/6:
				new_element = [1/7, 1/6, 1/5]
			elif val == 1/7:
				new_element = [1/9, 1/7, 1/5]
			elif val == 1/8:
				new_element = [1/9, 1/8, 1/7]
			elif val == 1/9:
				new_element = [1/9, 1/9, 1/7]
			new_row.append(new_element)
		fuzzy_matrix.append(new_row)
	return fuzzy_matrix

def fuzzy_to_normal(fuzzy_matrix):
	"""Funcion que convierte una matriz difusa de saaty a normal

	La conversion de los valores se realiza por el metodo de centro de gravedad
	
	:matrix: matriz difusa de saaty
	:return: matriz de saaty en su version normal
	"""
	normal_matrix = []
	for fuzzy_list in fuzzy_matrix: # tiene 3 listas por ser 3 alternativas
		new_list = []
		for triangular in fuzzy_list:
			# Metodo de centro de gravedad
			new_element = ((triangular[2] - triangular[0] + triangular[1] - triangular[0]) / 3 + triangular[0])
			new_list.append(new_element)
		normal_matrix.append(new_list)
	return normal_matrix
