# -*- coding: UTF-8 -*-
import math
import random
import datetime
T0=50000
T_end = pow(10,-8)
N = 31 #城市数量

#中国31个城市坐标
city_pos = [[1304,2312],[3639,1315],[4177,2244],[3721,1399],
            [3488,1535],[3326,1556],[3238,1229],[4196,1004],
            [4312,790],[4386,570],[3007,1970],[2562,1756],
            [2788,1491],[2381,1676],[1332,695],
            [3715,1678],[3918,2179],[4061,2370],
            [3780,2212],[3676,2578],[4029,2838],
            [4263,2931],[3429,1908],[3507,2367],
            [3394,2643],[3439,3201],[2935,3240],
            [3140,3550],[2545,2357],[2778,2826],
            [2370,2975]]

#计算当前city_list的总长度
#city_list={0,1,2,3,4,5,...,30}
def path_len(city_list):
    len_all = 0

    for i in range(N-1):
        #得到当前要算的两个城市距离的下标a和b
        a = city_list[i]
        b = city_list[i+1]
        len_ab = math.sqrt(pow(city_pos[a][0]-city_pos[b][0],2)+pow(city_pos[a][1]-city_pos[b][1],2))#求a和b两个城市的距离
        len_all = len_all+len_ab

    #计算最后一个城市到第一个城市的距离
    a = city_list[i]
    b = city_list[0]
    len = math.sqrt(pow(city_pos[a][0]-city_pos[b][0],2)+pow(city_pos[a][1]-city_pos[b][1],2))
    len_all = len_all+len
    return len_all

def create_newpath():
    u = random.randint(0, N-1) #产生0到N-1的一个整数型随机数
    v = random.randint(0, N-1)
    city_list[u],city_list[v] = city_list[v],city_list[u]

    return city_list




if __name__ == '__main__':
    #初始化
    random.seed(datetime.datetime.now())  # 用当前时间做种子产生不同的随机数
    T = T0 #初始温度100
    L = 1000 #mapkob链长，初始化为20000
    city_list = []
    city_list_copy = []#保存原始解
    # 初始化一个解city_list
    for i in range(N):
        city_list.append(i)

    while(T>T_end):
        for i in range(1,L):
            city_list_copy = city_list[:] #这里不能用简单的=，否则相当于没有创建新的列表city_list_copy和city_list的值就会永远是一样的
            city_list = create_newpath()#采用两变换法产生新的路径
            f1 = path_len(city_list_copy) #原来的路径长度
            f2 = path_len(city_list) #新路径长度
            df = f2-f1
            if(df>=0):
                r = random.random() #产生0到1之间的随机浮点数
                if(math.exp(-df/T)<=r): #保留原来的解
                    city_list = city_list_copy

        T=T*0.9 #降温


    print(city_list)













