# 💻 Conversor de Binário para Decimal

## 📖 Descrição

Após ter terminado a [trilha do conhecimento sobre Python](https://www.ev.org.br/trilhas-de-conhecimento/linguagem-de-programacao-python) na plataforma da [Fundação Bradesco](https://www.ev.org.br/), decidi me aprofundar um pouco mais em Kivy e construir um pequeno projeto.

Além do projeto, pensei em documentar meu progresso para servir de consulta ou para ajudar alguém que esteja lendo e possa tirar alguma dúvida. Ele foi desenvolvido no Windows, mas lendo a documentação oficial é possível executar em outros sistemas sem muita dificuldade.

O design da tela foi feito por mim, utilizei o site [coolors.co](https://coolors.co/) para a paleta de cores.

## 🛠️ Ferramentas

- Linguagem Python (versão 3)
- Biblioteca gráfica Kivy
- Ambiente virtual Python (venv)

## 🗂️ Setup (Windows)

Crie um ambiente virtual:

```bash
py -m venv venv/
```

Ative o ambiente:

```bash
source venv/Scripts/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## 📝 Anotações

### Ambiente Virtual

Criação de um ambiente virtual para acomodar todas as dependências em um ambiente isolado, sem mexer com os arquivos globais. Isso evita possíveis conflitos entre diferentes versões de bibliotecas instaladas:

```bash
py -m venv venv/
```

Após criar o ambiente virtual, é necessário ativá-lo. Para isso, utilizei o próprio terminal do Git (bash) e executei o seguinte comando:

```bash
source venv/Scripts/activate
```

Caso queira desativar o ambiente virtual, simplesmente rode o seguinte comando (não é necessário navegar até a pasta Scripts):

```bash
deactivate
```

### Instalação do Kivy

Após deixar o ambiente virtual pronto, instalei o mínimo necessário do Kivy seguindo a [documentação oficial](https://kivy.org/doc/stable/gettingstarted/installation.html):

```bash
pip install "kivy[base]"
```

### Requisitos das Dependências

Caso alguém queira baixar o projeto, seria necessário instalar todas as dependências manualmente. Para facilitar a vida de quem abrir o projeto, basta usar o comando `pip freeze` para listar todas as dependências e salve em um arquivo (geralmente) chamado `requirements.txt`:

```bash
pip freeze > requirements.txt
```

Em uma nova instância do projeto, instale as dependências de `requirements` da seguinte forma:

```bash
pip install -r requirements.txt
```

**Obs**.: se não quiser bagunçar suas bibliotecas locais, ative o ambiente virtual!

### Coordenadas no Kivy

Ao contrário de muitas linguagens de programação, onde `x: 0` e `y: 0` começam no topo esquerdo, em Kivy, `0` significa irá ser deslocado para a direita ou para baixo do layout, de acordo com a coordenada especificada.

As coordenadas recebem um valor decimal que pode ir de `0 (0%)` até `1 (100%)`. O elemento pode ser posicionado por meio da propriedade `pos_hint` que recebe um dicionário:

```py
# Alinha à direita no fundo do layout
pos_hint: {"x": 0, "y": 0}
```

```py
# Alinha à esquerda no topo do layout
pos_hint: {"x": 1, "y": 1}
```

É possível manipular as coordenadas a partir do centro do elemento com `center_x` e `center_y`:

```py
# Centraliza horizontalmente e verticalmente
pos_hint: {"center_x": 0.5, "center_y": 0.5}
```

### Arquivos `.kv`

Em um projeto Kivy, é possivel codificar tudo em arquivos `.py`, como mostra o código a seguir, declarado dentro do método `build`:

```py
class ConversorApp(App):
    def build(self):
        # Outros widgets...
        self.label = Label(
            bold=True,
            font_size=18,
            font_name="assets/fonts/raleway-v34-latin-700.ttf",
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            size_hint=(1, None),
            text="Efetue uma conversão"
)
```

Porém, isso pode tornar o código massivo, além de misturar a parte visual do Kivy com a funcionalidade da aplicação. Para contornar isso, existe a possibilidade de criar um arquivo `.kv` para conter apenas o conteúdo dos widgets, deixando o Python apenas para a parte funcional do app:

```py
<WindowLayout>
    # Outros widgets...
    Label:
        bold: True
        font_size: 18
        font_name: "assets/fonts/raleway-v34-latin-700.ttf"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: (1, None)
        text: "Efetue uma conversão"
```

Sendo assim, o contexto do visual e da funcionalidade fica segregado, de modo que torna o código mais limpo e organizado.

## 🎬 Conclusão

Não vou mentir, eu tive dificuldades em entender a como posicionar as coisas e criar os widgets. Fiquei acordado até de madrugada batendo a cabeça pra entender, mas acabou saíndo 😅

Pensei que seria tão fácil quanto trabalhar com CSS, mas achei a curva de aprendizado maior, e ainda há muito o que aprender.

Com esse pequeno projeto, pude me aprofundar mais em Python e na biblioteca gráfica Kivy. Além disso, aprendi a utilizar ambientes virtuais, instalar dependências de uma forma mais limpa e facilitar a instalação das mesmas em outras máquinas.

Se você gostou do projeto ou te ajudei a tirar alguma dúvida com relação ao Kivy, seria de muito agrado se desse uma estrela nesse repositório ✨

## 📎 Links

- [kivy.org](https://kivy.org/doc/stable/)
- [python.org](https://www.python.org/downloads/)
- [Installation (Kivy)](https://kivy.org/doc/stable/gettingstarted/installation.html)
- [Decimal to Binary](https://www.cuemath.com/numbers/decimal-to-binary/)
- [Git and Virtual Environments: A Guide for Python Developers](https://iifx.dev/en/articles/31110340)
