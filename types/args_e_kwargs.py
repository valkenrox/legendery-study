def cal_imposto(valor):
    
    ir = valor * 0.27
    iss = valor * 0.05
    csll = valor * 0.0375
    pis = valor * 0.008

   
    
     
    return ir + iss + csll + pis


print(cal_imposto(1000.0))


