
from pathlib import Path
from cryptography.fernet import Fernet

# Diretório exclusivo dos arquivos de teste
PASTA_TESTES = Path(__file__).parent / "arquivos_teste"

# Arquivos que serão utilizados no experimento
ARQUIVO_ORIGINAL = PASTA_TESTES / "documento1.txt"
ARQUIVO_CRIPTOGRAFADO = PASTA_TESTES / "documento1.protegido"
ARQUIVO_RECUPERADO = PASTA_TESTES / "documento1_recuperado.txt"

# Gerar uma chave de criptografia
chave = Fernet.generate_key()
cifra = Fernet(chave)

# Ler o conteúdo original
conteudo = ARQUIVO_ORIGINAL.read_bytes()

# Criptografar o conteúdo
conteudo_protegido = cifra.encrypt(conteudo)

# Salvar uma cópia criptografada
ARQUIVO_CRIPTOGRAFADO.write_bytes(conteudo_protegido)

print("Arquivo de teste protegido com sucesso!")

# Descriptografar a cópia
conteudo_recuperado = cifra.decrypt(conteudo_protegido)

# Salvar o conteúdo recuperado em outro arquivo
ARQUIVO_RECUPERADO.write_bytes(conteudo_recuperado)

print("Arquivo recuperado com sucesso!")

# Verificar se o conteúdo é idêntico ao original
if conteudo == conteudo_recuperado:
    print("VERIFICACAO: OK - Conteúdo original preservado!")
else:
    print("VERIFICACAO: ERRO - Conteúdo diferente!")
