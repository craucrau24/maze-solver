class Text:
    def __init__(self, text, pos):
        self._text = text
        self._pos = pos

    def draw(self, canvas, font=None, color="black", anchor="center"):
        args = {
            "fill": color,
            "anchor": anchor
        }

        if font is not None:
            args["font"] = font

        print(f"text: {self._text} at {self._pos} with options: {args}")
        canvas.create_text(self._pos.x, self._pos.y, text=self._text, **args)