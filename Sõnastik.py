rus_list=[]
est_list=[]


def loe_failist(f):
    fail=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        mas.append(rida.strip())      #  добавляет элемент в конец списка. extend() - добавляет в конец списка иметируемую последовательность
    fail.close()
    return mas
def correct(mas1, mas2, f1, f2):
    sona = input("Введите слово: ")
    parandama = input("Какое слово поправить?: ")
    if sona.isascii():        # isascii проверяет на латиницу
        if sona in mas2:
            index = mas2.index(sona)        # index() - возвращает индекс указанного элемента
            mas1[index] = parandama    # index() - возвращает индекс указанного элемента
    else:
        if sona in mas1:
            index = mas1.index(sona)  # index() - возвращает индекс указанного элемента
            mas2[index] = parandama  # index() - возвращает индекс указанного элемента


    fail=open(f1,'w',encoding="utf-8-sig")
    text = ""
    for s in mas1:
        text += s + "\n"
    fail.write(text)  # Производит проверку символов строки на вхождение в таблицу ASCII. Метод вернёт True , если все символы строки входят в ASCII, либо если строка пуста
    fail.close()
    fail=open(f2, 'w', encoding="utf-8-sig")
    text = ""
    for s in mas2:
        text += s + "\n"
    fail.write(text)
    fail.close()

def tolkimine(mas1,mas2):
    sona=input("Введи слово, которое надо перевести (на эстонском языке): ")
    if sona in mas1:
        tolk=mas2[mas1.index(sona)]
    elif sona in mas2:
        tolk=mas1[mas2.index(sona)]
    else:
        tolk="Такого слова в нашем словаре нет"
        global rus_list           #global - позволяет изменять изнутри функции значение глобальной переменной. Оно записывается перед именем переменной, которая дальше внутри функции будет считаться глобальной
        global est_list
        print("Добавьте новое словое - (Jah) или исправить другое? - (Ei)")
        ans = input("Ответ (Jah/Ei): ")
        if ans == "Jah":
            rus_list,est_list=uus_sona(rus_list,est_list,'rus.txt','est.txt')
        elif ans == "Ei":
            correct(mas1,mas2,'rus.txt','est.txt')
    print(f"{sona}-{tolk}")



def uus_sona(mas1,mas2,f1,f2): # f1 - vene, f2 - eesti
    sona1=input("Введи слово: ")
    sona2=input("Введи перевод: ")
    
    if sona1.isascii():   # isascii проверяет латиницу
        mas1.append(sona2) # vene
        mas2.append(sona1) # eesti
    else:
        mas1.append(sona1) # eesti
        mas2.append(sona2) # vene
    fail=open(f1,'a',encoding="utf-8-sig")
    fail.write(sona1+"\n" if not sona1.isascii() else sona2+"\n")  # Производит проверку символов строки на вхождение в таблицу ASCII. Метод вернёт True , если все символы строки входят в ASCII, либо если строка пуста
    fail.close()
    fail=open(f2, 'a', encoding="utf-8-sig")
    fail.write(sona1+"\n" if sona1.isascii() else sona2+"\n")     # fail.write записывает в файл указанную строку
    fail.close()
    return mas1, mas2


rus_list=loe_failist('D:/Visualstudioraboti/Sõnastik/rus.txt')   # пересохранил документ в формате 8 UTF
est_list=loe_failist('D:/Visualstudioraboti/Sõnastik/est.txt')
print(rus_list)
print(est_list)
while True:      # бесконечный цикл
    print(rus_list)
    print(est_list)
    tolkimine(rus_list,est_list)