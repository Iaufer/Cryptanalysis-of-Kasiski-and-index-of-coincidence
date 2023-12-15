import Kasiski_method

def match_index(ciphertext):
    # Удалите все неалфавитные символы из зашифрованного текста
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    #print(ciphertext)
    match_index = 0
    text_length = len(ciphertext)
    #print(ciphertext)
    # Попробуйте разные длины ключей и рассчитайте индекс совпадения (IoC)
    for key_length in range(1, text_length):
        sum_ioc = 0

        # Calculate IoC for each shift
        for shift in range(key_length):
            # Count letter frequencies
            freq_count = [0] * 28
            count = 0

            # Подсчет вхождений каждой буквы в заданную смену
            for i in range(shift, text_length, key_length):
                freq_count[ord(ciphertext[i]) - ord('A')] += 1
                count += 1
            #print(freq_count)
            # Рассчитать IoC для смены
            shift_ioc = sum(freq * (freq - 1) for freq in freq_count) / (count * (count - 1))

            sum_ioc += shift_ioc

        # Рассчитать средний IoC для длины ключа
        avg_ioc = sum_ioc / key_length

        # Проверьте, близко ли среднее значение IoC к ожидаемому значению для английского текста.
        if abs(avg_ioc - 0.065) < 0.01:
            match_index = key_length
            break

    return match_index

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def frequency_analysis(group):
    d = {}
    for sym in alphabet:
        d[sym] = group.count(sym)/26
    return d
 


def get_max_value(group):
    tmp = ''
    for i in range(len(group)):
        x = max(frequency_analysis(group[i]), key=frequency_analysis(group[i]).get)
        tmp += x
        #print(x)
    return tmp
    
def key_definition(group):
    sup_key = get_max_value(group)
    #print(sup_key)
    shifted_string = ""
    for char in sup_key:
        # shifted_char = chr(ord(char) - 69 + 65)
        # shifted_string += shifted_char
        if ord(char) - 69 < 0:
            shifted_char = chr(ord(char) - 69 + 91)
            shifted_string += shifted_char
        else:
            shifted_char = chr(ord(char) - 69 + 65)
            shifted_string += shifted_char
    #print(shifted_string)
    return shifted_string
    
        
def decryption(group):
    pass

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

def get_key(s):
    # f = open("_1.txt", encoding="UTF-8")
    # s = f.read()
    keylen = match_index(s)
    s = ''.join(filter(str.isalpha, s)).upper()
    tmp = ''

    group = []

    for i in range(keylen):
        for j in range(i, len(s), keylen):
            tmp = tmp + s[j]
        group.append(tmp)
        tmp = ''

    return key_definition(group)

with open("_1.txt", "r") as file:
    # Читаем строки файла в список
    test_text = file.readlines()

s = "".join(test_text).replace("\n", "")

#f = open("_1.txt", encoding="UTF-8")

#s = f.read()
import time
start = time.time_ns()
print(match_index(vigenere(s, "student")))
end = time.time_ns()
res1 = end - start
print("Время работы IC: ", res1, get_key(vigenere(s, "studenthelloworld")))
#////////


# start = time.time_ns()
# print(Kasiski_method.kasiski(vigenere(s, "studenthelloworld")))
# end = time.time_ns()
# res2 = end - start
# print("Время работы Метода Касиски: ", res2, len(s))

# print(float( ))


from _main import res

ct = vigenere(s, "studenthelloworld")
t = vigenere_decrypt(ct, get_key(ct))
print(t)
print(res(t))




#print(match_index(s))



# #print(group)

# #print(group[0])
# # for i in range(keylen):
# #     print(frequency_analysis(group[i]))
# #print(get_max_value(group))



# # #print(group[0])

# # #print(s)



# # result = ''
# # #chr(ord(char) - 69 + 91)
# # key = key_definition(group)
# # res = ''
# # for i in range(len(s)):
# #     if ord(s[i]) - ord(key[i % len(key)]) < 0:
# #         res += chr(ord(s[i]) - ord(key[i % len(key)]) + 91) 
# #     else:
# #         res += chr(ord(s[i]) - ord(key[i % len(key)]) + 65) 



# # #print(res)

# # #print(s)

