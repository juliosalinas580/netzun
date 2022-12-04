def ejercicio_2(num, lon):
    num_str = str(num)
    num_str_list = list(num_str)
    num_list = []
    for i in num_str_list:
        num_list.append(int(i))

    numro_join = num_list.copy()
    numeros_max = []
    num_len = len(num_str_list)

    for i in range(0, num_len):
        if len(num_list) != 0:
            tmp_max = max(num_list)
            numeros_max.append(tmp_max)
            for i in range(0, num_list.count(tmp_max)):
                num_list.remove(tmp_max)
    i = 1
    k = 0
    while (i <= lon) and (k < len(numeros_max)):
        tmp = numro_join.copy()

        n_count = numro_join.count(numeros_max[k])
        for j in range(0, n_count):
            numro_join.remove(numeros_max[k])
        if numro_join[0] == 0:
            numro_join = tmp.copy()
        k = k + 1
        if n_count > 2:
            i = i + n_count
        else:
            i = i + 1
    lista_str = []
    for i in numro_join:
        lista_str.append(str(i))
    return ''.join(lista_str)


num = int(input('n='))
lon = int(input('k='))
print(ejercicio_2(num, lon))