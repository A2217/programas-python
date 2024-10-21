def saludatodos(*todos):
    print(f"\nSaludos a {todos}")
    print(f"Saludos al primero {todos[0]}")
    print(f"Separados por comas {','.join(todos)}\n")
    for n in todos:
        print('Hola: ',n.upper())

saludatodos("Juan","Pedro","Luis","Gonzalo","Maria")