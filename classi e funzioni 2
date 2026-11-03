#Sei incaricato di creare un sistema per gestire una biblioteca utilizzando oggetti in Python.
#Modella un menù che consente all'utente di fare una scelta tra le seguenti possibilità:
#Aggiungi un libro alla biblioteca (per semplicità assumiamo che nella biblioteca non si possano inserire più copie dello
#stesso libro)
#Visualizza i dettagli di un libro a partire dal suo titolo (qui devi cercare il libro nella biblioteca.
#E' un punto un po' complicato, non preoccuparti se non ci riesci!!)
#Prendere in prestito un libro
#Restituire un libro
#Mostrare tutti i libri della biblioteca con le loro caratteristiche
#Uscire dal programma
#Per rappresentare il concetto di "Libro" crea una classe con le seguenti caratteristiche:
#Un titolo
#Un autore
#Un anno di pubblicazione
#Una variabile che rappresenta se il libro è disponibile o no
#Nella classe Libro, aggiungi aggiungi i seguenti metodi:
#descrizione() per restituire i dettagli del libro.
#prendi_in_prestito() per segnarlo come "non disponibile".
#restituisci() per segnarlo come "disponibile".




class libro:
    def __init__(self,titolo,autore,anno_di_publicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_di_publicazione = anno_di_publicazione
        self.disponibile=True
    def descrizione(self):
        print(f" {self.titolo}, di {self.autore} pubblicato nel {self.anno_di_publicazione}")
    def prendi_in_prestito(self):
        self.disponibile=False
        print(f"Libro {self.titolo} preso in prestito")
    def restituisci(self):
        self.disponibile=True
        print(f"Libro {self.titolo} restituito")





biblioteca = []
scelta = ""
libro_ricercato = ""
trovato=False


def menu():
    while True:
        print ("--- MENU BIBLIOTECA ---")
        print("1. Aggiungi un libro alla biblioteca")
        print("2. Cerca un libro all'interno della biblioteca")
        print("3. Prendi un libro in prestito")
        print("4. Restituisci un libro")
        print("5. Mostra tutti i libri presenti all'interno della biblioteca")
        print("6. Esci")

        scelta = input("Inserisci un numero per scegliere che cosa fare")
        if scelta == "1":
            nome= input("Inserisci il titolo del libro:")
            autore= input("Inserisci nome e cognome dell' autore del libro:")
            anno_di_publicazione= input("Inserisci anno di pubblicazione del libro:")
            nuovo_libro= libro(nome,autore,anno_di_publicazione)
            biblioteca.append(nuovo_libro)
        elif scelta == "2":
            libro_cercato=input("Che libro stai cercando?")
            for b in biblioteca:
                trovato = False
                if b.titolo.lower() == libro_cercato.lower():
                    print ("Abbiamo il libro ricercato!")
                    trovato = True
                    break
            else:
                print ("Non abbiamo il libro desiderato, ci dispiace!")
        elif scelta == "3":
            libro_prestato= input("Che libro stai cercando?")
            for b in biblioteca:
                trovato = False
                if b.titolo.lower() == libro_prestato.lower():
                    b.prendi_in_prestito()
                    trovato = True
                    break
            else:
                print ("Non abbiamo il libro desiderato, ci dispiace!")
        elif scelta == "4":
            libro_prestato = input("Che libro vuoi restituire? :D")
            for b in biblioteca:
                if b.titolo.lower() == libro_prestato.lower():
                    b.restituisci()
                    trovato = True
                    break
        elif scelta == "5":
            if len(biblioteca) == 0:
                print ("La biblioteca è vuota, inserisci dei libri prima di continuare")
            else:
                print ("Ecco l'elenco dei libri presenti in biblioteca")
                for b in biblioteca:
                    b.descrizione()
        elif scelta == "6":
            break
        else:
            print ("scelta non disponibile")




menu()
