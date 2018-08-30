Python 3.7.0a1 (v3.7.0a1:8f51bb436f, Sep 18 2017, 22:34:37) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

from datetime import date
mesporextenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
diadasemana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
hoje = date.today
dia = hoje.day
mes = hoje.month
ano = hoje.year
rodape = São Paulo, %s, %d de %s de %d" %(diadasemana [hoje.weekday()], dia, mesporextenso [mes+1], ano)
print (hoje)
print ("dia.:", dia)
print ("mes.:", mes)
print ("ano.:", ano)
print (rodape)
print ("Daqui 40 dias será ", date.fromordinal(hoje.toordinal() + 40)
print ("dia da semana.: ", hoje.weekday())
