import time, random

from Kasiski_method import kasiski
from ic import match_index, get_key
from _main import is_text_meaningful
# def main():
#     f = open("_1.txt", encoding="UTF-8")
#     ciphertext = f.read()

#     start = time.time_ns()
#     ic = match_index(ciphertext)
#     end = time.time_ns()
#     res1 = end - start
#     print("Длина ключа IC:", ic)
#     #////////


#     start = time.time_ns()
#     k = kasiski(ciphertext)
#     end = time.time_ns()
#     res2 = end - start
#     print("Длина ключа Методом Касиски:", k)
#     if res1 == 0:
#         res1 += 0.001
#     print("Отношение результата:", res2/res1)


#     print("Полученный ключ:", get_key())



#main()
##########################################
# from PyPDF2 import PdfReader
# reader = PdfReader('war-and-peace.pdf')


# f = open("1.txt", "w")

# for i in range(len(reader.pages) - 1500):
#     page = reader.pages[i]
#     text = page.extract_text()
#     #s = ''.join(filter(str.isalpha, text)).upper()
#     s = ''.join(filter(lambda x: x.isalpha() or x.isspace(), text)).upper()
#     f.write(s)
############################################




#################################### разбивает текст по 500 символов
# f = open("1.txt", encoding="UTF-8")
# text = f.read()
# print(text[4])


with open("1.txt", "r", encoding="UTF-8") as e:
    text = e.read().replace("\n", "")

#print(text)

# with open("1.txt", "r", encoding="UTF-8") as f:
#     text = f.read().replace("\n", "")

# text = text.replace('\n', '')

# if '\n' in text:
#     print("HELLO aRTYOM")

tmp = ''
lst = []
count = 0
for i in range(len(text)):
    if count == 200:
        lst.append(tmp)
        tmp = ''
        count = 0
    tmp += text[i]
    
    count += 1
#print(lst)
####################################


#################################### генерируем ключи


import re

arrkey = []

k = 0
tmp = ''
for i in range(3):
    j = random.randint(0, len(text) - 12)
    for k in range(3 + k):
        tmp = tmp + text[j + k]
    #tmp = re.sub(r"\s", "", tmp)
    tmp = tmp.replace(' ', 'W')
    arrkey.append(tmp)
    tmp = ''

print(arrkey, len(arrkey))


####################################

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def of(C):
    return alphabet.index(C)


def vigenere(m, key):
    m = m.upper()
    key = key.upper()
    k = ""
    r = ""
    key_index = 0
    
    for i in range(len(m)):
        if m[i].isspace():
            k += " "
            r += " "
        else:
            if key[key_index % len(key)].isspace():
                key_index += 1

            k += key[key_index % len(key)]
            r += alphabet[(of(m[i]) + of(k[i])) % len(alphabet)]
            key_index += 1

    return r

def vigenere_decrypt(c, key):
    c = c.upper()
    key = key.upper()
    k = ""
    r = ""
    key_index = 0
    
    for i in range(len(c)):
        if c[i].isspace():
            k += " "
            r += " "
        else:
            if key[key_index % len(key)].isspace():
                key_index += 1

            k += key[key_index % len(key)]
            r += alphabet[(of(c[i]) - of(k[i])) % len(alphabet)]
            key_index += 1

    return r


# if ( std::find_if( arr.begin(), arr.end(), [](auto&& var) { return var.key =="1";} ) != arr.end() )
def analysis(lst):
    arr = []
    pos = 274
    f = open("1.txt")
    text = f.read()
    count = 1500
    sum = 0
    f = 0
    a = 0
    j = random.randint(0, int(len(text) / 2))

    for i in range(int(len(arrkey))):
        pos = 200 
        #j = random.randint(0, int(len(text) / 2))
        while count:
            a += 1
            if f == 1:
                j = random.randint(0, int(len(text) / 2))
            if get_key(vigenere(text[j: j + pos], arrkey[i])) in arrkey:
                #print("Succes", get_key(vigenere(text[j: j + pos], arrkey[i])), arrkey[i],len(text[j: j + pos]))
                #print(gke, get_key(vigenere(text[j: j + pos], arrkey[i])), arrkey[i], pos)
                sum += len(text[j: j + pos])
                f = 1
                pos = 200
            else:
                a -= 1
                pos += 20
            count -= 1
        print(sum / a, arrkey[i])
        arr.append(sum/a)
        a = 1
        
        sum = 0
        count = 1500
    return arr



#print(text, len(text))

#a = analysis(lst)
# print(a)

# print("###",vigenere_decrypt(text[1: 1 + 400], arrkey[i]))
# print("###", text[1: 1 + 400])

# import matplotlib.pyplot as plt

# tmp = []
# for i in range(len(arrkey)):
#     tmp.append(len(arrkey[i]))
# print(tmp)

# plt.plot(tmp, a, marker='o', color='r')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("График")

# plt.grid(True)

# plt.show()

# #######Гистограмма быстроты нах. ключа

# import time

# start = time.time_ns()
# print(kasiski(ciphertext))
# print("Время работы Метода Касиски: ", time.time_ns() - start)
