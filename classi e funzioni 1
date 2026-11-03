#Immagina di essere il gestore di un fast food e vuoi creare un programma che tenga traccia degli ordini dei clienti in
# fila. Ogni cliente fa un ordine con un nome, un'età, e il tipo
#di menu scelto (standard, vegetariano, o per bambini).
#Una volta serviti, i clienti vengono rimossi dalla fila.
#Puoi modellare la fila utilizzando una lista e il Cliente utilizzando una classe Cliente con caratteristiche dei nome,
# età e tipo di menu scelto.


class Cliente:
    def __init__(self,nome,eta,tipo_di_ordine):
       self.nome = nome
       self.eta = eta
       self.tipo_di_ordine = tipo_di_ordine

    def __repr__(self):
        return f"Cliente:{self.nome}, {self.eta} anni--> Tipo di ordine: {self.tipo_di_ordine}"

fila = []

def menu():
    while True:
        print("Menu:")
        print("1. Aggiungi un cliente alla fila")
        print("2. Passa al prossimo ordine")
        print("3. Mostra la fila")
        print("4. Esci")

        scelta= input("scegli un opzione:")
        if scelta == "1":
            nome= input("Come ti chiami?")
            eta= int(input("Quanti anni hai? "))
            tipo_di_ordine= input("Cosa vuoi ordinare? (standard,vegetariano, per bambini)")
            nuovo_cliente = Cliente (nome,eta,tipo_di_ordine)
            fila.append(nuovo_cliente)
        elif scelta == "2":
            if fila:
                cliente_attuale = fila.pop(0)
                print ("stiamo servendo il cliente")
                print (cliente_attuale)
            else:
                print ("La fila è vuota. Non ci sono clienti da servire")
        elif scelta == "3":
            print ("\nfila attuale")
            for cliente in fila:
                print (f"{cliente}")
        elif scelta == "4":
            print ("Stop del programma, arrivederci!")
            break
        else:
            print ("Risposta non valida!")


menu()

