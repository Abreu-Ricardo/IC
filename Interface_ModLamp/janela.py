from calendar import TUESDAY
from hashlib import new
from pickle import TRUE
from struct import pack
from tkinter import HORIZONTAL
from typing import Sequence
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


import sample_class

# Fazer tudo o que esta aqui em baixo com 
# vbox pois grid preenche toda a janela, e ja que
# vamos colocar uma parte de insercao de sequencia
# e outra parte de labels, com os resultados
# vamos usar vbox nas duas partes 



# Usar de exemplo para testes: MTTVVSRTFRDAGQALSLDL



class Janela(Gtk.Window):
    def __init__(self):
        super().__init__(title="Minha Janela")
        self.set_size_request(800, 400)

        self.grid = Gtk.Grid()
        self.grid.set_row_spacing(10)
         
        self.seq_text = Gtk.Label()
        self.seq_text.set_label("Teste de label:   ")


        self.entrada = Gtk.Entry()
        self.entrada.set_placeholder_text("Insira sua sequência aqui...")




        # TESTE APAGAR OU MELHORAR
        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.text_p_1 = Gtk.Label(label="Hidrofobicidade:           ", selectable=TRUE)
        self.text_p_2 = Gtk.Label(label="Valor da carga:            ", selectable=TRUE)
        self.text_p_3 = Gtk.Label(label="Valor do ponto isoelétrico:", selectable=TRUE)
        self.text_p_4 = Gtk.Label(label="Valor do peso Molecular:   ", selectable=TRUE)
        self.text_p_5 = Gtk.Label(label="Valor de Bomam:            ", selectable=TRUE)
        self.text_p_6 = Gtk.Label(label="Tamanho da sequência:      ", selectable=TRUE)

        self.text_p_1.set_justify(Gtk.Justification.LEFT)
        self.text_p_2.set_justify(Gtk.Justification.LEFT)
        self.text_p_3.set_justify(Gtk.Justification.LEFT)
        self.text_p_4.set_justify(Gtk.Justification.LEFT)
        self.text_p_5.set_justify(Gtk.Justification.LEFT)
        self.text_p_6.set_justify(Gtk.Justification.LEFT)

        vbox1.pack_start(self.text_p_1, TRUE, TRUE, 0)
        vbox1.pack_start(self.text_p_2, TRUE, TRUE, 0)
        vbox1.pack_start(self.text_p_3, TRUE, TRUE, 0)
        vbox1.pack_start(self.text_p_4, TRUE, TRUE, 0)
        vbox1.pack_start(self.text_p_5, TRUE, TRUE, 0)
        vbox1.pack_start(self.text_p_6, TRUE, TRUE, 0)


        # Vbox da frente
        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.textVetor = []

        for i in range(0,6):
            self.textVetor.append(Gtk.Label(label="TESTE", selectable=TRUE))


        for i in range(0,6):
            vbox2.pack_start(self.textVetor[i], TRUE, TRUE, 0)




        self.botao_calcula = Gtk.Button()
        self.botao_calcula.set_label("Calcula")
        self.botao_salva = Gtk.Button()
        self.botao_salva.set_label("Salvar")

        self.botao_salva.connect("clicked", self.salvar)
        self.botao_calcula.connect("clicked", self.calcular, self)
         
         

        self.grid.attach(self.seq_text,       1, 1, 1, 1)
        self.grid.attach(self.entrada,        2, 1, 1, 1)
        self.grid.attach(self.botao_calcula,  2, 3, 1, 1)
        self.grid.attach(self.botao_salva,    1, 3, 1, 1)


        self.grid.attach(vbox1, 1, 5, 1, 1)
        self.grid.attach(vbox2, 2, 5, 1, 1)



        self.add(self.grid)
    
    #Passa o objeto janela como 1 parametro e o objeto botao no 2
    def calcular(aux1, aux2, self):
        # print(f"butao calcula pressionado\n aux1:{aux1} \naux2:    {aux2}")
        # print(sample_class.Bomam(aux1.entrada.get_text()))
        
        try:
            # Pega texto digitado e salva em seq e, transforma tudo em caixa alta
            seq = aux1.entrada.get_text().upper()


            print(f"Hidrofobicidade:             {sample_class.hidrofobicidade(seq):.3f}")
            print(f"Valor da carga:              {sample_class.carga(seq)}")
            print(f"Valor do ponto isoeletrico:  {sample_class.ponto_isoeletrico(seq):.3f}")
            print(f"Valor do peso Molecular:     {sample_class.peso_molecular(seq):.3f}")
            print(f"Valor de Bomam:              {sample_class.Bomam(seq):.3f}\n")


            self.textVetor[0].set_label( f"{sample_class.hidrofobicidade(seq):.3f}"   )
            self.textVetor[1].set_label( f"{sample_class.carga(seq):.3f}"             )
            self.textVetor[2].set_label( f"{sample_class.ponto_isoeletrico(seq):.3f}" )
            self.textVetor[3].set_label( f"{sample_class.peso_molecular(seq):.3f}"    )
            self.textVetor[4].set_label( f"{sample_class.Bomam(seq):.3f}"             )
            self.textVetor[5].set_label( f"{len(seq)}"             )


        except ValueError:
            print("Insira uma sequência válida")
            print(ValueError)
    
    def salvar(janela, botao):
        print("Implementar funcao para salvar num arquivo txt todas as propriedades fisico-quimicas")


if __name__ == '__main__':
    jan = Janela()
    jan.connect('destroy', Gtk.main_quit)
    jan.show_all()
    Gtk.main()
