#Nestedlist
if __name__ == '__main__':
    dic={}
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in dic:
            dic[score].append(name)
        else:
            dic[score]=[name]
        if score not in s:
            s.append(score)
            
    m=min(s)
    s.remove(m)  
    m1=min(s)  
    
    dic[m1].sort()
    for i in dic[m1]:
        print(i)




#Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(tuple(integer_list).__hash__()) 


# List Comprehensions

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
   #Solution 1 
   # res=[]
   # for i in range(x+1):
   #     for j in range(y+1):
   #         for k in range(z+1):
   #             if i+j+k !=n:
   #                 res.append([i,j,k])
    #print(res)  
    #Solution 2              
    res=[[i,j,k]for i in range(x+1)for j in range(y+1)for k in range(z+1) if i+j+k !=n ]
    print(res)


   