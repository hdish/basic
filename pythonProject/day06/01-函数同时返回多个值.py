
def calculate(a,b):
    sum = a + b
    sub = a - b
    mul = a * b
    div = a // b
    # return sum,sub,mul,div      # 同时返回多个值，默认用  元组 封装
    return [sum,sub,mul,div]        # 当然也可以手动把多个值封装成 列表或者集合，然后返回

if __name__ == '__main__':
    result = calculate(10,20)
    print(result)
    print(type(result))
