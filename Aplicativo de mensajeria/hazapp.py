import flet as ft
#mport datatime
# posicionar texto en el aplicativo crear lineas y columnas en el aplicativo
#


def main(pagina):
    texto = ft.Text("Holaaa")  # item.oqueeuqerofacer(parametros)
    pagina.add(texto)
    chat = ft.Column()
    nome_usuario = ft.TextField(label="Escriba su nombre:")
    campo_mensagem = ft.TextField(label="Escriba sua mensagem")

    def enviarmensagem(evento):
        texto_campoMensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        chat.controls.append(ft.Text(texto_campoMensagem))
        campo_mensagem = "" #limpiando el campo de mensaje
        pagina.update()

   
    enviar_mensagem = ft.ElevatedButton("enviar", on_click=enviarmensagem) #on_submit  (nome da funcao)

    def entrar_nochat(evento):
        popup.open = False
        pagina.remove(btninitial)

        print(nome_usuario)

        linha_mensagem = ft.Row([
            campo_mensagem, enviar_mensagem
        ])

        Mostramensagem = ft.Row([
            chat
        ])
        
        pagina.add(Mostramensagem)
        pagina.add(linha_mensagem)
        pagina.update()

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=ft.Text("Bem-vindo Hazapp"),
        content=nome_usuario,
        # siempre definir la funcion detas de la lina de codigo de llamada para respetar ese orden
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_nochat)]
    )  # modal=True estos son los modelos del popup

    def iniciar_chat(evento):  # esto para saber que cunado se cliqueo se genero un evento
        pagina.dialog = popup
        popup.open = True  # esto es una ventana de aviso
        pagina.update()  # siemore despues de editar la pagina dentro de una funcion damos el update
    # on_click= eso es para cuando de un click haga
    btninitial = ft.ElevatedButton("iniciar chat", on_click=iniciar_chat)
    # ft.Image para imagenes

    pagina.add(btninitial)

    pass


ft.app(main)  # view = ft.WEB_BROWSER crear un cite sem nada e no formato aplicativo
