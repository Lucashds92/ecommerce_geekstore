import sqlite3

#BEN: Gerar um ID novo


#BEN: Criar um novo produto


#VALDETE: Listar todos os produtos


#VALDETE: Mostrar um único produto


#FELIPE: Atualizar produto

def update_product(id:int, nome, preco, promocao, descricao, imagem):
    try:
        conn = sqlite3.connect('ecommerce_products.db')
        cursor = conn.cursor()
        sql_update = "UPDATE ecommerce_products SET nome_product = ?, preco_product = ?, promocao_product = ?, descricao_product = ?, imagem_product = ? WHERE id_product = ?"
        cursor.execute(sql_update, (nome, preco, promocao, descricao, imagem, id))
        conn.commit()
        conn.close()
    except Exception as ex:
        print(ex)
        return False           
      

#FELIPE: Deletar produto

def remove_product(id:int):
    try:
        conn = sqlite3.connect('ecommerce_products.db')
        cursor = conn.cursor()
        sql_delete = "DELETE FROM ecommerce_products WHERE id_products = ?"
        cursor.execute(sql_delete, (id, ))
        conn.commit()
        conn.close()
        return True
    except Exception as ex:
        print(ex)
        return False
