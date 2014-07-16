from sympy import Function, dsolve, pprint, exp, cos
from sympy.abc import t
from sympy import *

prec = 2 ## Numero de digitos decimais de precisão mostrados no log de dados


# #Loop para testes
while True:

	#Entrada pelo console
	def input_coefs():
		global a5, a4, a3, a2, a1, a0, xT
		print "Insira os coefs e entrada para uma EDO do tipo: "
		print "a5*y'''''(t) + a4*y''''(t) + a3*y'''(t)  + a2*y''(t) +a1*y'(t) +a0*y(t) = x(t)"
		a5 = input("a5:")
		a4 = input("a4:")
		a3 = input("a3:")
		a2 = input("a2:")
		a1 = input("a1:")
		a0 = input("a0:")
		xT = input("x(t):")


	input_coefs()

	try:
		xT = float(xT)
	except:
		pass
	print type(xT)

	##Defining our function
	y = Function('y')

	##Adicionando os coefs a eq diferencial
	eq = sympify(
		a5 * y(t).diff(t, 5) + a4 * y(t).diff(t, 4) + a3 * y(t).diff(t, 3) + a2 * y(t).diff(t, 2) + a1 * y(t).diff(
			t) + a0 * y(t) - xT)

	pprint(eq)
	print ""

	###Dif equation solver

	##Sets if it is of homogenous or inhomogenous type and type of resolution method
	if xT == 0:
		solvedEq = dsolve(sympify(eq), y(t), hint='nth_linear_constant_coeff_homogeneous')
		#elif (a3 != 0) or (a4 != 0) or (a5 != 0):
		#solvedEq = dsolve(sympify(eq),y(t),hint='nth_linear_constant_coeff_variation_of_parameters')
		pass
	else:
		solvedEq = dsolve(sympify(eq), y(t), hint='nth_linear_constant_coeff_undetermined_coefficients')

	##Transformação do tipo sympy_unity para o sympy_mul (mais operações permitidas)
	sepEq = solvedEq._args[1]

	print(sympify(solvedEq, rational=False, evaluate=False).evalf(2))

	##PRocesso de separação de resp natural e resposta transitória ---
	#SEPARACAO FUNCIONAL SOMENTE PARA GRAU 1 E 2
	#elementosEq = sepEq.atoms(Symbol)
	#C1 = elementosEq.pop()
	#C2 = elementosEq.pop()

	C1, C2, C3, C4, C5 = symbols("C1 C2 C3 C4 C5")

	#print C1, C2

	if a5 != 0:
		RespFor = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0), (C5, 0)])
	elif a4 != 0:
		RespFor = sepEq.subs([(C1, 0), (C2, 0), (C3, 0), (C4, 0)])
	elif a3 != 0:
		RespFor = sepEq.subs([(C1, 0), (C2, 0), (C3, 0)])
	elif a2 != 0:
		RespFor = sepEq.subs([(C1, 0), (C2, 0)])
	elif a1 != 0:
		RespFor = sepEq.subs(C1, 0)

	##    if C2 != t :
	##        #print "Tem c2"
	##        RespTran =  sepEq.subs([(C2,0),(C1,0)])
	##
	##
	##    else:
	##        RespTran =  sepEq.subs(C1,0)

	##Resposta transitória alocada em  RespTran, natural em RespNat


	formaNatural = sepEq.subs(RespFor, 0)
	## fN é a mesma coisa, mas usado por um bug bizarro do Sympy que exige uma variável sem alocações prévias quando diferenciando
	##isso é válido no método conds_iniciais_aplicadas
	fN = formaNatural

	##Tenta resolver parâmetros não terminados, se possível
			try:
				formaNatural = solve(formaNatural)
				fN           = solve(fN)
				RespFor      = solve(RespFor)
			except:
				pass


	print "Resposta Forçada:"
	pprint (RespFor.evalf(prec))
	print "Forma Natural:"
	pprint(formaNatural.evalf(prec))
	##Saida

	def conds_iniciais_aplicadas():

		print "Favor inserir as conds iniciais y(0) e y'(0)...:"

		##Verificando a ordem da EDO para se ter o numero correto de conds Iniciais e
		#uma resolução própria

		#Ordem 1
		if ((a5 == 0) and (a4 == 0)
		   and (a3 == 0) and (a2 == 0)):
			#Entrada cond inicial:
			y0 = input("y(0): ")
			##Resolução para se obter o valor da constante C1:

			#Aplicando t = 0 em y(t)
			fNt0 = fN.subs(t,0)
			#print "Valor de fN com t = 0:",fNt0
			##Resolvendo o sistema para se obter o valor da constante C1
			valorConstantes = solve(fNt0 - y0)
			#print "Valor de C1: ",valorConstantes,type(valorConstantes)



			##Agora a resposta natural, com o C1 encontrado na substituição aplicado na funcão natural:
			nC1 = valorConstantes.pop()

			respNatural = fN.subs(C1,nC1).evalf(prec)

			##Tenta resolver parâmetros não terminados, se possível
			try:
				respNatural = solve(respNatural)
			except:
				pass

			##Saida da Resposta Natural no console
			print "Resposta Natural:"
			pprint(respNatural)




		#Ordem 2
		elif ((a5 == 0) and (a4 == 0)
		   and (a3 == 0)):
			y0 = input("y(0): ")
			dy0 = input("y'(0): ")

			##Primeiramente a resposta Natural
			##Solucao geral é : formaNat
			#antes de aplicar as conds iniciais é necessário ter y'(t) e y(t) da resp natural

			#Forma natural é derivada uma vez
			ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
			formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
			#print"yLinhaNat:", ylinhaNat

			## Agora é necessário resolver o sistema:
			#  ynat(t) = y(0)
			#  ynat'(0)= y'(0)
			#print "Valor das constantes com t",valorConstantes
			### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
			ylinhaNat    = ylinhaNat.subs(t,0)
			formaNatural = formaNatural.subs(t,0)

			#print "YlinhaNat em t = 0: ",ylinhaNat
			#print "Forma Natural em t = 0: ",formaNatural
			##Resolvendo o sistema:
			valorConstantes = solve([formaNatural -y0,ylinhaNat -dy0])
			#print type(valorConstantes)
			#print "Constantes C1 e C2: ",valorConstantes
			### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
			nC1 = valorConstantes[C1]
			nC2	= valorConstantes[C2]
			#print "Valor de C1 e C2:",nC1,nC2

			respNatural = fN.subs([(C1,nC1),(C2,nC2)]).evalf(prec)

			##Tenta resolver parâmetros não terminados, se possível
			try:
				respNatural = solve(respNatural)
			except:
				pass

			print "Resposta Natural:"
			pprint(respNatural)





		#Ordem 3
		elif ((a5 == 0) and (a4 == 0)):
			y0 = input("y(0): ")
			dy0 = input("y'(0): ")
			d2y0 = input("y''(0): ")


			##Primeiramente a resposta Natural
			##Solucao geral é : formaNat
			#antes de aplicar as conds iniciais é necessário ter y''(t) y'(t) e y(t) da resp natural

			#Forma natural é derivada a primeira e à segunda
			y2linhaNat = sympify(fN.diff(t,2), rational = False, evaluate = False).evalf(prec)
			ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
			formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
			#print"yLinhaNat:", ylinhaNat

			## Agora é necessário resolver o sistema:
			#  ynat(t) = y(0)
			#  ynat'(0)= y'(0)
			# ynat''(0) = y''(0)
			#print "Valor das constantes com t",valorConstantes
			### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
			y2linhaNat   = y2linhaNat.subs(t,0)
			ylinhaNat    = ylinhaNat.subs(t,0)
			formaNatural = formaNatural.subs(t,0)

			#print "YlinhaNat em t = 0: ",ylinhaNat
			#print "Forma Natural em t = 0: ",formaNatural
			##Resolvendo o sistema:
			valorConstantes = solve([formaNatural -y0,ylinhaNat -dy0,y2linhaNat-d2y0])
			#print type(valorConstantes)
			#print "Constantes C1  C2 e C3: ",valorConstantes
			### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
			nC1 = valorConstantes[C1]
			nC2	= valorConstantes[C2]
			nC3 = valorConstantes[C3]
			#print "Valor de C1 e C2:",nC1,nC2

			respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3)]).evalf(prec)

			##Tenta resolver parâmetros não terminados, se possível
			try:
				respNatural = solve(respNatural)
			except:
				pass

			print "Resposta Natural:"
			pprint(respNatural)






		#Ordem 4
		elif ((a5 == 0)):
			y0 = input("y(0): ")
			dy0 = input("y'(0): ")
			d2y0 = input("y''(0): ")
			d3y0 = input("y'''(0): ")


			##Primeiramente a resposta Natural
			##Solucao geral é : formaNat
			#antes de aplicar as conds iniciais é necessário ter  y'''(t) y''(t) y'(t) e y(t) da resp natural

			#Forma natural é derivada a primeira , segunda e terceira
			y3linhaNat = sympify(fN.diff(t,3), rational = False, evaluate = False).evalf(prec)
			y2linhaNat = sympify(fN.diff(t,2), rational = False, evaluate = False).evalf(prec)
			ylinhaNat = sympify(fN.diff(t), rational = False, evaluate = False).evalf(prec)
			formaNatural  = sympify(fN, rational = False,evaluate= False).evalf(prec)
			#print"yLinhaNat:", ylinhaNat

			## Agora é necessário resolver o sistema:
			#  ynat(t) = y(0)
			#  ynat'(0)= y'(0)
			# ynat''(0) = y''(0)
			#print "Valor das constantes com t",valorConstantes
			### Agora com os valores em t = 0  para y'(t)  e y(t), substituindo:
			y3linhaNat   = y3linhaNat.subs(t,0)
			y2linhaNat   = y2linhaNat.subs(t,0)
			ylinhaNat    = ylinhaNat.subs(t,0)
			formaNatural = formaNatural.subs(t,0)

			#print "YlinhaNat em t = 0: ",ylinhaNat
			#print "Forma Natural em t = 0: ",formaNatural
			##Resolvendo o sistema:
			valorConstantes = solve([formaNatural -y0, ylinhaNat -dy0 , y2linhaNat-d2y0 , y3linhaNat-d3y0])
			print type(valorConstantes)
			#print "Constantes C1  C2 e C3: ",valorConstantes
			### Agora a resposta natural com as constantes encontradase aplicadas na funcão natural:
			nC1 = valorConstantes[C1]
			nC2	= valorConstantes[C2]
			nC3 = valorConstantes[C3]
			nC4 = valorConstantes[C4]
			#print "Valor de C1 e C2:",nC1,nC2

			respNatural = fN.subs([(C1,nC1),(C2,nC2),(C3,nC3),(C4,nC4)]).evalf(prec)

			print "Resposta Natural:"
			pprint(respNatural)

		#Ordem 5
		else:
			y0 = input("y(0): ")
			dy0 = input("y'(0): ")
			d2y0 = input("y''(0): ")
			d3y0 = input("y'''(0): ")
			d4y0 = input("y''''(0): ")






		#print "Valor das constantes com t = 0",valorConstantesT0


	conds_iniciais_aplicadas()









    
