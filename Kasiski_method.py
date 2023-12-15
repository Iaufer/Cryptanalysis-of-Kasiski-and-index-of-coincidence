import re
import time
def gcd(num):
    gcdl = []
    for i in range(1, sorted(num)[0] + 1):
        for index, j in enumerate(num):
            if j % i == 0:
                if (index + 1) == len(num):
                    gcdl.append(i)
                    break
                continue
            else:
                break
    if not gcdl:
        return 1
    else:
        return sorted(gcdl)[-1]

def kasiski(ciphertext):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    seglen = 3
    cipher = ciphertext
    seglist = []
    for i in range(seglen):
        segtmp = re.findall(r'.{3}', cipher)
        seglist += segtmp
        cipher = re.sub(r'.', '', cipher, count=1)
    repeatlist = []
    for i in range(len(seglist)):
        for j in range(len(seglist)):
            if (seglist[i] == seglist[j] and i != j):
                repeatlist.append(seglist[i])
    repeatlist = list(set(repeatlist))
    arr = []
    for i in repeatlist:
        count = ciphertext.count(i)
        if (count < 3): continue
        loclist = [0] * count
        pre = 0
        for j in range(count):
            loc = ciphertext.find(i, pre)
            loclist[j] = loc
            pre = loc + 1
        sublist = []
        
        
        for j in range(1,count):
            sublist.append(loclist[j]-loclist[j-1])
        arr.append(gcd(sublist))
        # lst = []


        # _sublist = []
        # for i in range(1, count):
        #     _sublist.append(loclist[i]-loclist[i-1])

        # #print(gcd(_sublist))        
        # print(gcd(_sublist))
        # #print(len(_sublist))

    #print(arr)

    return Freq3(arr)


def Freq3(b):
  m, i = 0, 0 # Максимальная частота и соответствующее ему значение
  for x in b:
    c = b.count(x) # Сколько раз встречается x в массиве b?
    if c > m:
      m, i = c, x
  return i

# f = open("1.txt", encoding="UTF-8")
# ciphertext = f.read()

# start = time.time_ns()
# print(kasiski(ciphertext))
# print("Время работы Метода Касиски: ", time.time_ns() - start)



# a =[1, 2, 3]
# b =[4, 5, 6]
# c =[7, 8, 9]
# d =[10, 11, 12]


# lst = []
# lst.append(a)
# lst.append(b)
# lst.append(d)
# lst.append(c)
# print(lst)










