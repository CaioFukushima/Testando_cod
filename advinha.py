{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2e0af3a4-21ac-46cd-afe5-cf1409dfc634",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite um número: 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Muito baixo! Tente um maior.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite um número: 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Muito baixo! Tente um maior.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite um número: 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Muito baixo! Tente um maior.\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite um número: 9\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Paranéns!Você acertou em 4 tentativas\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "#Jogo de advinhar o número\n",
    "numero=random.randint(1,10)\n",
    "chute = 0\n",
    "tentativas = 0\n",
    "while chute!=numero:\n",
    "    chute=int(input(\"Digite um número:\"))\n",
    "    tentativas = tentativas + 1\n",
    "    if chute==numero:\n",
    "        print(f\"Paranéns!Você acertou em {tentativas} tentativas\")\n",
    "    else:\n",
    "       if chute > numero :\n",
    "        print(\"Muito alto! Tente um menor.\")\n",
    "       else:\n",
    "           print(\"Muito baixo! Tente um maior.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4385effd-24ca-4f5b-8e04-c717773ebf11",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00002bb5-3e24-4ad5-8be9-a6312fab92d4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
