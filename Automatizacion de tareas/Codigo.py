# escribir mano a mano cada una de las partes del proyecto. anotacoes

# entrar no sistema da empresa e fazer o cadastro automatico da empresa e fazer um cadastro automatico.
# aprender o que sao os automaticacoes do sistema

# 1--entrar no sistema da empresa

# 2--fazer o login na pagina

# 3-- importar o banco de datos

# 4-- cadastrar cadda umo dos dados

# 5-- Repetir isso ate finalizar o cadastro de tudos os dados.


# automatizar maus tela e teclado

# instalacion de tres librerias al mismo tiempo pip install pandas numpy openpyxl
import pandas
import pyautogui
import time

pyautogui.PAUSE = 1  # este tiene mas comandos esperar un segundo para cada una de las acciones, esto tambien con el fin de que se ejecute todo sin problemas

pyautogui.press("win")  # pulsar la tecla de windows.
pyautogui.write("brave")
pyautogui.press("enter")  # \" eso es para identificar el texto


# crear variables para links o otras acciones que generen problemas
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)


time.sleep(2)  # diferencia de 5 segundos en este lugar especifico
pyautogui.press("enter")

time.sleep(2)
# poblemas con problemas de resolucion este tiene mas configuraciones segun las necesidades
pyautogui.click(x=1045, y=456)

pyautogui.write("nocua68@gmail.com")


pyautogui.press("tab")
pyautogui.write("dgdfgdfggdfgdfgdg")
pyautogui.press("tab")
pyautogui.press("enter")
# recomendable explicar cada uno de los procesos que esta pasando


time.sleep(1)

# ingreso de bases de datos


# abrir cada tipo de archivo tiene que estar en la misma pagina de nuestro codigo
tabela = pandas.read_csv("produtos.csv")
print(tabela)  # muestra por consola en la base sde datos

for linha in tabela.index:  # en cada linia de mi tabla hacer -- index para saber el tamaño de la tabla para cada item dentro de un conjunto de items
    pyautogui.PAUSE = 0.05
    # index linhas colums colums
    pyautogui.click(x=1101, y=298)
    
    #
    codigo= tabela.loc[linha,"codigo"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(codigo)
    #
    pyautogui.press("tab")
    marca= tabela.loc[linha,"marca"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(marca)
    #
    pyautogui.press("tab")
    tipo= tabela.loc[linha,"tipo"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(tipo)
    #
    pyautogui.press("tab")
    categoria= (tabela.loc[linha,"categoria"]) # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(str(categoria)) #concatenacion de valores enteros a string


    #
    pyautogui.press("tab")
    preco_unitario= tabela.loc[linha,"preco_unitario"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(str(preco_unitario))

    #
    pyautogui.press("tab")
    custo= tabela.loc[linha,"custo"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(str(custo))

    #
    pyautogui.press("tab")
    obs= tabela.loc[linha,"obs"] # para cada uno de estos pasos se tiene qyue escribirl el nombre de la columna recipera el valor que esta en la linha tal con la columna codigo
    pyautogui.write(str(obs))

    #
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.PAUSE = 0.5
    # numeros positivos para encuima ty negativos para abajo
    pyautogui.scroll(1000)
    # enviar el producto
