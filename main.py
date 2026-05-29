def saudacao(nome):
    return f"Olá, {nome}!"

if __name__ == "__main__":
    print(saudacao("FATEC"))



import sqlite3

def saudacao(nome):
    return f"Olá, {nome}!"

# Uma injeção de SQL clássica misturando variáveis diretamente na query
def buscar_usuario(nome_digitado):
    conn = sqlite3.connect('meubanco.db')
    cursor = conn.cursor()
    
    # O CodeQL nunca perdoa concatenação direta de texto em banco de dados
    query = "SELECT * FROM usuarios WHERE username = '" + nome_digitado + "'"
    cursor.execute(query)
    
    return cursor.fetchall()

if __name__ == "__main__":
    print(saudacao("Mundo"))