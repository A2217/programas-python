#procesa dos listas de cadenas (nombres)
def procesa(nombres1, nombres2):
    todos = nombres1 + nombres2
    todos.sort()
    for i in range(len(todos)):
        todos[i] = todos[i].upper()
    return todos

def entrada():
    dat = []
    while True:
        d= input ('Nombre: ')
        if d == '':break
        dat.append(d)
    return dat

#n1 = ['Juan', 'Pedro', 'Luis', 'Jose', 'Maria']
n1=entrada()
n2 = ['Rocio', 'Teresa', 'Karla']
todos = procesa(n1,n2)

print (todos)