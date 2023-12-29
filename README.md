# Projeto de Extração de Códigos

Este é um projeto simples de Flask para extrair códigos de texto com base em padrões específicos. Ele utiliza expressões regulares para encontrar e exibir os códigos de pedidos ou códigos AWB em um texto fornecido.

## Pré-requisitos

Certifique-se de ter o Python e o Flask instalados no seu ambiente antes de executar o aplicativo. Você pode instalar o Flask usando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando o Aplicativo
Para executar o aplicativo, use o seguinte comando:

```bash
python app.py
```

O aplicativo estará disponível em http://localhost:8000/.

Como Usar
Acesse http://localhost:8000/ no seu navegador.

Insira o texto na caixa de entrada.

Marque a checkbox "Pedido" caso queira extrair com o Regex apropriado.

Clique no botão "Extrair" para obter os resultados.