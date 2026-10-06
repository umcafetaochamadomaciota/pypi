import gradio as gr

def goodra_hug(trainer_name, intensity):
    return f"🐌 Goodra deu um abraço muito gosmento em {trainer_name}" + "!" * int(intensity)

demo = gr.Interface(
    fn=goodra_hug,
    inputs=[
        gr.Textbox(label="Nome do Treinador", placeholder="Digite seu nome..."),
        gr.Slider(minimum=1, maximum=10, step=1, value=3, label="Nível de Afeto do Goodra")
    ],
    outputs=[
        gr.Textbox(label="Resultado do Abraço")
    ],
    title="🐉 Abraço do Goodra",
    description="Escolha a intensidade e receba um carinho pegajoso do Goodra!",
    api_name="predict"
)

demo.launch()