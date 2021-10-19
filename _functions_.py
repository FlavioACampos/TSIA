# Funciones

# Suma todos los elementos dentro de la matriz difusa
def fuzzy_matrix_sum(matrix):
    tri_sum = [0,0,0]
    for row in matrix:
        for triangular in row:
            tri_sum[0] += triangular[0]
            tri_sum[1] += triangular[1]
            tri_sum[2] += triangular[2]
    return tri_sum

def fuzzy_row_sum(row):
    tri_sum = [0,0,0]
    for element in row:
        tri_sum[0] += element[0]
        tri_sum[1] += element[1]
        tri_sum[2] += element[2]
    return tri_sum

def fuzzy_division(triangular_1, triangular_2):
    tri_2 = list(reversed(triangular_2))
    weight = [x/y for x, y in zip(triangular_1,tri_2)]
    return weight

def fuzzy_multiplication(triangular_1, triangular_2):
    aggregated_weight_value = [
        x*y for x, y in zip(triangular_1,triangular_2)]
    return aggregated_weight_value
            
# Convierte una matriz normal de saaty a una difusa
def normal_to_fuzzy(matrix):
    fuzzy_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            if element == 1:
                new_element = [element,
                               element,
                               element+2]
            elif (element == 3 or
                  element == 5 or
                  element == 7):
                new_element = [element-2,
                               element,
                               element+2]
            elif (element == 2 or
                  element == 4 or
                  element == 6 or
                  element == 8):
                new_element = [element-1,
                               element,
                               element+1]
            elif element == 9:
                new_element = [element-2,
                               element,
                               element]
            elif element == 1/2:
                new_element = [1/3,
                               1/2,
                               1/1]
            elif element == 1/3:
                new_element = [1/5,
                               1/3,
                               1/1]
            elif element == 1/4:
                new_element = [1/5,
                               1/4,
                               1/3]
            elif element == 1/5:
                new_element = [1/7,
                               1/5,
                               1/3]
            elif element == 1/6:
                new_element = [1/7,
                               1/6,
                               1/5]
            elif element == 1/7:
                new_element = [1/9,
                               1/7,
                               1/5]
            elif element == 1/8:
                new_element = [1/9,
                               1/8,
                               1/7]
            elif element == 1/9:
                new_element = [1/9,
                               1/9,
                               1/7]
            new_row.append(new_element)
        fuzzy_matrix.append(new_row)
    return fuzzy_matrix

def fuzzy_to_normal(matrix):
    new_matrix = []
    for fuzzy_list in matrix: # tiene 3 listas por ser 3 alternativas
        new_list = []
        for element in fuzzy_list:
            # Metodo de centro de gravedad
            new_element = ((element[2] - element[0] +
                            element[1] - element[0])/
                           3 + element[0])
            new_list.append(new_element)
        new_matrix.append(new_list)
    return new_matrix
            
        

            
                
