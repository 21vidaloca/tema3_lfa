import random
# task 1 - define a cfg
print("task 1")

nonterminale=['S']
terminale=['a','b','']
dict={'S':['aSb','']}
stare_init='S'

cfg=(nonterminale,terminale,stare_init,dict)
print(cfg)

# task 2 - string generator
print("task 2")

def generam():
    contor=0
    ok=1
    sir=stare_init
    while contor<100:
        ok=0
        for x in sir:
            if(x in nonterminale):
                ok=1
                break
        if ok == 0:
            break
        else:
            # inlocuim primul gasit din stanga
            for i in range(0,len(sir)):
                if sir[i] in nonterminale:
                    # inlocuim cu ce avem in dict[sir[i]]
                    # print(dict[sir[i]])
                    ceva=random.choice(dict[sir[i]])
                    aux=sir[:i]+ceva+sir[(i+1):]
                    sir=aux
                    # print(aux)
                    break
            contor+=1
    return sir

siruri_generate=[]
while(len(siruri_generate)<10):
    sir_adaugat=generam()
    if(len(sir_adaugat)<=10): # and (sir_adaugat not in siruri_generate)):
        siruri_generate.append(sir_adaugat)
print(siruri_generate)

# task 3 - derivation
print("task 3")

def derivam(nr_derivari, lista):
    contor=0
    ok=1
    st=[]
    st.append(stare_init)
    while contor<nr_derivari:
        if st == []:
            break
        sir=st[0]
        ok=0
        for x in sir:
            if(x in nonterminale):
                ok=1
                break
        
        if(ok):
            # print(st)
            st.pop(0)
            # inlocuim primul gasit din stanga
            for i in range(0,len(sir)):
                if sir[i] in nonterminale:
                    # inlocuim cu ce avem in dict[sir[i]]
                    # print(dict[sir[i]])
                    for x in dict[sir[i]]:
                        aux=sir[:i]+x+sir[(i+1):]
                        # print(aux)
                        st.append(aux)
                        
                        if(aux not in lista):
                            lista.append((sir,aux))
                    break
            contor+=1
        else:
            st.pop(0)

lista=[]
derivam(6,lista)
rez=[]
ceva=0
def dfs(sir, pereche):
    global ceva
    if("S" in pereche and ceva == 0):
        ceva=1
    for x in lista:
        if(pereche[0] == x[1] and ceva == 0):
            print(x, ceva)
            dfs(sir,x)
            print(x, ceva)
            if(ceva == 1):
                rez.append(x)
                print(x)
print(lista)
sir_ch="aaaSbbb"
for x in lista:
    if(sir_ch == x[1]):
        pereche_buna=x
        break
ceva=0
dfs(sir_ch, pereche_buna)
print(rez[0][0]+"->",end="")
for x in rez:
    print(x[1]+"->",end="")
print(pereche_buna[1])
# task 4 - membership tester
print("task 4")
def testare(sir):
    lista=[]
    derivam(12,lista)
    ok=0
    print(lista)
    for x in lista:
        print(x[1],sir)
        if(x[1] == sir):
            ok=1
            break
        
    if(ok):
        print("True")
    else:
        print("False")


# testare("aaaaaaaaaaabbbbbbbbbbb")
# task 5 - extend your cfg(bonus)