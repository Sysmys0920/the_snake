# Тут опишите все классы игры.
class GameObject:
    """
    Базовый класс, от которого наследуются все объекты.
    Содержит общие атрибуты: позиция и цвет.
    """

    def __init__(self, position=None, body_color=None):
        """
        Конструктор базового игрового объекта.
        Аргументы: position (координаты), body_color (цвет).
        """
        if position is None:
            self.position = (320, 240)
        else:
            self.position = position

    def draw(self, surface):
        """
        Абстрактный метод для отрисовки объекта на экране.
        Аргумент: surface (поверхность, на которой рисуем)
        """
        pass

class Apple(GameObject):
    """
    Класс Apple. Наследуется от GameObject.
    Появляется в случайном месте поля.
    """
    apple_color = (255, 0, 0)

    super().__init__(position=None, body_color=apple_color)

    self.radomize_position()

    def randomize_position(self):
        """
        Устанавливает случайные координаты для яблока.
        """
        max_x = 640 - 20
        max_y = 480 - 20

        x.random.randrange(0, max_x + 1, 20)
        y.random.randrange(0, max_y + 1, 20)

        self.position = (x, y)

    def draw(self, surface):
        """
        Отрисовывает яблоко на игровом поле.
        """

        rect = pygame.Rect(
            self.position[0],
            self.position[1],
            20,
            20
        )

        pygame.draw.rect(surface, self.body_color, rect)
