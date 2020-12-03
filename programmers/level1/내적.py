def solution(a, b):
    inner_product = []
    for idx in range(len(a)):
        inner_product.append(a[idx] * b[idx])
    
    return sum(inner_product)
