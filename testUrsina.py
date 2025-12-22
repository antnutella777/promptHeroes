from ursina import *

app = Ursina()

window.size = (800, 450)
window.color = color.black
window.title = 'Terminal'

# Fundo ocupando a tela inteira
bg = Entity(
    parent=camera.ui,
    model='quad',
    scale=(2, 1),
    color=color.black
)

# Prompt no canto superior esquerdo
prompt = InputField(
    text='>>>>',
    parent=camera.ui,
    origin=(-0.5, 0.5),
    position=(-0.88, 0.45),
    scale=2,
    color=color.white,
    z=-1
)

app.run()
