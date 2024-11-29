def mostra_domande(domande, risposte):
    import random
    for num_dom in range(3)
        print(f"Domanda: {domande[num_dom]}")
        for num_risp in range(1, 4):
            print(f"{num_risp}. {risposte[num_risp-1]}")
    input(f"Scegli una risposta indicando il numero corrispondente: ")

domande = ["Cos'è la CPU?", "Cosa significa RAM?", "Cos'è un bit?"]

risposta_1 = ["Central Processing Unit", "Computer Processors United", "Company Planning UK",
            "Random Access Memory", "R a m", "R A M"]

mostra_domande(domande, risposta_1)