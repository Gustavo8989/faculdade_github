import cairo 

v = cairo.SVGSurface("cgpiU1S2.svg",201,201)

# Criação da rete

def reta(f,p,q,g):
    (yp,xp) = p 
    (yq,xq) = q 
    s = float(yq - yp) / (xq,xp)
    for x in range(xp,xq+1):
        y = round(yp + s(x-xp))
        f[x,y] = g 
