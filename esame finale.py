#La gelateria "Gelato Goloso" ha bisogno di un programma per gestire gli ordini dei clienti utilizzando una lista per
#salvare gli ordini dei clienti. Il programma deve inoltre permettere di:
#Aggiungere un nuovo cliente caratterizzato da nome, tipo di gelato scelto (vaniglia, cioccolato, fragola ecc...) e
#quantità.
#Visualizzare gli ordini e mostrare tutti gli ordini dei clienti.
#Modificare un ordine ovvero poter cambiare o il tipo di gelato o la quantità per un cliente.
#Rimuovere un ordine che elimina l'ordine dalla lista degli ordini.
#Calcolare quanto ogni cliente spende considerando che ogni ordine ha un
#costo (per esempio, ogni cono costa 3€), e deve essere calcolato quanto ogni cliente ha speso.
#Calcolare il fatturato totale che stampa quanto la gelateria ha guadagnato in totale.
#Salvare gli ordini su un file che prende tutti gli ordini e li salva sul file chiamato ordini_gelato.txt.


ordini=[]
scelta=0
contatore_gusto=[]


class Persona:
    def __init__(self, nome, tipo_di_gelato, quantita):
        self.nome = nome
        self.tipo_di_gelato = tipo_di_gelato
        self.quantita = quantita

quantita=str

def gusto():
    while True:
        print("scegli il gusto inserendo il numero corrispondente, uno alla volta")
        print("1.Cioccolato")
        print("2.Fragola")
        print("3.Limone")
        print("4.Biscotto")
        print("5.Menta")
        print("6.Avanti")
        scelta = input("Che gusto vuoi?")
        if scelta == "1":
            contatore_gusto.append("1")
        if scelta == "2":
            contatore_gusto.append("2")
        if scelta == "3":
            contatore_gusto.append("3")
        if scelta == "4":
            contatore_gusto.append("4")
        if scelta == "5":
            contatore_gusto.append("5")
        if scelta == "6":
            break

def stampa_su_file():
    with open("C:\\Users\\Edoar\\OneDrive\\Desktop\\ordini_gelato.txt", "w") as salva_ordini:
        for cliente in ordini:
            gusti_testo = ", ".join(cliente.tipo_di_gelato)
            riga = f"Cliente: {cliente.nome} | Gusti: {gusti_testo} | Coni: {cliente.quantita}\n"
            salva_ordini.write(riga)


def zona_privata():
    while True:
        print("\n--Zona privata--")
        print("Visione ricavi")
        print("1.Spesa per ogni singolo cliente")
        print("2.Ricavo totale")
        print("3.Stampa su file")
        print("4.Torna indietro")
        comando = input("Inserisci il comando")
        if comando == "1":
            selezione= input("Come si chiama il cliente di cui vuoi calcolare la spesa?")
            trovato=False
            for cliente in ordini:
                if cliente.nome == selezione:
                    spesa_singola=(len(cliente.tipo_di_gelato)*0.5+2)*cliente.quantita
                    print(f"Il cliente {cliente.nome}, ha speso \u20AC{spesa_singola}")
                    trovato=True
                    break
            if not trovato:
                print("Persona non trovata tra i clienti")
        elif comando == "2":
            spesa_totale=0
            for cliente in ordini:
                spesa_totale+=(len(cliente.tipo_di_gelato)*0.5+2)*cliente.quantita
            print(f"La spesa totale è \u20AC{spesa_totale}")
        elif comando == "3":
            stampa_su_file()
        elif comando == "4":
            break
        else:
            print("Comando errato")





def menu():
    global contatore_gusto
    while True:
        print("---Benvenuto nella nostra gelateria!---")
        print("Seleziona cosa vuoi fare inserendo il numero corrispondente")
        print("Un cono costa \u20AC2, a cui poi si aggiungono \u20AC0,50 per ogni gusto")
        print("1.Inserisci un ordine")
        print("2.Vuoi modificare il tuo ordine?")
        print("3.Visualizza gli ordini attuali")
        print("4.Cancella un ordine")
        print("5.Accedi all'area privata (Solo Staff)")
        print("6.Esci dal programma")
        scelta= input("Che cosa vuoi fare?")
        if scelta == "1":
            nome= input("Come ti chiami?")
            contatore_gusto=[]
            gusto()
            quantita= int(input("Quanti coni vuoi?"))
            nuova_persona=Persona(nome,list(contatore_gusto),quantita)
            ordini.append(nuova_persona)
            print(f"Ordine ricevuto per{nome}")
        elif scelta == "2":
            nome1 = input("Scrivi qui il nome che hai inserito inizialmente, per favore")
            for cliente in ordini:
                if cliente.nome == nome1:
                    print (f"Ordine trovato:{cliente.nome}. Ha preso:{cliente.quantita}")
                    modifica= input("Vuoi modificare il tuo ordine?")
                    if modifica.lower() == "gusto":
                        contatore_gusto=[]
                        gusto()
                        cliente.tipo_di_gelato=contatore_gusto
                        print("Gusto modicato")
                    elif modifica.lower() == "coni":
                       cliente.quantita=int(input("Quanti coni vuoi ora?"))
                       print("Numero di coni modificato")
                    else:
                        print("C'è un errore nell' inserimento del comando")
                        break
        elif scelta == "3":
            if len(ordini)==0:
                print("Non ci sono ordini al momento")
            else:
                print("\n---ORDINI ATTUALI---")
                for cliente in ordini:
                    print(f" {cliente.nome}ha ordinato {cliente.quantita} cono/i")
        elif scelta == "4":
            if len(ordini) > 0:
                rimosso = ordini.pop()
                print(f"Ultimo ordine rimosso: {rimosso.nome}")
            else:
                print("Nessun ordine presente.")
        elif scelta == "5":
            zona_privata()
        elif scelta == "6":
            print("Arrivederci")
            break
        else:
            print("Comando errato")


menu()




