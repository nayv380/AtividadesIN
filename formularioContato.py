import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20
    page.spacing = 10

    def enviar_formulario(e):
        nome_val = campo_nome.value.strip()
        email_val = campo_email.value.strip()
        mensagem_val = campo_mensagem.value.strip()

        if nome_val == "" or email_val == "" or mensagem_val == "":
            status.value = "Preencha todos os campos!"
            status.color = ft.colors.RED
        else:
            status.value = f"Formulário enviado com sucesso!\nNome: {nome_val}\nEmail: {email_val}\nMensagem: {mensagem_val}"
            status.color = ft.colors.GREEN
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
        page.update()

    campo_nome = ft.TextField(label="Nome", width=300)
    campo_email = ft.TextField(label="Email", width=300)
    campo_mensagem = ft.TextField(label="Mensagem", width=300, multiline=True, min_lines=3, max_lines=5)
    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)
    status = ft.Text(value="", size=16)

    page.add(
        ft.Text("Formulário de Contato", size=25, weight="bold"),
        campo_nome,
        campo_email,
        campo_mensagem,
        botao_enviar,
        status
    )

ft.app(target=main)
