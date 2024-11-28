# 初始化空列表来存储每个文件的内容
coordinates = []

# 读取 code.txt 文件内容
with open('code.txt', 'r',encoding='utf-8') as file:

    lines = file.readlines()
    max_x, max_y  = 0, 0 
 
# 解析每六行的数据块
for i in range(0, len(lines), 6):
    # 读取 x 坐标、元素 和 y 坐标
    x = int(lines[i].strip())  # 第一行是 x 坐标
    element = lines[i + 2].strip()  # 第三行是元素
    y = int(lines[i + 4].strip())  # 第五行是 y 坐标
    max_x, max_y = max(max_x,x), max(max_y, y)
    # 将结果添加到 coordinates 列表中
    coordinates.append({
        'x': x,
        'element': element,
        'y': y
    })
plate= [['' for _ in range(max_y)] for _ in range(max_x)]

print(len(plate), len(plate[0]))
# 输出结果
for coordinate in coordinates:
    print(coordinate.get('x'))
    #plate[coordinate.get('x')][coordinate.get('y')] = coordinate.get('element')
    
for idx in range(0,max_x):
    for idy in range(0,max_y):
        print(plate[idx][idy])