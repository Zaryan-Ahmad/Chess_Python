class Player:

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.color})"