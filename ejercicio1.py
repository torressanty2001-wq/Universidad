#BIBLIOTECA
class libros ():
    def __init__ (lib,titulo,autor,numeroDePaginas):
        lib.titulo = titulo
        lib.autor = autor
        lib.numeroDePaginas = numeroDePaginas

    def infolibro(lib):
        return f"esta es la informacion del libro {lib.titulo},{lib.autor}, {lib.numeroDePaginas} "
    
    def numerPaginas(lib):
        lib.numeroDePaginas += 1
        return f"estas en la pagina {lib.numeroDePaginas}"  
    
Libro1 = libros("el principito",  "antonie" , 54)

print(Libro1.infolibro())
print(Libro1.numerPaginas())      