import flet as ft
import time
import random

def main(page: ft.Page):
    page.title = "PROTOCOLO MEGA // LABORATÓRIO POKÉMON"
    page.bgcolor = "#0B132B"
    page.window.width = 850
    page.window.height = 750
    page.theme_mode = ft.ThemeMode.DARK

    banner = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.AUTO_AWESOME, color="#FFD700", size=30),
            ft.Column([
                ft.Text("SISTEMA DE MEGA EVOLUÇÃO ATIVO", color="#FFD700", weight=ft.FontWeight.BOLD, size=15),
                ft.Text("Acesso autorizado apenas para Pesquisadores Pokémon e Líderes de Ginásio", color="#A5C4D4", size=11),
            ], spacing=2),
        ]),
        bgcolor="#1C2541",
        border=ft.Border.all(1, "#FFD700"),
        padding=15,
        border_radius=8,
    )

    scientist_select = ft.Dropdown(
        label="Selecione seu Pesquisador",
        options=[
            ft.DropdownOption("Professor Carvalho (Kanto)"),
            ft.DropdownOption("Professora Sycamore (Kalos)"),
            ft.DropdownOption("Professor Birch (Hoenn)"),
            ft.DropdownOption("Cynthia (Campeã de Sinnoh)"),
            ft.DropdownOption("Red (O Campeão)"),
        ],
        value="Professor Carvalho (Kanto)",
        border_color="#48CAE4",
    )

    password_input = ft.TextField(
        label="Chave da Mega Pedra (Dica: MEGA)",
        password=True,
        can_reveal_password=True,
        border_color="#48CAE4",
    )

    status_text = ft.Text("", color="#EF233C", size=14)
    progress_bar = ft.ProgressBar(width=400, value=0, visible=False, color="#48CAE4")
    log_box = ft.Text(
        value="[SYSTEM READY] Aguardando ressonância da Mega Ring...",
        color="#48CAE4",
        font_family="Courier New",
    )

    def login_click(e):
        if password_input.value and password_input.value.upper() == "MEGA":
            show_dashboard(scientist_select.value)
        else:
            status_text.value = "❌ CHAVE INCORRETA! A Equipe Rocket interceptou sua tentativa."
            page.update()

    login_view = ft.Container(
        content=ft.Column([
            ft.Text("⚡ SINCRONIZAÇÃO DA MEGA RING", size=20, color="#48CAE4", weight=ft.FontWeight.BOLD),
            scientist_select,
            password_input,
            status_text,
            ft.Button(
                content=ft.Text(" ATIVAR MEGA EVOLUÇÃO "),
                bgcolor="#48CAE4",
                color="#0B132B",
                on_click=login_click,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=5)),
            ),
        ], spacing=20),
        padding=25,
        border=ft.Border.all(1, "#48CAE4"),
        border_radius=10,
        bgcolor="#1C2541",
    )

    def trigger_mega_evolution(e):
        progress_bar.visible = True
        log_box.value = "[!] Canalizando energia bio-energética da Mega Pedra..."
        page.update()
        for i in range(1, 101):
            progress_bar.value = i / 100
            time.sleep(0.02)
            page.update()
        log_box.value = f"💥 [EVOLUÇÃO CONCLUÍDA] Mega Evolução bem-sucedida!\n[STATUS] Pokémon excedeu o limite máximo de poder | HASH: 0x{random.randint(100000, 999999)}"
        progress_bar.visible = False
        page.update()

    def legendary_alert(e):
        log_box.value = "[ALERTA] Energia de Pokémon Lendário detectada na rota! O clima mudou drasticamente."
        page.update()

    def show_dashboard(operator):
        page.clean()
        tab_mega = ft.Container(
            content=ft.Column([
                ft.Text("Câmara de Mega Evolução", size=16, color="#48CAE4"),
                ft.Dropdown(
                    label="Escolha o Pokémon",
                    options=[
                        ft.DropdownOption("Mega Charizard X / Y"),
                        ft.DropdownOption("Mega Mewtwo Y"),
                        ft.DropdownOption("Mega Rayquaza"),
                        ft.DropdownOption("Mega Lucario"),
                        ft.DropdownOption("Mega Gengar"),
                    ],
                    value="Mega Charizard X / Y",
                    border_color="#FFD700",
                ),
                ft.Button(
                    content=ft.Text("LIBERAR ENERGIA MEGA"),
                    bgcolor="#FFD700",
                    color="#0B132B",
                    on_click=trigger_mega_evolution,
                ),
            ], spacing=15),
            padding=20,
        )

        tab_wild = ft.Container(
            content=ft.Column([
                ft.Text("Radar de Anomalias", size=16, color="#48CAE4"),
                ft.Button(
                    content=ft.Text("RAREADOR DE LENDÁRIOS"),
                    bgcolor="#48CAE4",
                    color="#0B132B",
                    on_click=legendary_alert,
                ),
            ], spacing=15),
            padding=20,
        )

        page.add(
            banner,
            ft.Text(f"👤 Pesquisador Conectado: {operator}", size=16, color="#FFD700", weight=ft.FontWeight.BOLD),
            ft.Divider(color="#48CAE4"),
            ft.Tabs(
                selected_index=0,
                animation_duration=300,
                expand=True,
                tabs=[
                    ft.Tab(label="MEGA EVOLUÇÃO", icon=ft.Icons.FLASH_ON, content=tab_mega),
                    ft.Tab(label="RADAR POKÉMON", icon=ft.Icons.AUTO_AWESOME, content=tab_wild),
                ],
            ),
            ft.Divider(color="#48CAE4"),
            ft.Text("CONSOLE DE LOGS DO LABORATÓRIO:", color="#FFD700", size=11),
            progress_bar,
            ft.Container(
                content=log_box,
                bgcolor="#0B132B",
                padding=15,
                border_radius=5,
                border=ft.Border.all(1, "#48CAE4"),
            ),
        )
        page.update()

    page.add(banner, login_view)

if __name__ == "__main__":
    ft.run(main)
