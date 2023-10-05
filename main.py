# IMPORTAÇÕES DAS BIBLIOTECAS A SEREM UTILIZADAS
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import customtkinter as ctk 
from PIL import Image, ImageTk
import math
import sys

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuração da Janela Pricipal        
        self.title('MSA Engenharia e Tecnologia') #título da janela
        self.geometry('700x830') #dimensão da janela
        self.resizable(width=False, height=False) #redimensionar janela
        ctk.set_appearance_mode("system")  
        ctk.set_default_color_theme("dark-blue")

        # Configuração das Abas Superiores
        self.tabview = ctk.CTkTabview(master=self)
        self.tabview.pack(padx=5, pady=5)
        self.tabview.add("Inicial")  # add tab at the end        
        self.tabview.add("Dados Iniciais")  # add tab at the end
        self.tabview.add("Cálculos 1")  # add tab at the end
        self.tabview.add("Cálculos 2")  # add tab at the end
        self.tabview.add("Cálculos 3")  # add tab at the end
        self.tabview.add("Cálculos 4")  # add tab at the end
        self.tabview.set("Inicial")  # set currently visible tab 

        ########################## FRAME 1 ########################## 
        frame1=ctk.CTkFrame(self.tabview.tab("Inicial"),
                      fg_color='MediumSeaGreen',
                      border_width=5,
                      border_color='white',
                      corner_radius=50,
                      width=500, 
                      height=500)
        frame1.pack(pady=15, padx=0)
         
        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame1, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com\n'
                    'Eng. Márcio Batista de Sá', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=30, padx=0)
        
        titulo1 = ctk.CTkLabel(master=frame1,
                      text="Dimensionamento de Estruturas em Concreto Armado\n"
                      "Viga T - Flexão Normal Simples\nConforme a NBR 6118:2014",
                      justify="center",                 
                      text_color='blue',
                      font=('arial narrow', 30, 'bold', 'italic'),                      
                      )
        titulo1.pack(pady=25, padx=10)
         
        img_viga = ctk.CTkImage(light_image=Image.open('vigaT.jpg'), 
        dark_image=Image.open('VigaT.jpg'), size=(400, 250))
        ctk.CTkLabel(master=frame1, text='', 
                    image=img_viga, 
                    compound='left', 
                    padx=10).pack(pady=25, padx=10)

        introdu = ctk.CTkLabel(master=frame1, 
                            text="Cálculo das Áreas de Aço das Armaduras\n"
                            "Seção Transversal T",                       
                            justify="center",                      
                            text_color='black',
                            font=('arial narrow', 25,'italic'),                      
                            )
        introdu.pack(pady=15, padx=10)  

        introdu1 = ctk.CTkLabel(master=frame1, 
                            text="Programa desenvolvido em Python com finalidade de produzir dimensionamento de Vigas em Concreto Armado.\n"
                                "Flexão Normal Simples - Baseado na Norma NBR 6118:2014.\n" 
                                "UTILIZAR APENAS PARA FINS ACADÊMICOS E ESTUDOS.",                       
                            justify="center",                      
                            text_color='#F7FE2E',
                            font=('arial narrow', 15,'italic'),                      
                            )
        introdu1.pack(pady=15, padx=10)        
        
        ########################## FRAME 2 ########################## 
        frame2=ctk.CTkFrame(self.tabview.tab("Dados Iniciais"),
                      fg_color='#1C1C1C',
                      border_width=5,
                      border_color='white',
                      corner_radius=50,
                      width=500, 
                      height=450)
        frame2.pack(padx=50, pady=10)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame2, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).grid(row=0, column=0, columnspan=3, pady=10)

        ########################## TÍTULO 2 ##########################
        titulo2 = ctk.CTkLabel(master=frame2,
                      text="2 - Dados Iniciais",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo2.grid(row=1, column=0, columnspan=2, pady=15) 

        ########################## MOMENTO Mk,máx ##########################
        momento_Mkmax = ctk.CTkLabel(master=frame2,
                      text="Momento Fletor Mk,máx (kN.m)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        momento_Mkmax.grid(row=2, column=0, padx=30, pady=10)

        n1 = ctk.DoubleVar()
        entry_momento_Mkmax = ctk.CTkEntry(master=frame2,
                       textvariable=n1,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_momento_Mkmax.grid(row=3, column=0, padx=30, pady=10)

        ########################## CORTANTE Vk,máx ##########################
        cortante_Vkmax = ctk.CTkLabel(master=frame2,
                      text="Força Cortante Vk,máx (kN)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        cortante_Vkmax.grid(row=2, column=1, padx=30, pady=10)

        n2 = ctk.DoubleVar()
        entry_cortante_Vkmax = ctk.CTkEntry(master=frame2,
                       textvariable=n2,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_cortante_Vkmax.grid(row=3, column=1, padx=30, pady=10)

        ########################## LARGURA bw ##########################
        larg_bw = ctk.CTkLabel(master=frame2,
                      text="Largura bw Viga (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        larg_bw.grid(row=4, column=0, padx=30, pady=10)

        n3 = ctk.DoubleVar()
        entry_larg_bw = ctk.CTkEntry(master=frame2,
                       textvariable=n3,                       
                       width=60,
                       height=30,                                             
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_larg_bw.grid(row=5, column=0, padx=30, pady=10)

        ########################## ALTURA h ##########################
        altura_h = ctk.CTkLabel(master=frame2,
                      text="Altura h Viga (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        altura_h.grid(row=4, column=1, padx=30, pady=10)

        n4 = ctk.DoubleVar()
        entry_altura_h = ctk.CTkEntry(master=frame2,
                       textvariable=n4,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_altura_h.grid(row=5, column=1, padx=30, pady=10)

        ########################## CONCRETO fck ##########################
        classe_fck = ctk.CTkLabel(master=frame2,
                      text="Concreto fck (MPa)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        classe_fck.grid(row=6, column=0, padx=30, pady=10)

        n5 = ctk.DoubleVar()
        entry_classe_fck = ctk.CTkEntry(master=frame2,
                       textvariable=n5,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_classe_fck.grid(row=7, column=0, padx=30, pady=10)

        ########################## AÇO fyk ##########################
        arma_fyk = ctk.CTkLabel(master=frame2,
                      text="Aço Armadura fyk (MPa)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        arma_fyk.grid(row=6, column=1, padx=30, pady=10)

        n6 = ctk.DoubleVar()
        entry_arma_fyk = ctk.CTkEntry(master=frame2,
                       textvariable=n6,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_arma_fyk.grid(row=7, column=1, padx=30, pady=10)    

        ########################## ALTURA ÚTIL d ##########################
        util_d = ctk.CTkLabel(master=frame2,
                      text="Altura Útil d (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        util_d.grid(row=8, column=0, padx=30, pady=10) 

        n8 = ctk.DoubleVar()
        entry_util_d = ctk.CTkEntry(master=frame2,
                       textvariable=n8,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_util_d.grid(row=9, column=0, padx=30, pady=10)

        ########################## Mesa bf ##########################
        mesa_bf = ctk.CTkLabel(master=frame2,
                      text="Largura Mesa bf (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        mesa_bf.grid(row=8, column=1, padx=30, pady=10) 

        n9 = ctk.DoubleVar()
        entry_mesa_bf = ctk.CTkEntry(master=frame2,
                       textvariable=n9,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_mesa_bf.grid(row=9, column=1, padx=30, pady=10)

        ########################## Mesa hf ##########################
        mesa_hf = ctk.CTkLabel(master=frame2,
                      text="Altura Mesa hf (cm)",
                      justify="center", 
                      text_color='white',
                      font=('arial narrow', 15, 'bold')                      
                      )
        mesa_hf.grid(row=10, column=0, padx=30, pady=10, columnspan=2) 

        n10 = ctk.DoubleVar()
        entry_mesa_hf = ctk.CTkEntry(master=frame2,
                       textvariable=n10,                       
                       width=60,
                       height=30,                                            
                       justify="center", 
                       text_color='white',
                       font=('arial narrow', 15, 'bold')                      
                       )
        entry_mesa_hf.grid(row=11, column=0, padx=30, pady=10, columnspan=2)

        ########################## TÍTULO 3 ##########################
        info = ctk.CTkLabel(master=frame2,
                      text="Obrigatório inserir todos os dados\n"
                      "Observar com atenção as unidades indicadas",
                      justify="center", 
                      text_color='red',
                      font=('arial narrow', 16, 'italic')                      
                      )
        info.grid(row=12, column=0, columnspan=2, pady=15)
       
        ########################## FRAME 3 ##########################
        frame3=ctk.CTkFrame(self.tabview.tab("Cálculos 1"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame3.pack(padx=10, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame3, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10)

        ########################## FUNÇÃO CALCULAR ##########################
        def calcular():        
            # Pegando os dados do usuário                         
            num_Mkmax = float(entry_momento_Mkmax.get()) 
            num_vk = float(entry_cortante_Vkmax.get())  
            num_bw = float(entry_larg_bw.get()) 
            num_d = float(entry_util_d.get())
            num_fck = float(entry_classe_fck.get())
            num_fyk = float(entry_arma_fyk.get())
            num_h = float(entry_altura_h.get())
            num_bf = float(entry_mesa_bf.get())
            num_hf = float(entry_mesa_hf.get())
            fcd = (num_fck/10)/(1.4)
            fyd = (num_fyk/10)/(1.15)  

            # Cálculo do Md        
            Md = round(num_Mkmax *1.4*100,2)
            resul_Md.configure(text=f"Md = {Md} kN.cm")   
                            
            # Cálculo da Posição da Linha Neutra (X)
            try:
             X = 1.25*num_d*(1-math.sqrt(1-(Md/(0.425*num_bf*num_d**2*fcd))))
            except ValueError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()

            except ZeroDivisionError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()

            except ArithmeticError:
                messagebox.showerror("Erro", "POR FAVOR, REVEJA SEUS DADOS DE PROJETO E CALCULE NOVAMENTE.")
                #sys.exit()       
            
            verifi_x.configure(text=f"X = {round(X,1)} cm")            
         
            if num_fck <= 50:                  
                    if float(X/num_d) <= 0.45:
                        verifi_045.configure(text=f"Verificação (x/d<0.45) Armadura Simples {round(X/num_d,2)} < 0.45 ")
                    else:
                        verifi_045.configure(text=f"x/d={round(X/num_d,2)} > 0.45\n" 
                                             "Adotar Armadura Dupla ou Rever Projeto")
            else:
                    if float(X/num_d) <= 0.35:
                        verifi_045.configure(text=f"Verificação (x/d<0.35) Armadura Simples {round(X/num_d,2)} < 0.35 ")
                    else:
                        verifi_045.configure(text=f"x/d={round(X/num_d,2)} > 0.45\n" 
                                             "Adotar Armadura Dupla ou Rever Projeto")                  

            # Cálculo dos Limtes X2lim e X3lim (Domínios 2 e 3)
            X2lim = round(num_d*0.26,2)
            X3lim = round(num_d*0.63,2)
            resul_X2lim.configure(text=f"Limite Domínio 2: X2lim = {X2lim} cm")
            resul_X3lim.configure(text=f"Limite Domínio 3: X3lim = {X3lim} cm")

             # Verificação 0,8*X        
            X08 = round(0.8*X,2)
            verifi_08X.configure(text=f"0,8.X = {X08} cm")

            if X08 < num_hf:
                 verifi_ST.configure(text=f"Como {X08} < {num_hf} \n"
                                     "A seção deverá ser dimensionada como Retangular")
            else:
                 verifi_ST.configure(text=f"Como {X08} > {num_hf} \n"
                                     "A seção deverá ser dimensionada como Viga T")
            if X08 > num_hf:
                  M1dT = (num_bf-num_bw)*num_hf*0.85*fcd*(num_d-0.5*num_hf)
                  resul_M1dT.configure(text=f"M1d = {round(M1dT,1)} kN.cm")

                  M2dT = Md - M1dT 
                  resul_M2dT.configure(text=f"M2d = {round(M2dT,1)} kN.cm")

                  XT = 1.25*num_d*(1-math.sqrt(1-(M2dT/(0.425*num_bw*num_d**2*fcd))))
                  resul_XT.configure(text=f"Linha Neutra X,T = {round(XT,1)} cm")

                  if XT/num_d <= 0.45:
                       verifi_XT.configure(text=f"Ok! X,T/d = {round(XT/num_d,2)} <= 0.45\n " 
                                           "A viga pode ser dimensionada")

                  else:
                       verifi_XT.configure(text=f"X,T/d = {round(XT/num_d,2)} > 0.45\n" 
                                           "ERRO: Recomenda-se aumentar altura h")
                       
                  # Cálculo da Área de Aço (As T)           
                  As1 = M1dT/(fyd*(num_d-0.5*num_hf))       
                  resul_As1.configure(text=f"Armadura Longitudinal As1 = {round(As1,2)} cm2") 

                  As2 = M2dT/(fyd*(num_d-0.4*XT))       
                  resul_As2.configure(text=f"Armadura Longitudinal As2 = {round(As2,2)} cm2")

                  AsT = As1 + As2     
                  resul_AsT.configure(text=f"Armadura Longitudinal As = {round(AsT,2)} cm2") 
            else: 
                  resul_M1dT.configure(text=f"M1d = Não Aplicável")
                  resul_M2dT.configure(text=f"M2d = Não Aplicável")
                  resul_XT.configure(text=f"Linha Neutra X,T = Não Aplicável")
                  verifi_XT.configure(text=f"Não Aplicável") 
                  resul_As1.configure(text=f"Não Aplicável")
                  resul_As2.configure(text=f"Não Aplicável")
                  resul_AsT.configure(text=f"Não Aplicável") 

                  # Cálculo da Área de Aço (As Retangular)           
                  As3 = Md/(fyd*(num_d-0.4*X))       
                  resul_As3.configure(text=f"Armadura Longitudinal As = {round(As3,2)} cm2")                        
                   
                  # Cálculo da Área Mínima de Aço (As,min Retangular) 
                  if num_fck <=30:
                         As3min = (0.15*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2") 
                  elif num_fck ==35:
                         As3min = (0.164*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2") 
                  elif num_fck ==40:
                         As3min = (0.179*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck ==45:
                         As3min = (0.179*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck ==50:
                         As3min = (0.208*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck ==55:
                         As3min = (0.211*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck ==60:
                         As3min = (0.219*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck ==65:
                         As3min = (0.226*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")
                  elif num_fck >= 66:
                         As3min = (0.245*num_bw*num_h)/100
                         resul_As3min.configure(text=f"As,min = {round(As3min,1)} cm2")

                  else:
                         resul_As3min.configure(text=f"REVER fck")
                       
            # Cálculo da Cortante Vsd
            Vsd = round(1.4*num_vk,1)
            resul_vsd.configure(text=f"Vsd = {round(Vsd,1)} kN")

            # Cálculo da Cortante Resistente VRd2
            if num_fck ==20:
                 VRd2 = 0.35*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==25:
                 VRd2 = 0.43*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif num_fck ==30:
                 VRd2 = 0.51*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==35:
                 VRd2 = 0.58*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")  
            elif num_fck ==40:
                 VRd2 = 0.65*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif num_fck ==45:
                 VRd2 = 0.71*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN") 
            elif num_fck ==50:
                 VRd2 = 0.77*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            elif 55 <= num_fck <=90:
                 VRd2 = 0.77*num_bw*num_d
                 resul_biela.configure(text=f"VRd2 = {round(VRd2,1)} kN")
            else:
                 resul_biela.configure(text=f"REVER fck")

            # Verificação da Compressão nas Bielas
            if Vsd <= VRd2: 
                verifi_biela.configure(text=f"OK! não ocorrerá esmagamento das bielas de concreto") 
            else: 
                verifi_biela.configure(text=f"Vsd={round(Vsd,1)} > VRd2={round(VRd2,1)}\n Rever Projeto!")

            # Cálculo do Vsd,min            
            if num_fck ==20:
                 Vsdmin = 0.101*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==25:
                 Vsdmin = 0.117*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif num_fck ==30:
                 Vsdmin = 0.132*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==35:
                 Vsdmin = 0.147*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")  
            elif num_fck ==40:
                 Vsdmin = 0.160*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif num_fck ==45:
                 Vsdmin = 0.173*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN") 
            elif num_fck ==50:
                 Vsdmin = 0.186*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            elif 55 <= num_fck <=90:
                 Vsdmin = 0.186*num_bw*num_d
                 resul_vsdmin.configure(text=f"Vsd,min = {round(Vsdmin,1)} kN")
            else:
                 resul_vsdmin.configure(text=f"REVER fck")

            # Verificação do Vsd,min (Armadura Transversal)
            if Vsd <= Vsdmin: 
                verifi_vsdmin.configure(text=f"OK! Adotar Armadura Transversal Mínima") 
            else: 
                verifi_vsdmin.configure(text=f"Vsd={round(Vsd,1)} > Vsdmin={round(Vsdmin,1)}\n Calcular Armadura Transversal!")

            # Cálculo do Asw            
            if num_fck ==20:
                 Asw = (2.55*(Vsd/num_d))-(0.17*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m") 
            elif num_fck ==25:
                 Asw = (2.55*(Vsd/num_d))-(0.20*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==30:
                 Asw = (2.55*(Vsd/num_d))-(0.22*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==35:
                 Asw = (2.55*(Vsd/num_d))-(0.25*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")  
            elif num_fck ==40:
                 Asw = (2.55*(Vsd/num_d))-(0.27*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==45:
                 Asw = (2.55*(Vsd/num_d))-(0.29*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif num_fck ==50:
                 Asw = (2.55*(Vsd/num_d))-(0.31*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            elif 55 <= num_fck <=90:
                 Asw = (2.55*(Vsd/num_d))-(0.31*num_bw)
                 resul_Asw.configure(text=f"Asw = {round(Asw,2)} cm2/m")
            else:
                 resul_Asw.configure(text=f"REVER fck")

            # Cálculo do Asw,min
            fctm = round(0.3*(math.cbrt(num_fck**2)),2)
            Aswmin = ((20*(fctm/10))/(num_fyk/10))*num_bw
            resul_Aswmin.configure(text=f"Asw,min = {round(Aswmin,2)} cm2/m")
            
        # Botão Confirmar
        button = ctk.CTkButton(master=frame3,
                           text='CALCULAR',
                           font=('Arial', 15),
                           width=100,
                           height=50,
                           fg_color='blue',
                           command=calcular)
        button.pack(pady=10)   

        ########################## CÁLCULO DO Md ##########################
        titulo3 = ctk.CTkLabel(master=frame3,
                      text="3 - Momento Fletor de Cálculo (Md)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo3.pack(padx=150, pady=10)

        resul_Md = ctk.CTkLabel(master=frame3,
                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Md.pack(pady=10)
      
        ########################## CÁLCULO DO X ##########################
        titulo4 = ctk.CTkLabel(master=frame3,
                      text="4 - Posição da Linha Neutra - Domínios (X)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo4.pack(padx=150, pady=10)  

        viga1 = ctk.CTkImage(light_image=Image.open('vigaT-LN.jpg'), 
                            dark_image=Image.open('vigaT-LN.jpg'), 
                            size=(350, 250))
        ctk.CTkLabel(master=frame3, 
                    text='', 
                    image=viga1, 
                    compound='left', 
                    padx=10).pack(pady=0, padx=0)     

        resul_X2lim = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_X2lim.pack(pady=10)

        resul_X3lim = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_X3lim.pack(pady=10)

        ########################## VERIFICAÇÃO X ##########################
        verifi_x = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_x.pack(pady=10)

        verifi_045 = ctk.CTkLabel(master=frame3,                       
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_045.pack(pady=10)        

        ########################## FRAME 4 ##########################
        frame4=ctk.CTkFrame(self.tabview.tab("Cálculos 2"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame4.pack(padx=10, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame4, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10, padx=0)  

        ########################## VERIFICAÇÃO SEÇÃO T ########################## 
        titulo5 = ctk.CTkLabel(master=frame4,
                      text="5 - Verificação Hipótese Seção T",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo5.pack(padx=150, pady=10)

        verifi_08X = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_08X.pack(pady=10) 

        verifi_ST = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_ST.pack(pady=10) 

        ########################## CÁLCULO DA SEÇÃO COMO T ########################## 
        titulo6 = ctk.CTkLabel(master=frame4,
                      text="6 - Cálculo da Seção como T",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo6.pack(padx=150, pady=10)

        viga2 = ctk.CTkImage(light_image=Image.open('vigaT-calc.jpg'), 
                            dark_image=Image.open('vigaT-calc.jpg'), 
                            size=(350, 250))
        ctk.CTkLabel(master=frame4, 
                    text='', 
                    image=viga2, 
                    compound='left', 
                    padx=10).pack(pady=0, padx=0)  

        resul_M1dT = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_M1dT.pack(pady=10)

        resul_M2dT = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_M2dT.pack(pady=10)

        resul_XT = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_XT.pack(pady=10)

        verifi_XT = ctk.CTkLabel(master=frame4,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_XT .pack(pady=10)            

        ########################## FRAME 5 ##########################
        frame5=ctk.CTkFrame(self.tabview.tab("Cálculos 3"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame5.pack(padx=0, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame5, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10, padx=0) 

        titulo7 = ctk.CTkLabel(master=frame5,
                      text="6.1 - Área de Aço AS (cm2)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo7.pack(padx=150, pady=10) 

        resul_As1 = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As1.pack(pady=10)

        resul_As2 = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As2.pack(pady=10)

        resul_AsT = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_AsT.pack(pady=10)

        ########################## CÁLCULO DA SEÇÃO COMO RETANGULAR ########################## 
        titulo8 = ctk.CTkLabel(master=frame5,
                      text="7 - Cálculo da Seção como Retangular",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo8.pack(padx=150, pady=10)

        resul_As3 = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As3.pack(pady=10)

        resul_As3min = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_As3min.pack(pady=10)

        ########################## CÁLCULO DA Vsd ########################## 
        titulo9 = ctk.CTkLabel(master=frame5,
                      text="8 - Cálculo da Força Cortante de Cálculo (Vsd)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo9.pack(padx=150, pady=10)

        resul_vsd = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_vsd.pack(pady=10)

        ########################## VERIFICAÇÃO DA BIELA ########################## 
        titulo10 = ctk.CTkLabel(master=frame5,
                      text="10 - Verificação da Compressão nas Bielas",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo10.pack(padx=150, pady=10)

        resul_biela = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_biela.pack(pady=10)

        verifi_biela = ctk.CTkLabel(master=frame5,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_biela.pack(pady=10)

        ########################## FRAME 6 ##########################
        frame6=ctk.CTkFrame(self.tabview.tab("Cálculos 4"),
                       fg_color='#1C1C1C',
                       border_width=5,
                       border_color='white',
                       corner_radius=50,
                       width=400, 
                       height=550)
        frame6.pack(padx=0, pady=15)

        logo = ctk.CTkImage(light_image=Image.open('logo.png'), 
                            dark_image=Image.open('logo.png'), 
                            size=(100, 50))
        ctk.CTkLabel(master=frame6, 
                    text='MSA Engenharia e Tecnologia\ncontato: msa.engtec@gmail.com', 
                    image=logo, 
                    compound='left', 
                    padx=10).pack(pady=10, padx=0) 

        ########################## CÁLCULO DA Vsd,min ########################## 
        titulo11 = ctk.CTkLabel(master=frame6,
                      text="11 - Cálculo da F. C. Solicitante Mínima (Vsd,min)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo11.pack(padx=150, pady=10)

        resul_vsdmin = ctk.CTkLabel(master=frame6,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_vsdmin.pack(pady=10)

        verifi_vsdmin = ctk.CTkLabel(master=frame6,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        verifi_vsdmin.pack(pady=10)

        ########################## CÁLCULO DA Asw ########################## 
        titulo12 = ctk.CTkLabel(master=frame6,
                      text="12 - Cálculo Área Aço Armadura Transversal (Asw)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo12.pack(padx=150, pady=10)

        resul_Asw = ctk.CTkLabel(master=frame6,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Asw.pack(pady=10)

        ########################## CÁLCULO DA Asw,min ########################## 
        titulo13 = ctk.CTkLabel(master=frame6,
                      text="13 - Cálculo Armadura Transversal Mínima (Asw,min)",
                      justify="center", 
                      text_color='yellow',
                      font=('arial narrow', 18, 'bold')                      
                      )
        titulo13.pack(padx=150, pady=10)

        resul_Aswmin = ctk.CTkLabel(master=frame6,                     
                        text="Resultado",
                        justify="center", 
                        text_color='white',
                        font=('verdana', 18, 'italic')                      
                        )
        resul_Aswmin.pack(pady=10)
        
        

      
if __name__ == "__main__":
    app = App()
    app.mainloop()

