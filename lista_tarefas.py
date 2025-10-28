
import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Lista de tarefas que será exibida na tela
    lista_tarefas = ft.Column()

    # Função para adicionar uma nova tarefa
    def adicionar_tarefa(e):
        tarefa = campo_tarefa.value.strip()
        if tarefa != "":
            lista_tarefas.controls.append(ft.Text(tarefa))
            campo_tarefa.value = ""
            page.update()

    # Campo de entrada de texto para digitar a tarefa
    campo_tarefa = ft.TextField(
        label="Digite uma nova tarefa",
        width=300
    )

    # Botão para adicionar a tarefa
    botao_adicionar = ft.ElevatedButton(
        text="Adicionar",
        on_click=adicionar_tarefa
    )

    # Adiciona os componentes à página
    page.add(
        ft.Text("Lista de Tarefas", size=25, weight="bold"),
        ft.Row([campo_tarefa, botao_adicionar]),
        lista_tarefas
    )

# Executa o aplicativo
ft.app(target=main)
