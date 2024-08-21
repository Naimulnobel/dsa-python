def sum_product(input_tuple):
    sum = 0
    product = 1
    for i in range(0, len(input_tuple)):
        sum += input_tuple[i]
        product *= input_tuple[i]

    return  sum, product

print(sum_product((1, 2, 3, 4)
))