Tips
1 对数组排序  sorted(arr,key = lambda x: fun) 对应相关规则 不改变arr 排列 须使用 新变量保存结果
2 对dict 排序  sorted(dict.items(), key = lambda x:(x[1],x[0]) )  对 val 值进行升序 val 相同对 key 进行升序

排序后遍历无需加 map.items()
3 DefaultDict  须从collections 引入 些许影响性能
4可以适应 zip(*matrix) 对 二维数组进行按列遍历
5 bisect_left(arr, val) 返回第一个 插入的val 的位置  arr 必须有序
6 heapq. 用法
7 求对数 需要引用 math.log10/ math.log2 方法  返回 float

8  arr.remove(val) 只移除第一个匹配的值  [1,1,1,2].remove(1) --> [1,1,2]

9 查看 substring  使用 count 方法 不是.index()

10 perfix sum 是 到 目前为止的 值的sum

11  binaryString to int    call (int,2)
