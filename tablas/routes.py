from tablas import app
from flask import render_template

@app.route('/tabla/<numero>')
def tabla(numero):
    try:
        numero=int(numero)
        if numero < 0 or numero > 10:
            return render_template("error.html", valor=numero, text="El valor numérico no está entre 0 y 10")
    except:
        return render_template("error.html", valor=numero, text="El valor introducido no es númerico")

    resultado = []
    for i in range(1,11):
        prod = numero * i
        fila = '{}  *  {}  =  {}'.format(numero,i,prod)
        resultado.append(fila)

    return render_template("tabla.html",tabla=resultado, num=numero)
