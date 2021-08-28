Tips
1 对数组排序  sorted(arr,key = lambda x: fun) 对应相关规则 不改变arr 排列 须使用 新变量保存结果 
2 对dict 排序  sorted(dict.items(), key = lambda x:(x[1],x[0]) )  对 val 值进行升序 val 相同对 key 进行升序 
3 DefaultDict  须从collections 引入 些许影响性能 
4可以适应 **matrix  对 二维数组进行按列遍历 
5 bisect_left, right 用法 
6 heapq. 用法
7 求对数 需要引用 math.log10/ math.log2 方法  返回 float 值 