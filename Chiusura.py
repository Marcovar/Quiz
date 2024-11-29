while True:
    user_input = input("Digita 'esci' per terminare il ciclo: ")
    if user_input.lower() == 'esci':
        print("Il ciclo è terminato.")
        break
    else:
        print(f"Hai digitato: {user_input}")
