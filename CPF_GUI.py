import tkinter as tk
from tkinter import *
import random
from datetime import time, datetime


class CPFGenerator:
    def __init__(self, master):
        # Cria a janela principal
        self.master = master
        self.master.title("Gerador de CPF")
        self.master.configure(bg="black")
        self.master.geometry('300x300+700+200')

        # Mensagem do Topo 'GERADOR CPF FAKE'
        msgTopo = Label(text='Gerador CPF \n Fake', bg='black', fg='white', font=('Courier', 20,'bold', 'italic'))
        msgTopo.place(x=50, y=1)

        # Cria um campo de entrada para o CPF
        self.entry = tk.Entry(self.master, width=12, bg="white", font=("Helvetica", 18,'bold', 'italic'))
        self.entry.place(x=80, y=70)
        # Relogio
        self.clock()
        # Cria a Label Creditos
        self.labelColorido()
        self.update_time()


        # Testo CPF do Entry 'CPF'
        cpfText = Label(text='CPF:', bg='black', fg='RED', font=("Helvetica", 16, 'bold', 'italic'))
        cpfText.place(x=10, y=70)

        # Cria os botões "Gerar novo CPF" e "Limpar CPF"
        self.generate_button = tk.Button(self.master, text="Gerar novo CPF",font=('Arial', 10, 'italic', 'bold'), bd=2, fg='white',
                           bg='black', command=self.generate_cpf)
        self.generate_button.place(x=110, y=120)
        self.clear_button = tk.Button(self.master, text='Limpar CPF', font=('Arial', 10, 'italic', 'bold'), bd=2, fg='white',
                           bg='black')
        self.clear_button.place(x=120, y=150)

    def clock(self):
        tempo = datetime.now()
        horas = tempo.strftime('%H:%M:%S')
        exibir = Label(text=f'{horas}', font=("Helvetica", 10), bg="black",fg='RED')
        exibir.place(x=235, y=280)
        self.master.after(1000, self.clock)
    def generate_cpf(self):
        # Gera um novo CPF aleatório
        cpf = [random.randint(0, 9) for _ in range(9)]
        cpf.append(self.calculate_first_verifier_digit(cpf))
        cpf.append(self.calculate_second_verifier_digit(cpf))

        # Trocar de cor ao clicar para gerar CPF
        self.labelColorido()
        self.update_time()
        # Exibe o CPF gerado no campo de entrada
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "".join(map(str, cpf)))

    def calculate_first_verifier_digit(self, cpf):
        # Calcula o primeiro dígito verificador do CPF
        total = 0
        for i in range(9):
            total += cpf[i] * (10 - i)
        verifier = 11 - (total % 11)
        if verifier == 10 or verifier == 11:
            verifier = 0
        return verifier

    def calculate_second_verifier_digit(self, cpf):
        # Calcula o segundo dígito verificador do CPF
        total = 0
        for i in range(9):
            total += cpf[i] * (11 - i)
        total += cpf[9] * 2
        verifier = 11 - (total % 11)
        if verifier == 10 or verifier == 11:
            verifier = 0
        return verifier

    def clear_cpf(self):
        # Limpa o campo de entrada
        self.entry.delete(0, tk.END)

    def labelColorido(self):
        self.label = Label(text='Lucas Matheus GDS', bg='black', fg='white')
        self.label.place(x=1, y=280)
        # Chama a função update_time a cada 60000 milissegundos (1 minuto)
        self.master.after(60000, self.update_time)

    def update_time(self):
        # Obtém a hora atual e atualiza a Label
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.configure(text='Lucas Matheus GDS')

        # Muda a cor da Label de acordo com o minuto atual
        current_minute = datetime.now().second
        if current_minute % 2 == 0:
            self.label.configure(fg="yellow")
        else:
            self.label.configure(fg="blue")

        # Chama a função update_time a cada 60000 milissegundos (1 minuto)
        self.master.after(60000, self.update_time)

# Cria a janela principal e inicializa a aplicação
root = tk.Tk()
app = CPFGenerator(root)
root.mainloop()
