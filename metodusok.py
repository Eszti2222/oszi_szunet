import math
import random

'''Kérj be egy [200, 920] intervallumban lévő egész számot (ha nem ebben az intervallumban van, jelezz hibát!), majd írasd ki az első számjegyét!'''

def elso():
    szam:int= int(input("Adj meg egy egész számot 200 és 920 között!"))
    if(szam<200 or szam>920): #felvehetjük a 200-at és a 920-at is
        print("A szám nem megfelelő!")
        szam_str = str(szam)
        elso_karakter = szam_str[0]
        print("A szám első karaktere:", elso_karakter)

'''	Egy hétfői napon az 1-es csoportnak 9 órája van. Az első órában a teljesítményük 90%-át képesek nyújtani.
A 2-3. órában már kissé éhesek, és csupán 60%-os a munkabírásuk. A 4-7. órában szerencsére programozást tanulnak, 
így némiképp javul a hatékonyságuk (70%), a 8-9. órában azonban már újra lecsökken (50%).
Írj metódust, mely paraméterében kap egy egész számot 1 és 9 között (melyik órán vannak; jelezz hibát,
ha nem ebben az intervallumban lévő számot kapsz, pl. “Ez már tényleg túlzás.”).
Példa egy esetre: Be: 3, Ki: “Még bírjuk (60%).”  -  nem kell tesztfüggvényeket írni, de az alábbi táblázat alapján ellenőrizzétek a munkátokat!'''

def masodik(szam:int):
    if(szam>=1):
        if(szam==1):
            print("Még 90%-on vagyunk!")
        elif(szam==2 or szam==3):
            print("Még bírjuk (60%)")
        elif(szam==4 or szam==5 or szam==6 or szam==7):
            print("Progit tanulunk, töltődünk! 70%")
        elif(szam==8 or szam==9 ):
            print("Lassan nem bírjuk tovább! 50%")
        else:
            print("Ez már tényleg túlzás!")
    else:
        print("Be se jövök!")


'''⦁	Az egyik diák (legyen Márti a neve) az alábbi algoritmus alapján tevékenykedik az órákon:
⦁	hétfőn alszik az összes órán,
⦁	kedden csak hittan órán figyel,
⦁	programozás órán dolgozik, de csak szerdán
⦁	csütörtökön minden órán figyel, mert jó kedve van (aznap szokott moziba menni),
⦁	pénteken a hétvégéről ábrándozik, így csak félig figyel minden aznapi órán,
⦁	a többi óráról semmit nem tudunk.
Írj metódsut, melynek  2 bemenő prarmétere van (nap neve, óra neve) és tájékoztatást ad Márti állapotáról. 
'''
def harmadik(nap:str,ora:str):

    if(nap[0]=="h"):
        print("Márti alszik")
    elif(nap[0]=="k"):
        if(ora[0]=="h"):
            print("Márti kedden csak a hittan órán figyel")
        else:
            print("Alszik")
    elif(nap[0]=="s"):
        if(ora[0]=="p"):
            print("Márti szerdán csak a programozás órán dolgozik")
        else:
            print("Nincs infó")
    elif(nap[0]=="c"):
        print("Figyel")
    elif(nap[0]=="p"): 
        print("Félig van jelen")
    else:
        print("Nem tudjuk.")

'''A program számítsa ki egy beolvasott valós szám négyzetgyökét! A program adjon hibaüzenetet, ha a felhasználó negatív számból akar gyököt vonni!'''
def negyedik():
    szam:float =input("Adj meg egy számot:")
    szam_float = float(szam)
    if(szam_float>=0):
        x:float= math.sqrt(szam_float)
        print(f"A szám négyzetgyöke: {x}")
    else:
        print("A szám nem megfelelő!")


'''Írj metódust, amelyben 13 véletlen egész számot generálunk [-5;12) intervallumban. A metódus térjen vissza a listával. a következő függvények esetén ezzel a listával dolgozz tovább. Az eredmény kiírása mindig a main.py-ban történjen!

Mennyi a páros számok összege? 
A páros, vagy a páratlan számok összege a nagyobb? 
Mennyi a számok átlaga? 
Mekkora a legnagyobb szám?'''
def otodik():
    vel_lista=[]
    i:int=0
    while(i<13):
        vel_szam:int= int(random.random()*18)-5
        vel_lista.append(vel_szam)
        i+=1
    return vel_lista

'''Hány pozitív és hány negatív szám van? '''
def a_otodik(vel_lista):
    i:int=0
    poz:int=0
    neg:int=0
    null:int=0
    while(i<len(vel_lista)):
        if(vel_lista[i]<0):
            neg+=1
        elif(vel_lista[i]>0):
            poz+=1
        else:
            null+=1
        i+=1
    print(f"Negatív számok {neg} db, pozitív számok {poz} db, nullák {null} db. ")