def mostra_domande(domanda: str, risposte: list):
    print(f"Domanda: {domanda}")
    for num_risp in range(1, len(risposte)+1):
        print(f"{num_risp}. {risposte[num_risp-1]}")
    input(f"Scegli una risposta indicando il numero corrispondente: ")

domande = ["Cos'è la CPU?", "Cosa significa RAM?", "Cos'è un bit?"]

risposta_1 = ["Central Processing Unit", "Computer Processors United", "Company Planning UK"]
risposta_2 = ["Random Access Memory", "Return And Mix", "Rage Against Machines"]

mostra_domande(domande[0], risposta_1)
mostra_domande(domande[1], risposta_2)