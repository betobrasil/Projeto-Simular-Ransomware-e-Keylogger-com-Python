# Keylogger Global — Laboratório Educacional

## 1. Sobre o projeto

Este projeto demonstra, para fins educacionais, o funcionamento de um Keylogger em ambiente controlado, utilizando Python e a biblioteca `pynput`.

O programa apresentado utiliza eventos do teclado para registrar teclas pressionadas, identificar a janela que está em primeiro plano e armazenar os registros em um arquivo de texto.

**Atenção:** um keylogger global pode capturar informações sensíveis, incluindo senhas e dados pessoais. Por isso, este código deve ser utilizado exclusivamente em um computador de laboratório, com autorização e sem inserir credenciais reais ou informações privadas.

## 2. Objetivos

- Compreender o funcionamento de um keylogger.
- Conhecer a captura de eventos do teclado.
- Entender como informações podem ser registradas em arquivos de texto.
- Identificar os riscos relacionados a esse tipo de ameaça.
- Estudar medidas de prevenção e detecção.

## 3. Tecnologias utilizadas

- **Python 3:** linguagem utilizada no desenvolvimento.
- **pynput:** biblioteca utilizada para trabalhar com eventos do teclado.
- **ctypes:** utilizada para consultar informações da janela ativa no Windows.
- **datetime:** utilizada para registrar data e horário.
- **pathlib:** utilizada para definir o caminho do arquivo de registro.

## 4. Estrutura dos arquivos

```text
keylogger/
├── registro_simulado.py
├── registro_teclas.txt
└── README.md
```

- `registro_simulado.py`: código-fonte do experimento.
- `registro_teclas.txt`: arquivo local utilizado para armazenar os registros durante os testes.
- `README.md`: documentação do projeto.

**Importante:** o arquivo `registro_teclas.txt` deve permanecer local e não deve ser publicado no GitHub caso contenha informações capturadas.

## 5. Funcionamento do código

O código apresentado possui os seguintes componentes:

1. **Biblioteca pynput:** permite trabalhar com eventos de pressionamento e liberação de teclas.
2. **Identificação da janela ativa:** utiliza funções do Windows para obter o título da janela em primeiro plano.
3. **Registro de eventos:** organiza os eventos com informações de horário e janela identificada.
4. **Teclas especiais:** trata eventos como espaço, Enter e Tab.
5. **Atalhos de controle:** acompanha teclas modificadoras e reconhece a combinação Ctrl + Alt + Esc para encerrar a captura.
6. **Arquivo de registro:** utiliza um arquivo `.txt` para armazenar os dados da sessão.

O código demonstra como esse tipo de ferramenta pode representar um risco à privacidade e à segurança das informações.

## 6. Execução em laboratório

O experimento deve ser realizado somente em ambiente isolado, autorizado e sem dados reais.

Antes de executar, instale a dependência necessária:

```bash
python -m pip install pynput
```

A execução do programa é feita pelo terminal:

```bash
python registro_simulado.py
```

Não utilize o programa para monitorar outras pessoas, capturar senhas ou registrar informações de contas reais.

## 7. Riscos de segurança

Um keylogger pode ser utilizado de maneira maliciosa para:

- Capturar senhas e credenciais.
- Registrar informações digitadas.
- Monitorar atividades do usuário.
- Comprometer a privacidade.
- Facilitar o acesso indevido a contas e sistemas.

## 8. Medidas de prevenção e defesa

Algumas medidas que ajudam a reduzir os riscos de keyloggers:

- Manter o antivírus e o sistema operacional atualizados.
- Utilizar firewall.
- Evitar executar programas de origem desconhecida.
- Verificar processos e aplicativos suspeitos.
- Utilizar autenticação multifator (MFA).
- Não compartilhar credenciais.
- Utilizar ferramentas de monitoramento e análise de segurança.
- Realizar testes de arquivos suspeitos em ambientes isolados, como sandboxes.

## 9. Conclusão

O desenvolvimento deste laboratório permite compreender conceitos relacionados ao funcionamento de keyloggers, ao registro de eventos do teclado e aos riscos associados à captura indevida de informações.

O conhecimento adquirido contribui para identificar comportamentos suspeitos e compreender a importância de medidas preventivas na proteção de sistemas e dados pessoais.

**Projeto desenvolvido para fins educacionais como parte do desafio de cibersegurança da DIO.**