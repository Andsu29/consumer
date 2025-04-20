def query_post(titulo, descricao, preco, categoria, marca, modelo, codpro, id, cor):
    return f"""
    INSERT INTO produtos (titulo, descricao, preco, categoria, marca, modelo, codpro, pid, cor) VALUES ('{titulo}', '{descricao}', '{preco}', '{categoria}', '{marca}', '{modelo}', '{codpro}', '{id}', '{cor}');
"""