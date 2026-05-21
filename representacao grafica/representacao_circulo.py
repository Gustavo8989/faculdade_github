def desenhado(f,c,r,g):
    (xc,yc) = c 
    x,y,dx,dy,e = 0,r,1,2*r-1,0 
    while (x < y):
        f[yc+y,xc+x] = g
        x +=1
        e+=dx
        dx+=2
        if dy < 2*e:
            y -=1
            e=dy
            dy=2
