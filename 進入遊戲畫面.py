在class snake加上一行：self.game_started = False

在run_game的最上面加上
welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
tips_font = pygame.font.SysFont('arial', 24)
start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
while 1:
    screen.blit(welcome_words, (188, 100))
    screen.blit(start_game_words, (236, 310))
    screen.blit(close_game_words, (233, 350))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == 27:
                exit()
        elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 300 <= x <= 500 and 300 <= y <= 500:
                snake.game_started = True
