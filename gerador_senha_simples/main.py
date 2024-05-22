from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from random import choice
from string import ascii_lowercase , ascii_uppercase , punctuation , digits
from pyperclip import copy

gerar_v = False # variavel para quando o usuario tenta gerar um senha ta escolher uma opcao.


def Limpar():
    #from main import letra_M ,  letra_m , numeros , simbolos , caracteres_es , todas , gerar 
    global gerar_v
    gerar_v = False
    letra_M.set(False)
    letra_m.set(False)
    numeros.set(False)
    simbolos.set(False)
    caracteres_es.set(False)
    todas.set(False)


def elementos_da_senha(): # pegar as opcao do usuarios e implentas aqui para tratar
    #from main import letra_M ,  letra_m , numeros , simbolos , caracteres_es , todas , gerar
    #importando por aqui para nao da comflito com loop
    gerar['state'] = 'normal'
    global elementos_senha , gerar_v

    #get, nas variavel que estao com valor que o usuarios selecionou la no radio button.
    letras_Ma = letra_M.get()
    letras_Mi = letra_m.get()
    simbolo = simbolos.get()
    numero = numeros.get()
    caracteres_espe = caracteres_es.get()
    todas_op = todas.get()

    if letras_Ma or letras_Mi or simbolo or numero or caracteres_espe or todas_op:
        gerar_v = True
    elementos_senha = [] # ondem os elementos selecionados pelo usuarios na interfacegrafica vai ficar para que depois que seja rondomizada
    #condições que verificar as opcao do usuarios para complementas o 'elemento_senha'
    if letras_Ma or todas_op:
        for valor in ascii_uppercase:
            elementos_senha.append(valor)

    if caracteres_espe or todas_op:
        caracteres_especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
        for valor in caracteres_especiais:
            elementos_senha.append(valor)
    
    if simbolo or todas_op:
        for valor in punctuation:
            elementos_senha.append(valor)

    if numero or todas_op:
        for valor in digits:
            elementos_senha.append(valor)

    if letras_Mi or todas_op:
        for valor in ascii_lowercase:
            elementos_senha.append(valor)

    return elementos_senha


def gerar_senha():
    global gerar_v
    carecteres = elementos_da_senha()
    if gerar_v:
        #from main import comb, label_senha , janela
        label_copiado['text'] = '*Copiado'
        tamanho_senha = comb.get()
        senha = ''
        for valor in range(int(tamanho_senha)):
            elemento = choice(carecteres)
            senha += elemento
        copy(senha)
        label_senha['text'] = senha
        aviso()
    else:
        label_senha['text'] = ''
        label_copiado['text'] = '*Escolhar!!!'


def aviso():
    global historico,  janela
    messagebox.askokcancel('Copiado!' , 'A senha geradar, e copiada automaticamente!')


def cria_janela():
    return Tk()


def loop():
    return janela.mainloop()

#cores usadas
cinza = '#374146'
cor_text = '#FFFFFF'
fonte = 'Arial 14 bold'

#configuração do janela
janela = cria_janela()
janela.title('Gerador de Senha')
janela.geometry('450x530')
janela.config(bg=cinza)
#janela.iconphoto(False , )
janela.resizable(width=False , height=False)

letra_M = BooleanVar() # Letras Maiúsculas
letra_m = BooleanVar() # Letras Minúsculas
numeros = BooleanVar() # numeros 
simbolos = BooleanVar() # Símbolos
caracteres_es = BooleanVar() #Caracteres Especiais
todas = BooleanVar()

#Fremes
#freme titulo
freme_titulo = Frame(janela,  width= 450 , height = 70 , bg = '#64767F')
freme_titulo.place(x = 0 , y = 0)

#abaixo do titulo
freme_b = Frame(janela , width= 450 , height = 20 , bg = '#4E5C63')
freme_b.place(x = 0 , y = 70)

#frames das opcao
frame_op = Frame(janela , width=440 , height=300 ,  bg = '#94AEBB')
frame_op.place(x = 10 , y = 110)

#fremes do botao de confirmar os botãoes
frame_botao = Frame(janela,  width=460 , height = 100 , bg = '#303538')
frame_botao.place(x = 0 , y = 430 )


#Labels
#Label titulo
label_titulo = Label(janela, width=18 , text = 'Gerador De Senha' , bg = '#64767F' , fg = 'White' , font = 'Arial 30 bold' , relief='flat' , anchor='nw')
label_titulo.place(x = 10 , y = 7 )

#Labels de orientação ao opcao
label_op = Label(janela , width=22 , height=1 , text='*Configure os filtro de senha' , font = 'Arial 20 bold' , bg = '#94AEBB' , relief = 'flat')
label_op.place(x = 20 , y = 130)

tamanho_label = Label(janela , width = 17 , height = 1 , text = '*Tamanho da Senha' , font = fonte , bg = '#94AEBB', relief = 'flat' , )
tamanho_label.place(x = 245 , y = 190)

label_senha = Label(janela , width = 15 , height = 2 , text = '' ,  anchor = CENTER , bg = '#64767F' ,  relief = 'flat', font = fonte)
label_senha.place(x = 230 , y = 455)

label_copiado = Label(janela , width = 8 , text = '' , fg = 'Red'  , bg = '#303538', relief = 'flat' , font = 'Arial 8 bold')
label_copiado.place(x = 233 , y = 435)

#botoes

gerar = Button(janela , width=11 , height = 1 , text = 'Gerar Senha' ,font = 'Aril 15 bold' , bg = '#303538', fg = '#7B8890' , relief = 'solid', state ='normal',command = gerar_senha)
gerar.place(x = 30 , y = 460)


limpar_radio = Button(janela , width= 8 ,height =  1 , text = 'Limpar' , font = fonte ,  bg = '#94AEBB' , relief = 'solid' , state = 'normal' , command = Limpar)
limpar_radio.place(x = 280 , y = 350)


#radiobutton
"""Letras Maiúsculas
Letras Minúsculas
Numeros
Símbolos
Caracteres Especiais"""


#radio button letras maiuculas
radiob_1 = Radiobutton(janela , text = 'letras Maiúsculas' , font = fonte , bg = '#94AEBB' , value=True , variable = letra_M)
radiob_1.place(x = 20 , y = 210) 

#radio button Letras Minúsculas
radiob_2 = Radiobutton(janela , text = 'Letras Minúsculas' , font = fonte , bg = '#94AEBB', value = True , variable= letra_m)
radiob_2.place(x =  20 , y = 240)

# radio button numeros 
radiob_3 = Radiobutton(janela , text = 'Nùmeros' , bg = '#94AEBB' ,  font = fonte , value = True , variable= numeros)
radiob_3.place(x =  20 , y = 270)

#Radio button simbolos
radiob_4 = Radiobutton(janela , text = 'Simbolos' , bg = '#94AEBB' ,  font =  fonte , value = True , variable= simbolos)
radiob_4.place(x =  20 , y = 300)

#radio buttton Caracteres Especiais
radiob_5 = Radiobutton(janela , text = 'Caracteres Especiais' , value =  True , variable = caracteres_es , font =  fonte , bg = '#94AEBB')
radiob_5.place(x = 20 , y = 330)

#todas as opcao
radiob_6 = Radiobutton(janela , text = 'Todas' , value = True , variable = todas , font = fonte , bg = '#94AEBB') 
radiob_6.place(x = 20 , y = 360)


#combobox
lista = []
for c in range(8 , 127):
    lista.append(c)

comb = Combobox(janela , value = lista)
comb.current(0)
comb.place(x = 270 , y = 220)

loop()
