def mostra_domande(domanda: str, risposte: list):
    print(f"Domanda: {domanda}")
    i = 1
    x = 0
    # SHUFFLE
    for option, value in risposte.items():
        print(f"{i}. {option}")
        if value == True:
            x = i
        i += 1
    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")
    if int(risp_utente) == x:
        print("Complimenti, risposta corretta!\n")
    else:
        print(f"Risposta errata\n") # DA FARE : la risposta corretta era {risposte.get(True)}

domande = ["Cos'è la CPU?",
           "Cosa significa RAM?",
           "Cos'è un bit?"]
risp = [
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
    mostra_domande(domande[n], risp[n])