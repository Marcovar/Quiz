lista_domande = [
    "Cos'è la CPU?",
    "Cosa significa RAM?",
    "Cos'è un bit?",
    "Qual è la differenza principale tra Linux e Windows?",
    "Cosa si intende per linguaggio macchina?"
]

lista_risposte = [
    ""
]

print("Benvenuto al quiz di informatica! Per uscire, digita exit")
counter_domande = 0
counter_risposte = 1

def mostra_domande(lista_domande: list, lista_risposte: list) -> str:
    print(f"Domanda {counter_domande+1}: {lista_domande[counter_domande]}")
    input(f"Scegli una risposta indicando il numero corrispondente:\n
          1. {lista_risposte[0]}\n
          2. {lista_risposte[1]}\n
          3. {lista_risposte[2]}\n")
    
    
    
    
