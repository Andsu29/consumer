def query_post(titulo, descricao, preco, categoria, marca, modelo, codpro, id):
    return f"""
    INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro, pid) VALUES ('{titulo}', '{descricao}', '{preco}', '{categoria}', '{marca}', '{modelo}', '{codpro}', '{id}');
"""