lista=[]
func=''
current=''
lista_undo=[]
count_play=0
count_current=0
while func!= 'fight':
    if count_current==0 and len(lista)>0:
        current=lista[0]
    func=input()
    f=func.split(' ')
    if f[0]=='add':
        if len(lista)==0:
            current=f[1]
        lista.append(f[1])
        lista_undo.append([f[0],f[1]])
        
    elif f[0]=='del':
        if count_play>0:
            if f[1] in lista and f[1] != current :
                index=lista.index(f[1])
                lista.remove(f[1])
                lista_undo.append([f[0],f[1],index])
        else:
            if f[1] in lista:
                try:
                    current=lista[lista.index(current)+1]
                    count_current+=1
                except IndexError:
                    current=lista[0]
                    count_current+=1                
                index=lista.index(f[1])
                lista.remove(f[1])
                lista_undo.append([f[0],f[1],index])
                
            
    elif f[0]=='play':
        if len(lista)>0 and count_play<1:
            count_play+=1
            lista_undo.append([f[0]])
    elif f[0]=='list':
        if len(lista)>0:
            print(','.join(lista))
        else:
            print('[vazia]')
            
    elif f[0]=='current':
        if len(lista)>0:
            print(current)
        else:
            print('Toque! Toque, Dijê!')
    elif f[0]=='next':
        if f[1]!= current and (f[1] in lista):
            next_add=lista.index(f[1])
            lista.insert((lista.index(current)+1),f[1])
            if lista.index(current)>next_add:
                lista_undo.append([f[0],f[1],next_add,lista.index(current)])
                lista.pop(next_add)
            else:
                lista_undo.append([f[0],f[1],next_add,lista.index(current)])
                lista.pop(next_add+1)

            
        if count_play==0 and f[1] in lista:
            current=f[1]
            count_current+=1
    elif f[0]=='ended':
        if count_play>0:
            lista_undo=[]
            try:
                current=lista[lista.index(current)+1]
                count_current+=1
            except IndexError:
                current=lista[0]
                count_current+=1
    elif f[0]=='undo' and len(lista_undo)>0:
        if len(f)==1:
            lista_i=[lista_undo[-1]]
            i=lista_undo[-1]
        elif len(f)>1:
            lista_i=lista_undo
        
        for i in lista_i:
            if i[0]=='next'and i[1] in lista:
                nextadd_inverso=lista.index(i[1])
                if i[3]>i[2]:
                    lista.insert(i[2],i[1])
                    lista.pop(nextadd_inverso+1)
                else:
                    lista.insert(i[2]+1,i[1])
                    lista.pop(nextadd_inverso)
                count_current-=1
            
            elif i[0]=='add' and i[1] in lista:
                lista.reverse()
                lista.remove(i[1])
                lista.reverse()
            elif i[0]=='del':
                lista.insert(i[2],i[1])
                count_current-=1
            elif i[0]=='play':
                count_play=0
                


        if len(f)==1:
            lista_undo.pop(-1)
        elif len(f)>1:
            lista_undo=[]
    elif f[0]=='stop':
        count_play=0

if func=='fight':
     print('Jedi Wagner, assuma o comando!')
    
    
                
            