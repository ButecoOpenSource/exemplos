#!/usr/bin/env python
#-*- encoding: utf-8 -*-


#Author: Pedro Jefferson
#Email: pedrojefferson.developer@gmail.com
#Github: 1pedro
#Blog: http://blog.butecopensource.com/
 
from gi.repository import Gtk
from gi.repository import Gdk
import sqlite3

 
class Main(Gtk.Window):
        def __init__(self):
                #Janela Principal
                Gtk.Window.__init__(self, title="SCU - Sistema de Cadastro de Usuários")
                Gtk.Window.set_size_request(self,600,600)
                Gtk.Window.set_resizable(self,False)
                Gtk.Window.modify_bg(self,Gtk.StateType.NORMAL,Gdk.color_parse("#FFFFFF"))
                #Criando a grid_total, que comportará todos os outros widgets
                self.grid_total = Gtk.Grid()
                self.add(self.grid_total)
                self.grid1 = Gtk.Grid()
                #box1 comportará o título da janela
                self.box1 = Gtk.Box()
                self.grid1.attach(self.box1,0,0,1,1)
                self.labelinit = Gtk.Label()
                #INITTEXT nada mais é que o texto superior da janela principal, contém marcações em pango. "Não confunda com HTML"
                INITTEXT = """<span foreground="#809897" font="30.5" weight="light"><span font="15.5">\n</span>Sistema de Cadastro de Usuários\n</span>"""
                self.labelinit.set_markup(INITTEXT)
                self.box1.pack_start(self.labelinit,expand=True,fill=True,padding=40)
                self.grid2 = Gtk.Grid(column_homogeneous=True,column_spacing=1,row_spacing=10)
                #Texto e Campo de entrada do nome
                self.label_nome = Gtk.Label(label="Nome Completo *")
                self.label_nome.set_halign(Gtk.Align.END)              
                self.grid2.attach(self.label_nome,0,0,1,1)
                self.entry_nome = Gtk.Entry()
                self.entry_nome.set_max_length(150)
                self.entry_nome.set_width_chars(30)            
                self.entry_nome.set_halign(Gtk.Align.START)
                self.grid2.attach(self.entry_nome, 1,0,1,1)
                self.entry_nome.connect("changed",self.on_entry_nome_changed)
                #Texto e campo de entrada para o cpf
                self.label_cpf = Gtk.Label(label="CPF *")
                self.label_cpf.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_cpf,0,3,1,1)
                self.entry_cpf = Gtk.Entry()
                self.entry_cpf.set_max_length(max=11)
                self.entry_cpf.set_width_chars(11)
                self.entry_cpf.set_halign(Gtk.Align.START)
                self.grid2.attach(self.entry_cpf,1,3,1,1)
                #Texto e campo de entrada para o telefone
                self.label_tel = Gtk.Label(label="Tel ")
                self.label_tel.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_tel,0,4,1,1)
                self.entry_tel = Gtk.Entry()
                self.grid2.attach(self.entry_tel,1,4,1,1)
                self.entry_tel.set_max_length(max=17)
                self.entry_tel.set_width_chars(17)
                self.entry_tel.set_halign(Gtk.Align.START)
                self.entry_tel.set_text("+99 99 999999999")
                self.entry_tel.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse("#999999"))
                #Texto e campo de entrada para o email
                self.label_email = Gtk.Label(label="Email ")
                self.label_email.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_email,0,5,1,1)
                self.entry_email = Gtk.Entry()
                self.grid2.attach(self.entry_email,1,5,1,1)
                self.entry_email.set_max_length(80)
                self.entry_email.set_halign(Gtk.Align.START)
                #Texto e campo de entrada para a data de nascimento
                self.label_nasc = Gtk.Label(label="Data de Nascimento *")
                self.label_nasc.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_nasc,0,6,1,1)
                self.entry_nasc = Gtk.Entry()
                self.entry_nasc.set_max_length(12)
                self.entry_nasc.set_width_chars(12)
                self.entry_nasc.set_halign(Gtk.Align.START)
                self.grid2.attach(self.entry_nasc,1,6,1,1)
                self.entry_nasc.set_text("DD/MM/YYYY")
                self.entry_nasc.modify_fg(Gtk.StateType.NORMAL,Gdk.color_parse("#999999"))
                #Texto e campo de entrada para o estado
                self.combo = Gtk.ComboBoxText()
                self.label_combo = Gtk.Label(label="Estado *")
                self.label_combo.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_combo,0,7,1,1)
                self.combo.insert(0,"0", "Bahia")
                self.combo.insert(1,"1", "São Paulo")
                self.combo.insert(2,"2", "Minas Gerais")
                self.combo.insert(3,"3", "Rio de Janeiro")
                self.combo.insert(4,"4", "Tocantins")
                self.combo.insert(5,"5", "Mato Grosso do Sul")
                self.combo.insert(6,"6", "Pernambuco")
                self.combo.set_halign(Gtk.Align.START)
                self.grid2.attach(self.combo, 1,7,1,1)
                #Texto e campo de entrada para a cidade
                self.combo2 = Gtk.ComboBoxText()
                self.label_combo2 = Gtk.Label(label="Cidade *")
                self.label_combo2.set_halign(Gtk.Align.END)
                self.grid2.attach(self.label_combo2,0,8,1,1)
                self.combo2.insert(0,"0","Camaçari")
                self.combo2.insert(1,"1","Dias D'vila")
                self.combo2.insert(2,"2","Vila de Abrantes")
                self.combo2.insert(3,"3","Salvador")
                self.combo2.set_halign(Gtk.Align.START)
                self.grid2.attach(self.combo2,1,8,1,1)
                #Botão de gravar
                self.comit = Gtk.Button(label="Gravar")
                self.comit.set_halign(Gtk.Align.CENTER)
                self.grid_total.attach(self.comit,0,2,2,2)
                self.comit.set_size_request(100,40)
                self.comit.connect("clicked", self.on_comit_clicked)
                #Espaçamento das grids
                self.grid2.set_row_spacing(10)
                self.grid1.set_row_spacing(10)
                self.box3 = Gtk.Box()
                #Colocando a Grid1 e Grid2 na grid principal
                self.grid_total.set_row_spacing(30)
                self.grid_total.attach(self.grid1, 0,0,2,1)
                self.grid_total.attach(self.grid2, 0,1,1,1)
                self.grid_total.attach(self.box3, 0,10,1,1)
 
        #Método que será chamado quando o valor do campo nome mudar,
        def on_entry_nome_changed(self, widget):
                nome = widget.get_text()
                nome = nome.upper()
                return widget.set_text(nome)
 
        #Método que ligará os dados da janela para a função de gravar em banco de dados
        def on_comit_clicked(self, widget):
                nome = self.entry_nome.get_text()
                cpf = self.entry_cpf.get_text()
                data_nasc = self.entry_nasc.get_text()
                estado  = self.combo.get_active_text()
                cidade = self.combo2.get_active_text()
                tel = self.entry_tel.get_text()
                email = self.entry_email.get_text()
 
                if nome != None and cpf != None and data_nasc != None \
                 and estado != None and cidade != None:
                        return comit_dados(None,nome,cpf, tel, email, data_nasc,estado,cidade)
                pass
 
 #Função para gravar no Banco
def comit_dados(*args):
        connection = sqlite3.connect('cadastro.db')
        connection.text_factory = str
        c = connection.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS dados (_id integer , nome text, cpf integer, tel varchar(17), email varchar(150), data_nasc varchar(12), estado varchar(30), cidade varchar(30))')
        c.execute('INSERT INTO dados (_id ,nome, cpf, tel, email, data_nasc, estado, cidade) VALUES (?,?,?,?,?,?,?,?)', (args))
        connection.commit()
 
#Inicialização da aplicação
win = Main()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

