from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extrair', methods=['POST'])
def extrair():

    texto = request.form.get('dados')
    padrao_a_extrair = request.form.get('padrao')

    if padrao_a_extrair == 'pedido':
      padrao = re.compile(r'(\d{16}[A-Z]+\d+)')
    else:
      padrao = re.compile(r'TXAU\d+tx')

    codigos = padrao.findall(texto)

    resultado = ', '.join(f'"{codigo}"' for codigo in codigos)

    return render_template('resultado.html', resultado=resultado)


if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0', port=8000)
