import easygui

# Pergunta inicial com botões customizados
opcao = easygui.buttonbox(
    msg="Qual a sua sobremesa favorita?",
    title="Cardápio de Doces",
    choices=["Bolo de Paçoca", "Bolo Tradicional", "Paçoca Purinha", "Outro"]
)

# Resposta baseada na escolha do usuário
if opcao == "Bolo de Paçoca":
    easygui.msgbox("A combinação perfeita! O melhor de dois mundos. 🍰🥜", "Excelente escolha!")
elif opcao == "Bolo Tradicional":
    easygui.msgbox("Um clássico! Vai super bem com um café fresquinho.", "Gosto Tradicional")
elif opcao == "Paçoca Purinha":
    easygui.msgbox("Doce de amendoim raiz! Cuidado para não se engasgar com o farelo. 🥜", "Raiz!")
else:
    easygui.msgbox("Sem problemas! Mais bolo de paçoca para nós. 😉", "Saindo da rotina")