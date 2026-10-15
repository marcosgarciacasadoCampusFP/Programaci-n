plantaactual=int(input("En que planta estas:"))
plantadeseada=int(input("Cual planta quieres ir:"))

if plantaactual<plantadeseada:
    print("Subiendo")
elif plantaactual>plantadeseada:
    print("Bajando")
else:
    print("Ya estás en la planta")