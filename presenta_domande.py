import random

def mescola_elementi(dizionario):
    """Prende gli elementi all'interno di un dizionario e li mette in ordine casuale"""

    database_list = list(dizionario.items())
    random.shuffle(database_list)
    return dict(database_list)
    
def mostra_domande(database: dict):
    """Presenta le domande e le opzioni di risposta in ordine casuale.
    Domande e risposte hanno un contatore."""

    conta_domande = 0
    conta_risposte_giuste = 0

    for domanda, risposte in (mescola_elementi(database)).items():
        conta_domande += 1
        print(f"Domanda {conta_domande}: {domanda}")
        numero_opzione = 1
        for opzione, verità in (mescola_elementi(risposte)).items():
            print(f"{numero_opzione}. {opzione}")
    
            if verità == True:
                numero_risp_giusta = numero_opzione
                risposta_giusta = opzione

            numero_opzione += 1

        conta_risposte_giuste += verifica_risposta(numero_risp_giusta, risposta_giusta)
    return conta_risposte_giuste

def verifica_risposta(numero_giusto, risp_giusta):
    """Verifica se la risposta dell'utente è vera o falsa,
    assegna un punteggio e mostra la risposta giusta.
    Gestisce le eccezioni in caso di risposta non numerica
    e con una Q permette di uscire dal programma."""

    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")

    try:
        if int(risp_utente) == numero_giusto:
            print("Complimenti, risposta corretta!\n")    
            return 1        
        else:
            print(f"Risposta sbagliata. La risposta corretta era: {risp_giusta}.\n")
            return 0
    except:
            if risp_utente == "Q".lower():
                print("Hai scelto di chiudere il quiz. Alla prossima!")
                pass
            else:
                print("Risposta non valida. Inserisci un numero o digita Q per chiudere il quiz.")
                return(verifica_risposta(numero_giusto, risp_giusta))
            


def conteggio_finale(conta_giuste):
    """Mostra il risultato finale del quiz con il numero di risposte corrette sul totale"""

    print(f"Il quiz è finito.\nHai risposto correttamente a {conta_giuste} domande su {len(dom_risp)}.")


def ripeti_quiz():
    """Chiede all'utente se vuole rifare il quiz. Se l'input non è corretto, la funzione riparte"""

    risposta = input("Vuoi ripetere il quiz? S/N\n")
    if risposta == "N".lower():
        print("Grazie, alla prossima!")
    elif risposta == "S".lower():
        ciclo_quiz()
    else:
        print("Risposta non valida. Digita S per continuare oppure N per chiudere.")
        ripeti_quiz()

def inizia_quiz():
    """Saluta l'utente, azzera il contatore e lancia la funzione per mostrare le domande.
    Passa il risultato alla funzione per calcolare il risultato finale"""

    print("Iniziamo il quiz!\n")
    return mostra_domande(dom_risp)

# # domande = ["Cos'è la CPU?",
#            "Cosa significa RAM?",
#            "Cos'è un bit?",
#            "Quando è uscita la prima versione di Python?",
#            "Quale di questi è un linguaggio di programmazione?"]

# risposte = [
        # {"Central Processing Unit": True,
        # "Computer Processors United": False,
        # "Company Planning UK": False},

        # {"Random Access Memory": True,
        # "Return And Mix": False,
        # "Rage Against Machines": False},

        # {"Un'unità di memoria": True,
        # "Un simbolo nel codice": False,
        # "Un elemento grafico": False},
        
        # {"1991": True,
        # "1978": False,
        # "1985": False},
        
        # {"C++": True,
        # "D--": False,
        # "E==": False}
        # ]

dom_risp = {
            "Cos'è la CPU?":
            {"Central Processing Unit": True,
            "Computer Processors United": False,
            "Company Planning UK": False},

           "Cosa significa RAM?":
           {"Random Access Memory": True,
            "Return And Mix": False,
            "Rage Against Machines": False},
            
            "Cos'è un bit?":
            {"Un'unità di memoria": True,
            "Un simbolo nel codice": False,
            "Un elemento grafico": False},

            "Quando è uscita la prima versione di Python?":
            {"1991": True,
            "1978": False,
            "1985": False},

            "Quale di questi è un linguaggio di programmazione?":
            {"C++": True,
            "D--": False,
            "E==": False}
            }

def ciclo_quiz():
    """Esegue tutti gli step del quiz"""
    try:
        conteggio_finale(inizia_quiz())
        ripeti_quiz()
    except:
        pass


ciclo_quiz()