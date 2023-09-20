from Classes.InteractiveObject.interactiveObject import InteractiveObject

class Button(InteractiveObject):
    def __init__(self, x, y, sprite_image):
        super().__init__(self, x, y, sprite_image)
        self.activate = False

    def interact(self):
        pass