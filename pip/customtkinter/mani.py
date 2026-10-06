import customtkinter as ctk
import time
import random

# Configurações globais do tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class DinosaurLabApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("SISTEMA DE CONTENÇÃO JURÁSSICA // INGEN LABS v6.0")
        self.geometry("850x700")
        self.resizable(False, False)

        # --- CABEÇALHO / BANNER DE ALERTA ---
        self.banner = ctk.CTkFrame(self, fg_color="#1E291B", border_color="#EAB308", border_width=2, corner_radius=8)
        self.banner.pack(fill="x", padx=20, pady=(20, 10))

        self.lbl_warning_title = ctk.CTkLabel(
            self.banner, 
            text="⚠️ ALERTA DE NÍVEL DE SEGURANÇA 4", 
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#EAB308"
        )
        self.lbl_warning_title.pack(anchor="w", padx=15, pady=(10, 2))

        self.lbl_warning_sub = ctk.CTkLabel(
            self.banner, 
            text="Acesso restrito ao pessoal autorizado da InGen. Monitoramento de cercas ativado.", 
            font=ctk.CTkFont(size=12),
            text_color="#A3E635"
        )
        self.lbl_warning_sub.pack(anchor="w", padx=15, pady=(0, 10))

        # --- PAINEL PRINCIPAL (LOGIN DE ACESSO) ---
        self.main_frame = ctk.CTkFrame(self, fg_color="#111827", border_color="#22C55E", border_width=1, corner_radius=10)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.lbl_auth = ctk.CTkLabel(
            self.main_frame, 
            text="🦖 AUTENTICAÇÃO DO OPERADOR", 
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="#4ADE80"
        )
        self.lbl_auth.pack(pady=(20, 15))

        # Seleção do Dinossauro/Setor
        self.dino_select = ctk.CTkOptionMenu(
            self.main_frame,
            values=[
                "Tyrannosaurus Rex (Padoque 01)",
                "Velociraptor (Unidade Alpha)",
                "Indominus Rex (Padoque de Alta Contenção)",
                "Dilophosaurus (Setor Norte)",
                "Spinosaurus (Zona B)"
            ],
            button_color="#166534",
            button_hover_color="#15803D",
            dropdown_hover_color="#166534",
            width=350
        )
        self.dino_select.pack(pady=10)

        # Chave de Acesso
        self.entry_key = ctk.CTkEntry(
            self.main_frame, 
            placeholder_text="Chave de Acesso (Dica: JURASSIC)", 
            show="*",
            width=350,
            border_color="#15803D"
        )
        self.entry_key.pack(pady=10)

        # Status
        self.lbl_status = ctk.CTkLabel(self.main_frame, text="", text_color="#EF4444", font=ctk.CTkFont(size=13))
        self.lbl_status.pack(pady=5)

        # Botão de Login
        self.btn_login = ctk.CTkButton(
            self.main_frame,
            text="ACESSAR PAINEL DE CONTENÇÃO",
            font=ctk.CTkFont(weight="bold"),
            fg_color="#15803D",
            hover_color="#166534",
            command=self.verify_access
        )
        self.btn_login.pack(pady=15)

        # --- ÁREA DE DASHBOARD (INICIALMENTE OCULTA