from flask import Flask, render_template, request, redirect, url_for
import repositorio

app = Flask(__name__)

@app.route('/')
def home():
    listProducts = repositorio.list_products()
    return render_template("index.html", products=listProducts)

@app.route('/produto/<int:id>', methods=['GET', 'POST'])
def update_product(id):
    if request.method == 'POST':
        if "excluir" in request.form:
            repositorio.delete_product(id)
            return redirect(url_for('home'))
        elif "salvar" in request.form:
            id = request.form['id']
            nome = request.form['nome']
            preco = request.form['preco']
            promocao = request.form['promocao']
            descricao = request.form['descricao']
            imagem = request.form['imagem']

            dados_retornados = repositorio.get_product(id)
            if dados_retornados:
                repositorio.update_product(id=id, nome=nome , preco=preco, promocao=promocao, descricao=descricao, imagem=imagem)
            else:
                repositorio.create_product(nome=nome , preco=preco, promocao=promocao, descricao=descricao, imagem=imagem)

            return redirect(url_for('home'))
    else:
        id, nome, preco, promocao, descricao, imagem = repositorio.get_product(id)
        return render_template("cadastro.html", id=id, nome=nome , preco=preco, promocao=promocao, descricao=descricao, imagem=imagem)


app.run(debug=True)