def mergeSort(vettore): #definiamo la funzione mergeSort che prende in input il vettore dato dall'utente e, successivamente, i sottovettori calcolati

       print("Suddivisione ",vettore) #stampa a schermo la fase di suddivisione del vettore in quel momento 

       if len(vettore)>1: #controllo lunghezza vettore in esame. Se meggiore di 1
           #divido il vettore in due sotto vettori
           mid = len(vettore)//2
           primaparte = vettore[:mid] #primà metà del vettore
           secondaparte = vettore[mid:] #secobda metà del vettore

           #ricorsione (funzione si richiama fino a quando il vettore è pari a 1)
           mergeSort(primaparte)
           mergeSort(secondaparte)

           #definiamo tre variabili di valore iniziale nullo (chiamate a, b e c)
           a=0
           b=0
           c=0

           while a < len(primaparte) and b < len(secondaparte): #ciclo while: mentre a è minore della lunghezza del primo vettore e b minore del secondo vettore
               if primaparte[a] < secondaparte[b]: #se l'elemento a del primo vettore è minore dell'elemento b del secondo vettore
                   vettore[c]=primaparte[a] #l'elemento c del vettore iniziale sarà pari all'elemento a del primo vettore
                   a=a+1 #a aumenta di 1
               else:
                   vettore[c]=secondaparte[b] #l'elemento c del vettore iniziale sarà pari all'elemento b del secondo vettore 
                   b=b+1 #b aumenta di 1
               c=c+1 #c aumenta di 1

           while a < len(primaparte): #ciclo while: mentre a è minore della lunghezza del vettore prima parte
               vettore[c]=primaparte[a] #l'elemento c del vettore iniziale sarà pari all'elemento a del primo vettore
               a=a+1 #a aumenta di 1
               c=c+1 #c aumenta di 1

           while b < len(secondaparte): #ciclo while: mentre a è minore della lunghezza del vettore prima parte
               vettore[c]=secondaparte[b] #l'elemento c del vettore iniziale sarà pari all'elemento b del secondo vettore
               b=b+1 #b aumenta di 1
               c=c+1 #c aumenta di 1

       print("Unione ",vettore) #Il vettore viene assemblato ordinato


while True: #è un ciclo while che permette in Python di far riavviare il codice fino a quando non è l'utente a fermare l'esecuzione del programma
    #'sequenza principale' del codice
    vettore = list(map(int,input("Inserire vettore (solo numeri interi): ").split())) #Viene richiesto all'utente il vettore iniziale, separato da uno spazio
    mergeSort(vettore) #richiama la funzione merge sort
    print("Vettore ordinato ",vettore) #stampa il vettore

    Risposta = str(input("Vuoi fermarti? (Nel caso inserire 'S') ")) #chiede se continuare
    if Risposta == "S": #se si inserisce la lettere 'S'
        break #il vettore si ferma
        
