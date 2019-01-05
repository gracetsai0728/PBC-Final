import pygame
import random

#先假設三個食物一開始的座標不會影響到後面的座標
pre_food1 = [1000000, 100000000]
pre_food2 = [1000000, 100000000]
pre_food3 = [1000000, 100000000]

class Food:
    """食物類"""

    def __init__(self, screen, picture, level):
        """隨機初始化第一個食物的位置"""
        self.screen = screen

        # 載入食物圖片並獲取外接矩形 (pygame通過外接矩陣操作圖片)
        self.image = pygame.image.load(picture)
        # 獲得圖片外接矩陣
        self.rect = self.image.get_rect()
        #使傳進來的每張圖片獲得對應的等級
        self.level = level

        # 隨機獲得圖片中心橫縱座標
        # （randint獲得10~690的int型別隨機數，包括10和690）
        # （rect.centerx為中心橫座標）
        self.rect.centerx = random.randint(20, 680)#------------------明明後面就要寫了，為什麼我前面還要再寫一遍？？？
        self.rect.centery = random.randint(20, 680)#這個是最開始的方程式，後面的是刷新的方程式，這裡不寫全部的食物都會卡在左上角

#重刷後隨機跑出一個圖形
    def reinit1(self):
        """ 隨機獲得一個食物，並返回食物座標"""
        global pre_food1
        global pre_food2
        global pre_food3
        while True:
            check_spot1 = [True, True]
            check_spot2 = [True, True]
            self.rect.centerx = random.randint(20, 680)
            self.rect.centery = random.randint(20, 680)
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food2[0]-20+i:
                        check_spot1[0] = False
                    if self.rect.centery == pre_food2[1]-20+j:
                        check_spot1[1] = False
            if check_spot1 == [False, False]:
                continue
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food3[0]-20+i:
                        check_spot2[0] = False
                    if self.rect.centery == pre_food3[1]-20+j:
                        check_spot2[1] = False
            if check_spot2 == [False, False]:
                continue
            else:
                break
        pre_food1 = [self.rect.centerx, self.rect.centery]
        return [self.rect.centerx, self.rect.centery]

    def reinit2(self):
        """ 隨機獲得一個食物，並返回食物座標"""
        global pre_food1
        global pre_food2
        global pre_food3
        while True:
            check_spot1 = [True, True]
            check_spot2 = [True, True]
            self.rect.centerx = random.randint(20, 680)
            self.rect.centery = random.randint(20, 680)
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food1[0]-20+i:
                        check_spot1[0] = False
                    if self.rect.centery == pre_food1[1]-20+j:
                        check_spot1[1] = False
            if check_spot1 == [False, False]:
                continue
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food3[0]-20+i:
                        check_spot2[0] = False
                    if self.rect.centery == pre_food3[1]-20+j:
                        check_spot2[1] = False
            if check_spot2 == [False, False]:
                continue
            else:
                break
        pre_food2 = [self.rect.centerx, self.rect.centery]
        return [self.rect.centerx, self.rect.centery]

    def reinit3(self):
        """ 隨機獲得一個食物，並返回食物座標"""
        global pre_food1
        global pre_food2
        global pre_food3
        while True:
            check_spot1 = [True, True]
            check_spot2 = [True, True]
            self.rect.centerx = random.randint(20, 680)
            self.rect.centery = random.randint(20, 680)
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food1[0]-20+i:
                        check_spot1[0] = False
                    if self.rect.centery == pre_food1[1]-20+j:
                        check_spot1[1] = False
            if check_spot1 == [False, False]:
                continue
            for i in range(40):
                for j in range(40):
                    if self.rect.centerx == pre_food2[0]-20+i:
                        check_spot2[0] = False
                    if self.rect.centery == pre_food2[1]-20+j:
                        check_spot2[1] = False
            if check_spot2 == [False, False]:
                continue
            else:
                break
        pre_food3 = [self.rect.centerx, self.rect.centery]
        return [self.rect.centerx, self.rect.centery]

    def position(self):
        """ 返回食物座標（中心點x,y）"""

        return [self.rect.centerx, self.rect.centery]

    def foodrect(self):
        """返回外接矩矩形"""

        return self.rect

    def blitball(self):
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
        self.screen_width = 700
        self.screen_height = 700
        # 設定螢幕背景色
        self.bg_color = [255, 255, 240]
        # 設定蛇移動速度（幀數）
        self.speed = 3
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

            #if self.poslist[0][1] < 0:
                #self.poslist[0][1] = 485
        if new_direction is 'D':
            self.poslist[0][1] += 32
            #if self.poslist[0][1] > 485:
                #self.poslist[0][1] = 0
        if new_direction is 'L':
            self.poslist[0][0] -= 32
            #if self.poslist[0][0] < 0:
                #self.poslist[0][0] = 485
        if new_direction is 'R':
            self.poslist[0][0] += 32
            #if self.poslist[0][0] > 485:
                #self.poslist[0][0] = 0

            if self.poslist[0][1] < 0:
                self.poslist[0][1] = 685
        if new_direction is 'D':
            self.poslist[0][1] += 32
            if self.poslist[0][1] > 685:
                self.poslist[0][1] = 0
        if new_direction is 'L':
            self.poslist[0][0] -= 32
            if self.poslist[0][0] < 0:
                self.poslist[0][0] = 685
        if new_direction is 'R':
            self.poslist[0][0] += 32
            if self.poslist[0][0] > 685:
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

                self.screen.blit(self.bodyimage, (poslist[i]))


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
    level_font = pygame.font.Font(None, 28)
    # 記錄分數&自己的等級
    score = 0
    level = 1
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
        food1 = Food(screen, food_image_list[0], 1)
        food2 = Food(screen, food_image_list[1], 2)
        food3 = Food(screen, food_image_list[2], 3)
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
            food1_rect = food1.foodrect()
            food2_rect = food2.foodrect()
            food3_rect = food3.foodrect()
            # 繪製這個食物
            food1.blitball()
            food2.blitball()
            food3.blitball()
            # 繪製蛇
            poslist = snake.position()
            snake.draw_snake(poslist)
            head_rect = poslist[0]

            # 吃到食物
            if food1_rect.colliderect(head_rect):
                #一旦吃到食物就檢查自己的等級是否有比圖片的等級大
                if food1.level > level:
                    running = False
                else:
                    snake.eatfood(food1_rect)
                    food1.reinit1()
                    score += 1
                    level += 1
                    if score % 20 == 18 or score % 20 == 19:
                        #每張圖片的等級都是自己在list裡面的位置+1
                        food1 = Food(screen, food_image_list[score%20], (score%20)+1)
                    else:
                        food1 = Food(screen, food_image_list[(score % 20)+2], (score%20)+3)

            if food2_rect.colliderect(head_rect):
                if food2.level > level:
                    running = False
                else:
                    snake.eatfood(food2_rect)
                    food2.reinit2()
                    score += 1
                    level += 1
                    if score % 20 == 18 or score % 20 == 19:
                        food2 = Food(screen, food_image_list[score%20], (score%20)+1)
                    else:
                        food2 = Food(screen, food_image_list[(score % 20)+2], (score%20)+3)

            if food3_rect.colliderect(head_rect):
                if food3.level > level:
                    running = False
                else:
                    snake.eatfood(food3_rect)
                    food3.reinit3()
                    score += 1
                    level += 1
                    if score % 20 == 18 or score % 20 == 19:
                        food3 = Food(screen, food_image_list[score%20], (score%20)+1)
                    else:
                        food3 = Food(screen, food_image_list[(score % 20)+2], (score%20)+3)
            #根據自己的等級來調整速度，30等達最快速度12
            if level >2 and level <= 8:
                run_settings.speed = 5
            if level >8 and level <= 13:
                run_settings.speed = 7
            if level >13 and level <=30:
                run_settings.speed = 10
            if level >30:
                run_settings.speed = 12
            

            # 列印內容 引數：字串、是否平滑、顏色
            score_text = socre_font.render("score : "+str(score),True,(255,0,0))
            score_rect = score_text.get_rect()
            level_text = level_font.render("level : "+str(level),True,(255,0,0))
            level_rect = level_text.get_rect()
            # 設定字型位置
            score_rect.centerx = 650
            score_rect.centery = 10
            screen.blit(score_text, score_rect)

            level_rect.centerx = 550
            level_rect.centery = 10
            screen.blit(level_text, level_rect)

            # 檢測是否撞到自己 （蛇頭和身體位置是否重合）
            head_rect = poslist[0]
            count = len(poslist)
            while count > 1:
                if head_rect==poslist[count - 1]:
                    running = False
                elif new_direction is 'R':
                    self.poslist[0][0] += 32
                    if self.poslist[0][0] > 485:
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
