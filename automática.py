{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# RPA e Python - Automatize qualquer Processo ou Sistema com Python\n",
    "\n",
    "### pyautogui\n",
    "\n",
    "- Biblioteca para controlar Mouse, Teclado e Tela do Computador com o Python<br>\n",
    "(Link: https://pyautogui.readthedocs.io/en/latest/quickstart.html)\n",
    "\n",
    "\n",
    "- Vamos fazer um exemplo simples aqui, mas repare que isso serve para:\n",
    "    - Qualquer site\n",
    "    - Qualquer programa ou pasta do seu computador\n",
    "    - Qualquer Sistema que você tenha que acessar e automatizar\n",
    "    \n",
    "### Desafio:\n",
    "\n",
    "- Queremos automatizar o backup de arquivos no sistema\n",
    "    - No nosso exemplo, vamos ter que criar um processo que faça o upload de 1 arquivo no Google Drive de forma automática e rápida"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'OK'"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pyautogui\n",
    "import time\n",
    "\n",
    "pyautogui.alert(\"O código vai começar. Não use nada do seu computador enquanto o código está rodando\")\n",
    "pyautogui.PAUSE = 0.5\n",
    "# abrir o google drive no meu computador\n",
    "pyautogui.press('winleft')\n",
    "pyautogui.write('chrome')\n",
    "pyautogui.press('enter')\n",
    "time.sleep(1)\n",
    "pyautogui.write(\"https://drive.google.com/drive/my-drive\")\n",
    "pyautogui.press('enter')\n",
    "\n",
    "# entrar na minha área de trabalho\n",
    "pyautogui.hotkey('winleft', 'd')\n",
    "# cliquei no arquivo que eu quero fazer backup e arrastei ele\n",
    "pyautogui.moveTo(3704, 98)\n",
    "pyautogui.mouseDown()\n",
    "pyautogui.moveTo(2318, 1413)\n",
    "\n",
    "# enquanto eu to arrastando, eu vou mudar para o google drive\n",
    "pyautogui.hotkey('alt', 'tab')\n",
    "time.sleep(1)\n",
    "# larguei o arquivo no google drive\n",
    "pyautogui.mouseUp()\n",
    "\n",
    "# esperar 5 segundos\n",
    "time.sleep(5)\n",
    "\n",
    "pyautogui.alert(\"O código acabou de rodar. Pode usar o seu computador de novo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Point(x=2318, y=1413)"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pyautogui.position()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
