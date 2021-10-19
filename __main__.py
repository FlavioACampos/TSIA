from rio_tijuana import * # para decidir esto se usaran ifs con los 100 rios
from _functions_ import (fuzzy_matrix_sum,
                         normal_to_fuzzy,
                         fuzzy_row_sum,
                         fuzzy_division,
                         fuzzy_multiplication,
                         fuzzy_to_normal)
# Planes

print("Planes:\n")

print("""Plan 1: Las demandas relacionadas a suministros humanos y animales
deben ser completamente satisfechas en el futuro conforme a las
necesidades actuales. El agua restante debe ser utilizada dando prioridad
a la irrigacion de acuerdo a necesidades futuras. En el caso de un sobrante,
las demandas ecologicas deben ser satisfechas.
""")

print("""Plan 2: La prioridad debe ser puesta en atender las demandas
de suministros humanos y animales, seguido por las necesidades de irrigacion,
todo de acuerdo a necesidades futuras. Una vez mas, en caso de que haya
sobrante de agua, las demandas ecologicas deben ser satisfechas.
""")

print("""Plan 3: Esta alternativa considera cumplir las necesidades de
suministros humanos y animales como la mayor prioridad; primeramente de
acuerdo con las necesidades futuras, luego seguido por las demandas ecologicas.
Solo en caso de un sobrante de agua, las demandas de irrigacion deben cumplirse.
""")

plan_1 = [ # Politico > Social > Economico > Tecnico > Ambiental
    [1/1, 3/1, 2/1, 5/1, 3/1], # A
    [1/3, 1/1, 1/3, 5/1, 2/1], # B
    [1/2, 3/1, 1/1, 4/1, 6/1], # C
    [1/5, 1/5, 1/4, 1/1, 3/1], # D
    [1/3, 1/2, 1/6, 1/3, 1/1]  # E
    ]

plan_2 = [ # Politico > Economico > Social > Ambiental > Tecnico
    [1/1, 2/1, 3/1, 4/1, 5/1], # A
    [1/2, 1/1, 2/1, 3/1, 4/1], # B
    [1/2, 1/2, 1/1, 2/1, 7/1], # C
    [1/4, 1/9, 1/2, 1/1, 3/1], # D
    [1/5, 1/4, 1/3, 1/9, 1/1]  # E
    ]

plan_3 = [ # Politico > Ambiental > Social > Economico > Tecnico
    [1/1, 5/1, 5/1, 3/1, 7/1], # A
    [1/5, 1/1, 1/2, 1/2, 2/1], # B
    [1/2, 2/1, 1/1, 2/1, 5/1], # C
    [1/8, 2/1, 1/2, 1/1, 3/1], # D
    [1/7, 1/2, 1/5, 1/9, 1/1]  # E
    ]

print("Matriz de Saaty para los criterios {}\n".format(crit))
for name, row in zip(crit,criteria):
    print(name,row)

print("\nMatriz difusa de Saaty\n")

fuzzy_matrix = normal_to_fuzzy(criteria)

for row in fuzzy_matrix:
    print(row)

matrix_elements_sum = fuzzy_matrix_sum(fuzzy_matrix)

##print("\nSuma total de la matriz\n")
##print(matrix_elements_sum)

rows = []
for row in fuzzy_matrix:
    row_sum = fuzzy_row_sum(row)
    rows.append(row_sum)
    
##print("\nSuma de cada fila\n")
##for row in rows:
##    print(row)

weights = []
for triangular in rows:
    weight = fuzzy_division(triangular,matrix_elements_sum)
    weights.append(weight)

# Parte importante: Los pesos de cada criterio

print("\nPeso de cada criterio ['w1', 'w2', 'w3', 'w4', 'w5']\n")
i = 0
for weight in weights:
    i += 1
    print("[w{}]".format(i),weight)

print("\nMatrices de Saaty para los subcriterios:")

criterion = [
    subcriteria_A, subcriteria_B, subcriteria_C,
    subcriteria_D, subcriteria_E
    ]

sub_names = [
    sub_a, sub_b, sub_c,
    sub_d, sub_e
    ]

i = 0
j = 0
for subcriteria in criterion:
    print("\nSubcriterios de '{}'\n".format(crit[j]))
    for row in zip(subcriteria):
        print(sub_names[j][i],row)
        i+=1
    i = 0
    j += 1

print("\nMatrices difusas de Saaty para los subcriterios y sus pesos:")

j = 0
subcriteria_weights = []
for subcriteria in criterion:
    fuzzy_subcriteria = normal_to_fuzzy(subcriteria)
    elements_sum = fuzzy_matrix_sum(fuzzy_subcriteria)
    sub_rows = []
    print("\nSubcriterios difusos de '{}'\n".format(crit[j]))
    i = 0
    for row in fuzzy_subcriteria:
        row_sum = fuzzy_row_sum(row)
        sub_rows.append(row_sum)
        print(sub_names[j][i],row)
        i+=1
    k = 0
    print("\nPesos:\n")
    sub_weights = []
    for triangular in sub_rows:
        weight = fuzzy_division(triangular,elements_sum)
        sub_weights.append(weight)
        print("w{}{} =".format(j+1,k+1),weight)
        k+=1
    subcriteria_weights.append(sub_weights)
    j += 1

aggregated_weights = [] # Parte importante
for criteria_weight, subcriteria_list in zip(weights,subcriteria_weights):
    list_of_subcriteria_weights = []
    for subcriteria_weight in subcriteria_list:
        aggregated_weight = fuzzy_multiplication(
            subcriteria_weight,criteria_weight)
        list_of_subcriteria_weights.append(aggregated_weight)
    aggregated_weights.append(list_of_subcriteria_weights)

print("\nMultiplicacion de los vectores de criteria y subcriteria")
print("\n>>> W' = {W'A, W'B, W'C, W'D, W'E}\n")

j = 0
for aggregated_weight in aggregated_weights:
    print("W'{}\n".format(crit[j]))
    for individual_weight in aggregated_weight:
        print(individual_weight)
    j+=1
    print()

plans = [
    plan_1,
    plan_2,
    plan_3
    ]

print("Matrices de Saaty de los planes")

i = 0
j = 0
for plan in plans:
    print("\nPlan {}\n".format(i+1))
    i+=1
    for row in plan:
        print(row)

print("\nMatrices difusas de Saaty para los planes y sus pesos:")

alternative_weights = []
for alternative in plans:
    fuzzy_plan = normal_to_fuzzy(alternative)
    alternative_sum = fuzzy_matrix_sum(fuzzy_plan)
    plan_rows = []
    print("\nMatriz difusa del plan '{}'\n".format(j+1))
    i = 0
    for row in fuzzy_plan:
        row_sum = fuzzy_row_sum(row)
        plan_rows.append(row_sum)
        print("p{}-{}".format(j+1,i+1),row)
        i+=1
    k = 0
    print("\nPesos:\n")
    alt_weights = []
    for triangular in plan_rows:
        weight = fuzzy_division(triangular,alternative_sum)
        alt_weights.append(weight)
        print("w{}{} =".format(j+1,k+1),weight)
        k+=1
    alternative_weights.append(alt_weights)
    j += 1

# Todos los pesos de las alternativas multiplican

# hay que multiplicar los aggregated weights por la matriz difusa de alternativas

total_alternative_weights = [] # Suma de los pesos de las alternativas
for x in alternative_weights:
    sum_z = [0,0,0]
    for z in x:
        # actualizacion de valores triangulares
        sum_z[0] += z[0]
        sum_z[1] += z[1]
        sum_z[2] += z[2]
    #print(sum_z)
    total_alternative_weights.append(sum_z)

##print()
##for x in aggregated_weights:
##    for z in x:
##        print(z)
##    print()

# multiplicacion de las 3 alternativas por los aggregated weights

fuzzy_performance_list = []
for i in range(3):
    plan_x_subcriteria = []
    for x in aggregated_weights:
        for z in x:
            performance = fuzzy_multiplication(
                z, total_alternative_weights[i])
            plan_x_subcriteria.append(performance)
    fuzzy_performance_list.append(plan_x_subcriteria)

print("\nLista de multiplicacion de los pesos por cada una de las [24] subcriterias\n")
for x, z, y in zip(fuzzy_performance_list[0],
                   fuzzy_performance_list[1],
                   fuzzy_performance_list[2]):
    print(x,z,y)

# Pasar los datos difusos a normalizacion
defuzed_performance_list = fuzzy_to_normal(fuzzy_performance_list)
print("\nLista pasada de difuso a normal por metodo Centro de Gravedad")
print("de los pesos de las alternativas.\n")

for internal_list in defuzed_performance_list:
    print(internal_list,'\n')

final_results = []
for defuzed_list in defuzed_performance_list:
    normalized_result = (sum(defuzed_list))/len(defuzed_performance_list[0])
    final_results.append(normalized_result)

i = 1
for result in final_results:
    print("Plan {} = ".format(i),round(result,3))
    i += 1

##total_performance_weights = []
##for x in fuzzy_performance_list:
##    sum_z = [0,0,0]
##    for z in x:
##        # actualizacion de valores triangulares
##        sum_z[0] += z[0]
##        sum_z[1] += z[1]
##        sum_z[2] += z[2]
##    #print(sum_z)
##    total_performance_weights.append(sum_z)
##
##for x in total_performance_weights:
##    print(x)













































