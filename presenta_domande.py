import random
def mostra_domande(domanda: str, risposte: dict):
    print(f"Domanda: {domanda}")
    numero_opzione = 1
    numero_risp_giusta = 0
    risposte_tuple = list(risposte.items())
    random.shuffle(risposte_tuple)
    for option, value in risposte_tuple:
        print(f"{numero_opzione}. {option}")
        if value == True:
            numero_risp_giusta = numero_opzione
            risposta_giusta = option
        numero_opzione += 1
    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")
    if int(risp_utente) == numero_risp_giusta:
        print("Complimenti, risposta corretta!\n")
    else: 
        print(f"Risposta errata. La risposta corretta era: {risposta_giusta}.\n")

domande = ["Cos'è la CPU?",
           "Cosa significa RAM?",
           "Cos'è un bit?"]

risposte = [
        {"Central Processing Unit": True,
        "Computer Processors United": False,
        "Company Planning UK": False},

        {"Random Access Memory": True,
        "Return And Mix": False,
        "Rage Against Machines": False},

        {"Un'unità di memoria": True,
        "Un simbolo nel codice": False,
        "Un elemento grafico": False}
        ]

# risposta_giusta_1 = "Central Processing Unit"
# risposta_giusta_2 = "Random Access Memory"
# risposta_giusta_3 = "Un'unità di memoria"

# risposte_corrette = ["Central Processing Unit",
#                      "Random Access Memory",
#                      "Un'unità di memoria"]

# mostra_domande(domande[0], risposta_1)
# mostra_domande(domande[1], risposta_2)
# mostra_domande(domande[2], risposta_3)

for n in range(len(domande)):
    mostra_domande(domande[n], risposte[n])