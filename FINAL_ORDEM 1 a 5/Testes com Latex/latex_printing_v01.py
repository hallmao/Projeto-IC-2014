__author__ = 'Michael'

from  final_ode_8_v4 import  Respostas

from pylatex import Document,Section,Subsection,Table,Math,Plot


doc = Document()

section = Section("Este e o primeiro relatorio em PDF para eqs diferenciais v01:")

section.append("Importante notar que essa bagaca esta em fase de testes, pode bugar tudo")


doc.append(section)

doc.generate_pdf()





