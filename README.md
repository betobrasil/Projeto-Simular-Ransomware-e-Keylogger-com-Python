# Projeto: Simulação de Ransomware e Keylogger com Python

## Sobre o Projeto

Este projeto foi desenvolvido como parte de um desafio prático de Cybersecurity, com o objetivo de estudar e compreender o funcionamento de dois tipos de malware: **Ransomware** e **Keylogger**.

Utilizando a linguagem Python, foram desenvolvidas simulações em ambiente controlado para demonstrar como essas ameaças podem afetar arquivos e informações dos usuários.

O projeto tem finalidade exclusivamente educacional, buscando também apresentar medidas de prevenção e proteção contra essas ameaças digitais.

## Objetivos

- Compreender o funcionamento de um ransomware.
- Simular a criptografia e descriptografia de arquivos.
- Entender como funciona um keylogger.
- Registrar teclas digitadas durante os testes.
- Identificar os riscos relacionados a esses tipos de malware.
- Estudar medidas de prevenção e segurança da informação.
- Documentar os experimentos utilizando GitHub.

## Tecnologias Utilizadas

- Python 3
- Biblioteca Cryptography (para o experimento de criptografia, caso utilizada pelo script).
- Biblioteca Pynput (para o experimento de registro de teclas).
- Visual Studio Code / IDLE / Editor de código.
- Windows.
- Git e GitHub.

## 1. Experimento: Ransomware Simulado

### Descrição

O primeiro experimento consiste em uma simulação de ransomware utilizando Python.

O objetivo é demonstrar como arquivos podem ser criptografados e posteriormente recuperados por meio de um processo de descriptografia.

### Funcionamento

O experimento contempla:

1. Criação de arquivos de teste.
2. Execução do script de criptografia.
3. Geração de arquivos criptografados com extensão `.protegido`.
4. Simulação de uma mensagem de resgate.
5. Execução do processo de descriptografia.
6. Recuperação dos arquivos originais.

### Evidências

As imagens dos testes estão disponíveis na pasta `images`.

- Código de criptografia.
- Teste de criptografia.
- Arquivos utilizados nos testes.
- Mensagem simulada de resgate.

**Observação:** os testes foram realizados utilizando arquivos próprios, criados exclusivamente para fins educacionais.

## 2. Experimento: Keylogger Simulado

### Descrição

O segundo experimento apresenta uma simulação de keylogger utilizando Python e a biblioteca Pynput.

Um keylogger é um programa capaz de registrar as teclas digitadas pelo usuário. Esse tipo de ameaça pode ser utilizado de maneira maliciosa para capturar informações confidenciais.

### Funcionamento

O script `registro_simulado.py` realiza o registro de teclas durante os testes, armazenando os resultados no arquivo:

`registro_teclas.txt`

O experimento permite observar como ferramentas desse tipo podem capturar informações digitadas e por que é importante proteger o computador contra programas desconhecidos.

### Evidências

As capturas de tela estão disponíveis na pasta `images`.

- Código do registro de teclas.
- Teste de execução do script.
- Arquivo contendo os registros realizados.

**Importante:** o script deve ser utilizado somente em ambiente controlado e com autorização do usuário. O arquivo de registro contém dados de teste e não deve armazenar senhas ou informações pessoais.

## 3. Medidas de Proteção e Defesa

Além das simulações práticas, foi elaborado um documento apresentando medidas de prevenção contra ransomware e keylogger.

O arquivo `defesa/medidas_de_protecao.md` aborda:

- Utilização de antivírus atualizado.
- Configuração de firewall.
- Realização de backups periódicos.
- Atualizações do sistema operacional.
- Utilização de sandbox para análise de programas suspeitos.
- Cuidados com links e arquivos desconhecidos.
- Uso de autenticação multifator.
- Conscientização dos usuários.
- Identificação de possíveis infecções.
- Procedimentos em caso de suspeita de comprometimento.

## Estrutura do Projeto

```text
projeto-malware-python/
│
├── ransomware/
│   ├── arquivos_teste/
│   ├── criptografia.py
│   └── mensagem_resgate.txt
│
├── keylogger/
│   ├── registro_simulado.py
│   ├── registro_teclas.txt
│   └── README.md
│
├── defesa/
│   └── medidas_de_protecao.md
│
├── images/
│   ├── 01-codigo-criptografia.png
│   ├── 02-teste-criptografia.png
│   ├── 03-arquivos-teste.png
│   ├── 04-mensagem-resgate.png
│   ├── 05-codigo-registro-simulado.png
│   ├── 06-teste-registro.png
│   └── 07-registro-teclas.png
│
├── .gitignore
└── README.md
```

## Aprendizados

A realização deste projeto proporcionou conhecimentos práticos sobre:

- Funcionamento de ameaças digitais.
- Criptografia e recuperação de arquivos.
- Captura e registro de informações digitadas.
- Desenvolvimento de scripts utilizando Python.
- Importância da segurança da informação.
- Identificação de comportamentos suspeitos.
- Estratégias de prevenção e proteção contra malwares.
- Organização e publicação de projetos utilizando GitHub.

## Conclusão

O desenvolvimento deste projeto permitiu compreender, na prática, como funcionam duas ameaças importantes no cenário da segurança digital: Ransomware e Keylogger.

Os experimentos demonstraram como essas ferramentas podem comprometer arquivos e informações dos usuários, reforçando a importância de medidas preventivas e boas práticas de segurança.

Mais do que implementar simulações, o objetivo foi compreender os riscos, estudar formas de identificação e conhecer mecanismos de defesa.

**Projeto desenvolvido exclusivamente para fins educacionais, como parte dos estudos de Cybersecurity.**