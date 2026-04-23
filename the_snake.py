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
        # Продолжение метода draw для класса Apple (с 90-й строки)
        rect = pygame.Rect(self.position, (20, 20))
        pygame.draw.rect(surface, self.apple_color, rect)
        pygame.draw.rect(surface, (93, 216, 228), rect, 1)

class Snake(GameObject):
    """
    Класс Snake. Наследуется от GameObject.
    Описывает поведение змейки.
    """
    def __init__(self):
        super().__init__(body_color=(0, 255, 0))
        self.length = 1
        self.positions = [(320, 240)]
        self.direction = (20, 0)
        self.next_direction = None
        self.last = None

    def update_direction(self):
        """Метод обновления направления после нажатия клавиши."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        """Метод движения змейки."""
        cur = self.get_head_position()
        x, y = self.direction
        new = (
            (cur[0] + x) % 640,
            (cur[1] + y) % 480
        )
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.last = self.positions.pop()

    def draw(self, surface):
        """Метод отрисовки змейки на экране."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (20, 20))
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, (93, 216, 228), rect, 1)

        # Отрисовка головы
        head_rect = pygame.Rect(self.positions[0], (20, 20))
        pygame.draw.rect(surface, self.body_color, head_rect)
        pygame.draw.rect(surface, (93, 216, 228), head_rect, 1)

    def get_head_position(self):
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self):
        """Сброс змейки в начальное состояние."""
        self.length = 1
        self.positions = [(320, 240)]
        self.direction = random.choice([(0, 20), (0, -20), (20, 0), (-20, 0)])

def handle_keys(game_object):
    """Функция обработки нажатий клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != (0, 20):
                game_object.next_direction = (0, -20)
            elif event.key == pygame.K_DOWN and game_object.direction != (0, -20):
                game_object.next_direction = (0, 20)
            elif event.key == pygame.K_LEFT and game_object.direction != (20, 0):
                game_object.next_direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and game_object.direction != (-20, 0):
                game_object.next_direction = (20, 0)

def main():
    """Основной цикл игры."""
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    snake = Snake()
    apple = Apple()

    while True:
        clock.tick(10)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        
        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()

        screen.fill((0, 0, 0))
        snake.draw(screen)
        apple.draw(screen)
        pygame.display.update()

if __name__ == '__main__':
    main()
