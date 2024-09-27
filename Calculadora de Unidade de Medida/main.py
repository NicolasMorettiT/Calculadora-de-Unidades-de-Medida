from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# ---------- Cores ----------

cor1 = '#3b3b3b' # black/preta
cor2 = '#ffffff' #branca
cor3 = '#b03ed6' #roxo
cor4 = '#e6d119' #amarelo
cor5 = '#918727' #amarelo escuro

janela = Tk()
janela.title('')
janela.geometry('650x260')
janela.configure(bg= cor1)
 
 
# ---------- Frames para Janela -----------
frame_cima = Frame(janela, width=450, height=50, bg=cor2, pady = 0, padx = 3, relief=FLAT)
frame_cima.place(x = 2, y = 2 )

frame_esquerda= Frame(janela, width=450, height=220, bg=cor2, pady = 0, padx = 3, relief=FLAT)
frame_esquerda.place(x = 2, y = 54 )

frame_direita= Frame(janela, width=200, height=260, bg=cor2, pady = 0, padx = 3, relief=FLAT)
frame_direita.place(x = 454, y = 2 )

# ---------- Estilo para Janela -----------
 
estilo = ttk.Style(janela)

estilo.theme_use("clam")

# ---------- Configurando Frame Cima -----------

l_app_nome = Label(frame_cima, text='Calculadora de Unidades de Medidas',  height=1, padx= 0, relief=FLAT, anchor=CENTER, font=('Ivy 15 bold'), bg=cor2, fg=cor3 )
l_app_nome.place(x=50, y=10)

# ----------- Configando a funcionalidade ---------
unidades = {
    'massa': [{'kg': 1000}, {'hg': 100}, {'dag': 10}, {'g': 1}, {'dg': 0.1}, {'cg': 0.01}, {'mg': 0.001}],
    'comprimento': [{'km': 1000}, {'hm': 100}, {'dam': 10}, {'m': 1}, {'dm': 0.1}, {'cm': 0.01}, {'mm': 0.001}],
    'tempo': [{'seg': 1}, {'min': 60}, {'hr': 3600}, {'dia': 86400}, {'sem': 604800}, {'mes': 2592000}, {'ano': 31536000}],        'área': [{'km²': 1e6}, {'hm²': 1e4}, {'dam²': 100}, {'m²': 1}, {'dm²': 0.01}, {'cm²': 0.0001}, {'mm²': 0.000001}],
    'quantidade': [{'ml': 1},{'l': 1000},{'m³': 1e6},{'gal': 3785.41}],
    'velocidade': [{'m/s': 1}, {'km/h': 0.277778}, {'mph': 0.44704}],
    'temperatura': [{'C': 'C'}, {'F': 'F'}, {'K': 'K'}],  # Conversão especial
    'energia': [{'J': 1}, {'kJ': 1000}, {'cal': 4.184}, {'kcal': 4184}],
    'pressão': [{'Pa': 1}, {'kPa': 1000}, {'bar': 100000}, {'atm': 101325}]
    }

# ----------- Função de Conversão de Temperatura -----------
def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == unidade_destino:
        return valor

    # Converter para Celsius
    if unidade_origem == 'C':
        celsius = valor
    elif unidade_origem == 'F':
        celsius = (valor - 32) * 5 / 9
    elif unidade_origem == 'K':
        celsius = valor - 273.15
    else:
        raise ValueError("Unidade de origem inválida")

    # Converter de Celsius para a unidade destino
    if unidade_destino == 'C':
        return celsius
    elif unidade_destino == 'F':
        return (celsius * 9 / 5) + 32
    elif unidade_destino == 'K':
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida")

def mostrar_menu(categoria):
    
    unidade_de = []
    unidade_para = []
    unidade_valores = []
    categoria = categoria.lower()
    
    for j in unidades[categoria]:
        for k, v in j.items():
            unidade_de.append(k)
            unidade_para.append(k)
            unidade_valores.append(v)
            
    c_de['values'] = unidade_de
    c_para['values'] = unidade_para
    
    l_unidade_nome['text'] = categoria.upper()
    
    def calcular():
        # Obtendo as unidades
        origem = c_de.get()
        destino = c_para.get()
        
        try:
            # Obtendo o número
            valor = float(e_numero.get())
        except ValueError:
            l_resultado['text'] = "Entrada inválida"
            return
        
                
        if categoria == 'temperatura':
            try:
                resultado = converter_temperatura(valor, origem, destino)
            except ValueError:
                l_resultado['text'] = "Unidade inválida"
                return
        else:
            a_val = unidade_valores.get(origem)
            b_val = unidade_valores.get(destino)

            if a_val is None or b_val is None:
                l_resultado['text'] = "Unidade inválida"
                return

            # Converter de origem para a unidade base
            valor_base = valor * a_val

            # Converter da unidade base para destino
            resultado = valor_base / b_val

        # Formatar o resultado com 4 casas decimais
        l_resultado['text'] = f"{resultado:.2f} {destino}"
    
    # ---------- Criando Label, Botao, Entrada

    l_info = Label(frame_direita, text='Digite o número:',padx=0, pady=3, width = 17, height=2, relief=FLAT, anchor=NW, font=('Ivy 14 bold'), bg=cor2, fg=cor1 )
    l_info.place(x=0, y=110)
    
    e_numero = Entry(frame_direita, width=10 ,font=('Ivy 14 bold'), justify='center', relief=SOLID )
    e_numero.place(x=0, y=150)
    
    b_calcular = Button(frame_direita,text='Calcular',command=calcular, width= 9, height=1, relief=RAISED, overrelief=RIDGE ,anchor=CENTER, font=('Ivy 9 bold'), bg=cor4, fg=cor1)
    b_calcular.place(x=115, y=150)
    
    l_resultado = Label(frame_direita, text='', width=12, height=1, padx=0, pady=3, relief=GROOVE, anchor=CENTER, font=('Ivy 18 bold'), bg=cor2, fg=cor1)
    l_resultado.place(x=0, y=200)
# ---------- Configurando Frame Esquerda -----------

# Botão Massa
img0 = Image.open('images/weight.png')
img0 = img0.resize((50,50), Image.LANCZOS)
img0 = ImageTk.PhotoImage(img0)
b_0 = Button(frame_esquerda, command=lambda: mostrar_menu('massa') ,text='Massa',image=img0, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_0.grid(row=0, column = 0, sticky=NSEW, padx=5, pady=5)

# Botão Tempo
img1 = Image.open('images/time.png')
img1 = img1.resize((50,50), Image.LANCZOS)
img1 = ImageTk.PhotoImage(img1)
b_1 = Button(frame_esquerda,command=lambda: mostrar_menu('tempo'), text='Tempo',image=img1, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_1.grid(row=0, column = 1, sticky=NSEW, padx=5, pady=5)

# Botão Comprimento
img2 = Image.open('images/length.png')
img2 = img2.resize((45,45), Image.LANCZOS)
img2 = ImageTk.PhotoImage(img2)
b_2 = Button(frame_esquerda, command=lambda: mostrar_menu('comprimento'),text='Comprimento',image=img2, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_2.grid(row=0, column = 2, sticky=NSEW, padx=5, pady=5)

# Botão Área
img3 = Image.open('images/size.png')
img3 = img3.resize((50,50), Image.LANCZOS)
img3 = ImageTk.PhotoImage(img3)
b_3 = Button(frame_esquerda, command=lambda: mostrar_menu('área'),text='Área',image=img3, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_3.grid(row=1, column = 0, sticky=NSEW, padx=5, pady=5)

# Botão Quantidade
img4 = Image.open('images/rain.png')
img4 = img4.resize((50,50), Image.LANCZOS)
img4 = ImageTk.PhotoImage(img4)
b_4 = Button(frame_esquerda, command=lambda: mostrar_menu('quantidade'), text='Quantidade',image=img4, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_4.grid(row=1, column = 1, sticky=NSEW, padx=5, pady=5)

# Botão Velocidade
img5 = Image.open('images/speed.png')
img5 = img5.resize((50,50), Image.LANCZOS)
img5 = ImageTk.PhotoImage(img5)
b_5 = Button(frame_esquerda,command=lambda: mostrar_menu('velocidade'), text='Velocidade',image=img5, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_5.grid(row=1, column = 2, sticky=NSEW, padx=5, pady=5)

# Botão Temperatura
img6 = Image.open('images/temperature.png')
img6 = img6.resize((45,45), Image.LANCZOS)
img6 = ImageTk.PhotoImage(img6)
b_6 = Button(frame_esquerda, command=lambda: mostrar_menu('temperatura'),text='Temperatura',image=img6, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_6.grid(row=2, column = 0, sticky=NSEW, padx=5, pady=5)

# Botão Energia
img7 = Image.open('images/energy.png')
img7 = img7.resize((50,50), Image.LANCZOS)
img7 = ImageTk.PhotoImage(img7)
b_7 = Button(frame_esquerda, command=lambda: mostrar_menu('energia'),text='Energia',image=img7, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_7.grid(row=2, column = 1, sticky=NSEW, padx=5, pady=5)

# Botão Pressão
img8 = Image.open('images/pressure.png')
img8 = img8.resize((50,50), Image.LANCZOS)
img8 = ImageTk.PhotoImage(img8)
b_8 = Button(frame_esquerda,command=lambda: mostrar_menu('pressão'), text='Pressão',image=img8, compound=LEFT, width= 130, height=50, relief=FLAT, overrelief=SOLID ,anchor=NW, font=('Ivy 10 bold'), bg=cor3, fg=cor2 )
b_8.grid(row=2, column = 2, sticky=NSEW, padx=5, pady=5)

# ---------- Configurando Frame Direita -----------

l_unidade_nome = Label(frame_direita, text='---', width = 17, height=2, relief=GROOVE, anchor=CENTER, font=('Ivy 15 bold'), bg=cor2, fg=cor1 )
l_unidade_nome.place(x=-10, y=-2)

l_de = Label(frame_direita, text='De', height=1, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), bg=cor2, fg=cor1, padx=3 )
l_de.place(x=10, y=70)

c_de = ttk.Combobox(frame_direita, width= 5, justify=('center'), font=('Ivy 8 bold'))
c_de.place(x=38,y=70)

l_para = Label(frame_direita, text='para', height=1, relief=GROOVE, anchor=CENTER, font=('Ivy 10 bold'), bg=cor2, fg=cor1, padx=3 )
l_para.place(x=90, y=70)
c_para = ttk.Combobox(frame_direita, width= 5, justify=('center'), font=('Ivy 8 bold'))
c_para.place(x=130,y=70)


janela.mainloop()


