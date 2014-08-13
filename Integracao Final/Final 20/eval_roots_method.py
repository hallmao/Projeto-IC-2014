
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

                        ratio  = 0

                        ratio = abs(RaizesC[i]/RaizesR[i])
                        flagRatio = False


                        print "Ratio: ",ratio

                        
                        if ratio <  (1.0/100):
                                print "Parte complexa ignorada"

                                output[i] = complex(RaizesR[i],0)


                        elif ratio > 100:
                                print "Parte real ignorada"

                                output[i] = complex(0,RaizesC[i])
                        else:
                                print "Only output"
                                output[i] = complex(RaizesR[i],RaizesC[i])
                                
         
 
                else:
                        print "Only output"
                        output[i] = complex(RaizesR[i],RaizesC[i])

        print "Raizes ---:",output
        return output
