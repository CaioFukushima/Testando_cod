{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "90abc81d-e901-4d4f-8875-d0b443232509",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "\n",
    "#Criar senha\n",
    "x=(\"abcdefghijklmnopqrstuvwxyz\")\n",
    "y=(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\")\n",
    "z=(\"123456789\")\n",
    "w=(\"!@#$%^&*()_+-=[]{}|;:,.<>?\")\n",
    "\n",
    "a=(x+y+z+w)\n",
    "\n",
    "numero1 = int(input(\"Quantos caracteres precisa ter?\")) #\n",
    "resposta = input(\"Quer símbolos especiais? (sim/não) \") #\n",
    "if resposta ==\"não\":\n",
    "     a = x + y + z\n",
    "else:\n",
    "     a = x + y + z +w\n",
    "senha=\"\"\n",
    "for numero2 in range(numero1):\n",
    "    senha=senha+random.choice(a)\n",
    "print(senha)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1b0354f9-8f07-4bf5-90d4-62ea6231c039",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()_+-=[]{}|;:,.<>?\n"
     ]
    }
   ],
   "source": [
    "x=(\"abcdefghijklmnopqrstuvwxyz\")\n",
    "y=(\"ABCDEFGHIJKLMNOPQRSTUVWXYZ\")\n",
    "z=(\"123456789\")\n",
    "w=(\"!@#$%^&*()_+-=[]{}|;:,.<>?\")\n",
    "\n",
    "a=(x+y+z+w)\n",
    "print(a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcb3e05a-af16-4d79-b53f-516dfcf764b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae8a7773-90eb-4ac6-bc77-d366976b1ab3",
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
