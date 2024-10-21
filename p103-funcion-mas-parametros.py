def saludatodos(*todos):
    print(f"\nSaludos a {todos}")
    print(f"Saludos al primero {todos[0]}")
    print(f"Separados por comas {','.join(todos)}")
    saludatodos("Juan","Pedro","Luis","Gonzalo")