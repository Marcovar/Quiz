import random

def mostra_domande(domanda: str, risposte: dict):
    print(f"Domanda: {domanda}")
    numero_opzione = 1
    global conta_risposte_giuste
    risposte_tuple = list(risposte.items())
    random.shuffle(risposte_tuple)
    for opzione, verità in risposte_tuple:
        print(f"{numero_opzione}. {opzione}")
        if verità == True:
            numero_risp_giusta = numero_opzione
            risposta_giusta = opzione
        numero_opzione += 1
    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")
    if int(risp_utente) == numero_risp_giusta:
        print("Complimenti, risposta corretta!\n")
        conta_risposte_giuste += 1        
    else: 
        print(f"Risposta sbagliata. La risposta corretta era: {risposta_giusta}.\n")

def conteggio_finale():
    print(f"Il quiz è finito.\nHai risposto correttamente a {conta_risposte_giuste} domande su {len(domande)}.")

def ripeti_quiz():
    risposta = input("Vuoi ripetere il quiz? S/N\n")
    if risposta == "N".lower():
        print("Grazie, alla prossima!")
    else:
        ciclo_quiz()

def inizia_quiz():
    print("Iniziamo il quiz!\n")
    for n in range(len(domande)):
        mostra_domande(domande[n], risposte[n])

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
    global conta_risposte_giuste
    conta_risposte_giuste = 0
    inizia_quiz()
    conteggio_finale()
    ripeti_quiz()

ciclo_quiz()