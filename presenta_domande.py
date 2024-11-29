def mostra_domande(domanda: str, risposte: dict):
    print(f"Domanda: {domanda}")
    i = 1
    x = 0
    # SHUFFLE
    for risposta in risposte.values():
        for option, value in risposta.items():
            print(f"{i}. {option}")
            if value == True:
                x = i
            i += 1
    risp_utente = input(f"Scegli una risposta indicando il numero corrispondente: ")
    if risp_utente == x:
        print("Complimenti, risposta corretta!")
    else:
        print(f"Risposta errata") # DA FARE : la risposta corretta era {risposte.get(True)}

domande = ["Cos'è la CPU?",
           "Cosa significa RAM?",
           "Cos'è un bit?"]
risp = {
"risposta_1":{"Central Processing Unit": True,
              "Computer Processors United": False,
              "Company Planning UK": False},
}

# risposta_2:["Random Access Memory",
#               "Return And Mix",
#               "Rage Against Machines"]
# risposta_3 = ["Un'unità di memoria",
#               "Un simbolo nel codice",
#               "Un elemento grafico"]
# }
risposta_giusta_1 = "Central Processing Unit"
risposta_giusta_2 = "Random Access Memory"
risposta_giusta_3 = "Un'unità di memoria"

# risposte_corrette = ["Central Processing Unit",
#                      "Random Access Memory",
#                      "Un'unità di memoria"]

# mostra_domande(domande[0], risposta_1)
# mostra_domande(domande[1], risposta_2)
# mostra_domande(domande[2], risposta_3)

mostra_domande(domande[0], risp)