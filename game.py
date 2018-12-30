import pygame
import random


class Food:
    """食物類"""

    def __init__(self, screen,picture):
        """隨機初始化第一個食物的位置"""
        self.screen = screen

        # 載入食物圖片並獲取外接矩形 (pygame通過外接矩陣操作圖片)
        self.image = pygame.image.load(picture)
        # 獲得圖片外接矩陣
        self.rect = self.image.get_rect()

        # 隨機獲得圖片中心橫縱座標
        # （randint獲得10~490的int型別隨機數，包括10和490）
        # （rect.centerx為中心橫座標）
        self.rect.centerx = random.randint(20, 480)
        self.rect.centery = random.randint(20, 480)

    def reinit(self):
        """ 隨機獲得一個食物，並返回食物座標"""
        self.rect.centerx = random.randint(20, 480)
        self.rect.centery = random.randint(20, 480)
        return [self.rect.centerx, self.rect.centery]

    def position(self):
        """ 返回食物座標（中心點x,y）"""

        return [self.rect.centerx, self.rect.centery]

    def foodrect(self):
        """返回外接矩矩形"""

        return self.rect

    def blitme(self):
        """在指定位置繪製食物"""
        self.screen.blit(self.image, self.rect) #blit(image,要繪製的位置)



import pygame
#初始化移動狀態，使一開始向上移動
move_up = True
move_down = False
move_left = False
move_right = False
def check_events(snake):
    """響應按鍵和滑鼠事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        check_keydown_events(event)
    redirection(snake)
def check_keydown_events(event):
    """響應鍵盤按下"""
    #可修改全域性變數
    global move_up
    global move_down
    global move_left
    global move_right
    if event.type == pygame.KEYDOWN:
        # and move_down == False 及類似程式碼使蛇不可回頭
        if event.key == pygame.K_UP and move_down == False:
            #修改移動狀態
            move_up = True
            move_down = False
            move_left = False
            move_right = False
        if event.key == pygame.K_DOWN and move_up == False:
            move_up = False
            move_down = True
            move_left = False
            move_right = False
        if event.key == pygame.K_LEFT and move_right == False:
            move_up = False
            move_down = False
            move_left = True
            move_right = False
        if event.key == pygame.K_RIGHT and move_left == False:
            move_up = False
            move_down = False
            move_left = False
            move_right = True
def redirection(snake):
    global move_up
    global move_down
    global move_left
    global move_right
    #傳遞給蛇類的方向方法，使蛇頭方向變更
    if move_up:
        snake.direction('U')
    if move_down:
        snake.direction('D')
    if move_left:
        snake.direction('L')
    if move_right:
        snake.direction('R')



class Settings():
    """儲存遊戲所有設定的類"""

    def __init__(self):
        """初始化遊戲的設定"""
        # 設定螢幕大小
        self.screen_width = 500
        self.screen_height = 500
        # 設定螢幕背景色
        self.bg_color = [255, 255, 240]
        # 設定蛇移動速度（幀數）
        self.speed = 7
        # 設定蛇的顏色
        self.snake_color = [50, 0, 0]


import copy


class Snake:
    def __init__(self,screen):
        """初始化第一個點（蛇頭）的位置"""
        # 建立儲存每個點位置的列表，目前只有蛇頭
        self.screen = screen
        self.poslist = [[250, 250,25,25]]
        # 載身體圖片並獲取外接矩形
        self.headimage=pygame.image.load('./player3.png')
        self.bodyimage=pygame.image.load('./pokeball.png')

    def position(self):
        """return儲存連續點位置的列表"""

        return self.poslist

    def direction(self, new_direction):
        """控制蛇移動方向"""

        count = len(self.poslist) # 現在總共有幾節身體
        position = count - 1 #序數，由最後面開始往前掃

        # poslist[1]～[尾]（不含蛇頭）所有點移動向下一位置

        while position > 0: # 還沒掃到第一個 ＃全部更新一次poslist
            self.poslist[position] = copy.deepcopy(self.poslist[position - 1])
            position -= 1 # 第二個點移到原本第一個點的位置

        # 更新蛇頭（poslist[0]）位置，和“移動方向“有關
        if new_direction is 'U':
            self.poslist[0][1] -= 32
            # 設定可以穿牆
            if self.poslist[0][1] < 0:
                self.poslist[0][1] = 485
        if new_direction is 'D':
            self.poslist[0][1] += 32
            if self.poslist[0][1] > 485:
                self.poslist[0][1] = 0
        if new_direction is 'L':
            self.poslist[0][0] -= 32
            if self.poslist[0][0] < 0:
                self.poslist[0][0] = 485
        if new_direction is 'R':
            self.poslist[0][0] += 32
            if self.poslist[0][0] > 485:
                self.poslist[0][0] = 0

    def eatfood(self, foodrect): #蛇頭（poslist[0]）變吃掉食物的座標
        """吃掉食物並加入列表"""

        self.poslist.append(foodrect)

    def draw_snake(self, poslist):
        """畫蛇"""
        for i in range(len(poslist)):
            if i ==0:
                self.screen.blit(self.headimage, (poslist[i]))
            else:
                self.screen.blit(self.bodyimage,(poslist[i]))


# 匯入其他檔案的類、函式


def run_game():
    # 初始化pygame
    pygame.init()
    # 設定時鐘物件，控制幀數
    clock = pygame.time.Clock()
    # 一個Settings類例項，便於控制遊戲引數
    run_settings = Settings()
    # 遊戲視窗大小，引數為寬和高
    screen = pygame.display.set_mode((run_settings.screen_width,
                                      run_settings.screen_height))
    # 設定視窗名字
    pygame.display.set_caption("貪吃蛇")
    restart = True
    # 建立字型物件，繪製文字，返回surface。引數一：字型  引數二：字號
    socre_font = pygame.font.Font(None, 28)
    # 記錄分數
    score = 0
    # 是否重開
    food_image_list=['./1.png',
                     './2.png',
                     './3.png',
                     './4.png',
                     './5.png',
                     './6.png',
                     './7.png',
                     './8.png',
                     './9.png',
                     './10.png',
                     './11.png',
                     './12.png',
                     './13.png',
                     './14.png',
                     './15.png',
                     './16.png',
                     './17.png',
                     './18.png',
                     './19.png',
                     './20.png']
    while restart:
        # 類的例項
        snake = Snake(screen)
        food = Food(screen, food_image_list[0])
        running = True
        # 是否遊戲結束
        while running:
            # 視窗背景顏色，用引數RGB設定
            screen.fill(run_settings.bg_color)
            # 開始接收、響應鍵盤指令
            check_events(snake)
            # 控制迴圈幀數，引數為每秒幀數
            time_pass = clock.tick(run_settings.speed)
            # 接受食物圖片的外接矩形
            food_rect = food.foodrect()
            # 繪製這個食物
            food.blitme()
            # 繪製蛇
            poslist = snake.position()
            snake.draw_snake(poslist)
            head_rect = poslist[0]
            # 吃到食物
            if food_rect.colliderect(head_rect):
                snake.eatfood(food_rect)
                food.reinit()
                score += 1
                food=Food(screen,food_image_list[score%20])

            # 列印內容 引數：字串、是否平滑、顏色
            score_text = socre_font.render("score : "+str(score),True,(255,0,0))
            score_rect = score_text.get_rect()
            # 設定字型位置
            score_rect.centerx = 450
            score_rect.centery = 10
            screen.blit(score_text, score_rect)

            # 檢測是否撞到自己 （蛇頭和身體位置是否重合）
            head_rect = poslist[0]
            count = len(poslist)
            while count > 1:
                if head_rect==poslist[count - 1]:
                    running = False
                count -= 1
            # 更新螢幕
            pygame.display.update()
            # 遊戲結束介面
        screen.fill([255, 255, 240])
        # 一個字型物件，引數一：字型（None為預設）  引數二：字型大小
        font = pygame.font.Font(None, 38)

        # 繪製文字，返回surface
        text = font.render("Game Over! press space to restart. ", True, (255, 0, 0))
        textRect = text.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery
        screen.blit(text, textRect)
        # 是否重開
        while True:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    restart = True
                    # 初始化物件、變數
                    # python自動清理，只用刪除引用
                    score = 0
                    del snake
                    del food
                    break
            # 更新螢幕
            pygame.display.update()


run_game()