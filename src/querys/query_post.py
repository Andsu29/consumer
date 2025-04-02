def query_post(titulo):
    return f"""
    INSERT INTO produtos (titulo) VALUES ('{titulo}');
"""

# -- Inserir registros na base de dados
# insert into users 
# (first_name, last_name, email, password_hash) values
# ("Helena", "A.", "1@email.com", "3_hash"),
# ("Joana", "B.", "2@email.com", "4_hash"),
# ("Rosana", "C.", "3@email.com", "5_hash");