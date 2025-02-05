import random

def mostra_domande(domanda: str, risposte: dict):
    """Presenta le domande e le risposte. Le risposte sono in ordine casuale. 
    L'utente può rispondere e riceve un messaggio diverso a seconda che la risposta sia giusta o sbagliata"""

    print(f"Domanda: {domanda}")
    numero_opzione = 1

    risposte_tuple = list(risposte.items())
    random.shuffle(risposte_tuple) # mescolo l'ordine delle risposte
    
    # mostro tutte le risposte per una domanda
    for opzione, verità in risposte_tuple:
        print(f"{numero_opzione}. {opzione}")
        
        if verità == True:
            numero_risp_giusta = numero_opzione
            risposta_giusta = opzione

        numero_opzione += 1
    
    return verifica_risposta(numero_risp_giusta, risposta_giusta)

    # risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")

    # if int(risp_utente) == numero_risp_giusta:
    #     print("Complimenti, risposta corretta!\n")    
    #     return 1   
    # else:
    #     try:
    #         print(f"Risposta sbagliata. La risposta corretta era: {risposta_giusta}.\n")
    #         return 0
    #     except:
    #         print("Risposta non valida.")

def verifica_risposta(numero_giusto, risp_giusta):
    """Verifica se la risposta dell'utente è vera o falsa, assegna un punteggio e mostra la risposta giusta"""

    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")

    try:
        if int(risp_utente) == numero_giusto:
            print("Complimenti, risposta corretta!\n")    
            return 1   
        else:
            print(f"Risposta sbagliata. La risposta corretta era: {risp_giusta}.\n")
            return 0
    except:
            print("Risposta non valida. Inserisci un numero.")
            verifica_risposta(numero_giusto, risp_giusta)


def conteggio_finale(conta_giuste):
    """Mostra il risultato finale del quiz con il numero di risposte corrette sul totale"""

    print(f"Il quiz è finito.\nHai risposto correttamente a {conta_giuste} domande su {len(domande)}.")


def ripeti_quiz():
    """Chiede all'utente se vuole rifare il quiz. Se l'input non è corretto, la funzione riparte"""

    risposta = input("Vuoi ripetere il quiz? S/N\n")
    if risposta == "N".lower():
        print("Grazie, alla prossima!")
    elif risposta == "S".lower():
        ciclo_quiz()
    else:
        print("Risposta non valida. Digita S oppure N.")
        ripeti_quiz()

def inizia_quiz():
    """Saluta l'utente, azzera il contatore e lancia la funzione per mostrare le domande.
    Passa il risultato alla funzione per calcolare il risultato finale"""

    print("Iniziamo il quiz!\n")
    conta_risposte_giuste = 0
    for n in range(len(domande)):
        conta_risposte_giuste += mostra_domande(domande[n], risposte[n])
    return conta_risposte_giuste

domande = ["Cos'è la CPU?",
           "Cosa significa RAM?",
           "Cos'è un bit?",
           "Quando è uscita la prima versione di Python?",
           "Quale di questi è un linguaggio di programmazione?"]

risposte = [
        {"Central Processing Unit": True,
        "Computer Processors United": False,
        "Company Planning UK": False},

        {"Random Access Memory": True,
        "Return And Mix": False,
        "Rage Against Machines": False},

        {"Un'unità di memoria": True,
        "Un simbolo nel codice": False,
        "Un elemento grafico": False},
        
        {"1991": True,
        "1978": False,
        "1985": False},
        
        {"C++": True,
        "D--": False,
        "E==": False}
        ]

def ciclo_quiz():
    """Esegue tutti gli step del quiz"""

    conteggio_finale(inizia_quiz())
    ripeti_quiz()


ciclo_quiz()