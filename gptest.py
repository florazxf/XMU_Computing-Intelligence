# -*- coding: UTF-8 -*-

from collections import deque  # python自带的队列模型


def searchResult(n=-1,no=0,initial_state=[10,0,0],final_state = [5,5,0]):


    search_queue = deque() #建立一个双端队列
    search_queue.append((no,initial_state,n)) #把初始结点加入到队列中 (当前序号，列表，父节点序号)
    searched = [] #用于记录检查过的结点
    search_order = [] #用于记录找到final_state的广度优先遍历顺序
    no = 0
    while search_queue: #队列不为空时循环执行
        elementn = search_queue.popleft()  #对队列中的第一项进行判断，出队
        element = elementn[1]
        n = elementn[0]
        if element not in searched:  #此元素没有被检查过才判断
            #search_order.append(element)
            search_order.append(elementn)
            searched.append(element)
            if element == final_state:
                return search_order
            else:
                # 一斤瓶倒入七两瓶
                if element[0]>0 and element[1]<7: #一斤瓶中有油且七两瓶中不满
                    no = no+1
                    if element[0]+element[1]>=7:   #(A,B,C) and B<7 and A+B>=7  -> (A+B-7,7,C)  一斤瓶油装满七两瓶
                        search_queue.append((no,[element[0] + element[1] - 7,7,element[2]],n))
                    else:                          # (A,B,C) and A>0 and A+B<7  ->(0,A+B,C) 一斤瓶中油全倒入七两瓶
                        search_queue.append((no,[0, element[0] + element[1], element[2]],n))

                #一斤瓶倒入三两瓶
                if  element[0]>0 and element[2]<3:#一斤瓶中有油且三两瓶中不满
                    no = no + 1
                    if element[0]+element[2]>=3: #(A,B,C) and C<3 and A+C>=3  -> (A+C-3,B,3) 一斤瓶油装满三两瓶
                        search_queue.append((no,[element[0] +element[2]-3, element[1], 3],n))
                    else:                        #(A,B,C) and A>0 and A+C<=3  ->(0,B,A+C) 一斤瓶中油全倒入三两瓶
                        search_queue.append((no,[0, element[1], element[0]+element[2]],n))

                #七两瓶倒入三两瓶
                if  element[1]>0 and element[2]<3:
                    no = no + 1
                    if element[1]+element[2]>=3: #(A,B,C) and C<3 and B+C>=3  -> (A,B+C-3,3) 七两瓶油装满三两瓶
                        search_queue.append((no,[element[0],element[1] +element[2]-3, 3],n))
                    else:                        #(A,B,C) and B>0 and B+C<=3  ->(A,0,B+C) 七两瓶中油全倒入三两瓶
                        search_queue.append((no,[element[0],0, element[1]+element[2]],n))

               #七两瓶倒入一斤瓶
                if  element[1]>0 and element[0]<10:
                    no = no + 1
                    if element[0]+element[1]>=10: #(A,B,C) and A<10 and B+A>=10 ->(10,A+B-10,C)七两瓶油装满一斤瓶
                        search_queue.append((no,[10, element[0] + element[1] - 10, element[2]],n))
                    else:                        #(A,B,C) and B>0 and A+B<=10 ->(A+B,0,C) 七两瓶中油全倒入一斤瓶
                        search_queue.append((no,[element[0]+element[1], 0, element[2]],n))

              #三两瓶倒入七两瓶
                if element[1] < 7 and element[2] >0:
                    no = no + 1
                    if element[1] + element[2] >= 7:  # (A,B,C) and B<7 and B+C>=7 ->(A,7,B+C-7) 三两瓶油装满七两瓶
                        search_queue.append((no,[element[0], 7, element[1] + element[2] - 7],n))
                    else:  # (A,B,C) and C>0 and B+C<=7  ->(A,B+C,0) 三两瓶中油全倒入七两瓶
                        search_queue.append((no,[element[0], element[1] + element[2], 0],n))


              #三两瓶倒入一斤瓶
                if element[0] < 10 and element[2] > 0:
                    no = no + 1
                    if element[0] + element[2] >= 10:  # (A,B,C) and A<10 and A+C>=10 ->(10,B,A+C-10) 三两瓶油装满一斤瓶
                        search_queue.append((no,[10, element[1], element[0] + element[2] - 10],n))
                    else:  # (A,B,C) and C>0 and A+C<=10 ->(A+C,B,0) 三两瓶中油全倒入一斤瓶
                        search_queue.append((no,[element[0] + element[2], element[1], 0],n))



if __name__ == '__main__':
    #初始化状态
    initial_state = [10,0,0]
    oil_volume = [10, 7, 3]
    final_state = [5,5,0]
    n = 0
    results = searchResult()

    shuchuls = []  #把搜索到的结点都放入shuchuls这个列表中
    i = len(results)-1
    shuchu = results[i]
    while shuchu[2]!=-1:
        while shuchu[2] != results[i - 1][0]:
            i = i-1
        shuchuls.append(shuchu[1])
        shuchu = results[i-1]
    shuchuls.append(initial_state)


    for i in range(len(shuchuls)-1,-1,-1):
        print(shuchuls[i])


