def  evaluate_roots(roots):

        print "Metodo Evaluate Roots"

        print roots,len(roots)

        RaizesC = [0]*len(roots)
        RaizesR = [0]*len(roots)
        output  = [0]*len(roots)

        for i in range(len(roots)):

                print "for loop",i

                RaizesC[i] = im(roots[i])
                RaizesR[i] = re(roots[i])
                print RaizesR[i]
                print RaizesC[i]

                if RaizesC[i] != 0 and RaizesR[i] != 0:

                        if RaizesC[i] < (1.0/100)*RaizesR[i]:
                                print "Parte complexa ignorada"

                                output[i] = complex(RaizesR[i],0)


                        elif RaizesR[i] < (1.0/100)*RaizesC[i]:
                                print "Parte real ignorada"

                                output[i] = complex(0,RaizesC[i])
         
 
                else:
                        print "Only output"
                        output[i] = complex(RaizesR[i],RaizesC[i])

        print "Raizes ---:",output
        return output
