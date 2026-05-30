from PIL import Image
import numpy as np
import cairo
import math



# CRIAÇÃO DE IMAGEM VETORIAL COM RETAS E CÍRCULOS E TRANSFORMAÇÃO EM IMAGEM MATRICIAL

nome_arquivo = "img.svg"
altura,largura = 200,200


def criandoImgVetorial():
    with cairo.SVGSurface(nome_arquivo,largura,altura) as v:
        contexto = cairo.Context(v)
        contexto.scale(largura,altura)
        contexto.set_line_width(0.01)
        contexto.set_source_rgb(1,1,1)
        contexto.paint()
        # Preta
        contexto.set_source_rgb(0,0,0)
        contexto.move_to(0.2,0.3)
        contexto.line_to(0.8,0.7)
        contexto.stroke()
        #Cinza
        contexto.set_source_rgb(0.41,0.41,0.41)
        contexto.move_to(0.8,0.3)
        contexto.line_to(0.2,0.7)
        contexto.stroke()
        #circulo
        contexto.set_source_rgb(0.75,0.75,0.75)
        contexto.arc(0.5,0.5,0.3,0,2*math.pi)
        contexto.stroke()
        return v
    


f = np.zeros((201,201,4),dtype=np.uint8)

def desenhaCirculo(f,c,r,g):
    surface = cairo.ImageSurface.create_for_data(
        f,
        cairo.FORMAT_ARGB32,
        201,
        201)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1,1,1)
    ctx.paint()
    ctx.arc(c,c,r,0,2*math.pi)
    ctx.set_source_rgb(g/255,g/255,g/255)
    ctx.stroke()

    surface.write_to_png("img.png")


def desenhaReta(f, p, q, g):
    x1, y1 = p
    x2, y2 = q
    dx = x2 - x1
    dy = y2 - y1

    passos = max(abs(dx), abs(dy))

    if passos == 0:
        f[y1, x1] = g
        return

    x_inc = dx / passos
    y_inc = dy / passos

    x = x1
    y = y1

    for _ in range(passos + 1):
        f[round(y), round(x)] = g
        x += x_inc
        y += y_inc


def desenhaCirculo(f, c, r, g):
    altura, largura = f.shape

    for y in range(altura):
        for x in range(largura):
            d = math.sqrt((x - c[0])**2 + (y - c[1])**2)

            if abs(d - r) < 0.5:
                f[y, x] = g

f = np.full((201, 201), 255, dtype=np.uint8)

largura = 201
altura = 201

p1 = (round(0.2 * largura), round(0.3 * altura))
q1 = (round(0.8 * largura), round(0.7 * altura))
desenhaReta(f, p1, q1, 0)

p2 = (round(0.8 * largura), round(0.3 * altura))
q2 = (round(0.2 * largura), round(0.7 * altura))
desenhaReta(f, p2, q2, 105)

centro = (round(0.5 * largura), round(0.5 * altura))
raio = round(0.3 * largura)

desenhaCirculo(f, centro, raio, 192)
Image.fromarray(f).save("figura.png")




'''def criando_reta():
    linha = 400 
    teste = cairo.ImageSurface(cairo.FORMAT_ARGB32, linha, linha)
    ctx = cairo.Context(teste)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    ctx.set_source_rgb(0,255,0)
    ctx.set_line_width(5)
    ctx.move_to(50,50)
    ctx.line_to(350,350)
    ctx.stroke()
    teste.write_to_png("teste.png")'''