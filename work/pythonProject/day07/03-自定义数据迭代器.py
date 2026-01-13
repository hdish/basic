
import math

# 读取qinhuaci.txt文件中的数据，按照n/批次，生成生成器
def dataset_loader(batch_size):
    """
    :param batch_size: 每批次的数据条数
    :return:
    """
    # 1.1读取文件，获取到所有数据，即：readlines() 一次性读取所有行到列表中
    with open('./data/qinhuaci.txt','r',encoding='utf-8') as src_f:
        data_lines = src_f.readlines()  # 一次性读取所有行到列表中

        # 1.2计算数据的总条数
        line_count = len(data_lines)

        # 1.3计算数据的总批次  即，总批次 = 数据总条数/每批次的数据条数  细节：记得向上取整
        batch_count = math.ceil(line_count / batch_size)

        # 1.4遍历总批次，获取每个批号
        for batch_id in range(batch_count):
            """
            batch_id 就代表着 批次id，例如：0代表第1批，1代表第2批．假设每批次8 条数据.
            batch_id= θ，代表第 1 批，8条/批次，则第1批的数据为:data_lines[0:8］，即：获取索引为0~8的数据，包左不包右
            batch_id=1，代表第 2 批，8条/批次， 则第2批的数据为:data_Lines[8:16］
            batch_id=2，代表第 3 批，8条/批次， 则第3批的数据为:data_lines[16:24]
            """
            # 1.5具体生成每批次的数据，用 yield 放到生成器中
            yield data_lines[batch_id * batch_size : batch_id * batch_size + batch_size]

if __name__ == '__main__':
    my_generator = dataset_loader(3)
    for batch_value in my_generator:
        print(batch_value)
