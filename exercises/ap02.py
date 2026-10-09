import sys
sys.stdout.reconfigure(encoding="utf-8")
# comentario
'''
comentario de varias linhas
'''
nome = "Rodrigo"
print("olá" + nome)

print(f"olá {nome}, \nbemvindo!")


#receber dados do utilizador
Informatica = input( f"olá {nome}, escreve o nome de uma disciplina:")

print(f"olá {nome}, \nbemvindo a {Informatica}!")

print("nome é do tipo" + type(nome) .__name__)