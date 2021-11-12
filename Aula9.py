# arquivo = open('teste.txt', 'w')
# arquivo.write('Minha primera escrita')
# arquivo.close()

# arquivo = open('teste.txt', 'a')
# arquivo.write('\nSegunda linha')
# arquivo.close()
import shutil


def escrever_arquivo(texto):
    diretorio = 'C:/Users/cleber/Documents/Python/teste.txt'
    arquivo = open('C:/Users/cleber/Documents/Python/teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:/Users/cleber/PycharmProjects/app_python')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:/Users/cleber/PycharmProjects/app_python/notas_alunos')

if __name__ == '__main__':
    media_notas('notas.txt')
    #escrever_arquivo('Primeira linha.\n')
    #aluno = 'Rafael, 10, 10, 5, 5'
    #atualizar_arquivo('notas.txt', aluno)
    #ler_arquivo('test.txt')