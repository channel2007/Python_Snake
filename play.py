# encoding: utf-8
import os, random, sys, random
import pygame

from pygame.locals import *
from doublyLinkedList import *

# 初始位置.
CONST_STARTING_SNAKE_POS_X = 32
CONST_STARTING_SNAKE_POS_Y = 24

# 視窗大小.
canvas_width = 800
canvas_height = 600

# 遊戲區大小.
game_area_width  = 64
game_area_height = 48

# 顏色.
block = (0,0,0)
darkBlock = (148,190,2)
darkGreen = (41,66,0)

# 遊戲區陣列.
gameAreaArray =[[0]*game_area_height for i in range(game_area_width)]

# 除錯訊息.
debug_message = False
# 判斷遊戲結束.
game_over = False

# 分數.
score = 0

# 每秒執行主迴圈次數.
fps = 8

# 開始位置.
snake_x = CONST_STARTING_SNAKE_POS_X
snake_y = CONST_STARTING_SNAKE_POS_Y
# 前進方向.
# 0:上 1:下 2:左 3:右.
direction = 1
# 產生節點數.
generate_node = 3
# 蛇身體位置串列.
snake_body_linkedList = DoublyLinkedList()

# 要吃的節點資料.
# 0:x 1:y 2:產生蛇身數量.
eat_data = [32,24,5]

# 10:遊戲開始.
# 11:GameOver.
game_mode = 10

#-------------------------------------------------------------------------
# 函數:亂數產生要吃的數字節點.
#-------------------------------------------------------------------------
def randomEatData():
    r = True
    while r:
        # 亂數陣列位置.
        eat_data[0] = random.randint(2, 61)
        eat_data[1] = random.randint(7, 45)
        # 亂數產生增加蛇身數量.
        eat_data[2] = random.randint(3, 9)
        # 陣列位置為空.
        if(gameAreaArray[eat_data[0]][eat_data[1]] == 0):
            # 設定產生蛇身數量.
            gameAreaArray[eat_data[0]][eat_data[1]] = eat_data[2]
            # 離開迴圈.
            r = False

#-------------------------------------------------------------------------
# 函數:秀字.
#-------------------------------------------------------------------------
def showFont( text, x, y, color, size):
    global canvas
    if(size==24):
        text = font_24.render(text, True, color) 
    else:
        text = font_40.render(text, True, color) 
    canvas.blit( text, (x,y))

#-------------------------------------------------------------------------
# 函數:重新開始遊戲.
#-------------------------------------------------------------------------
def resetGame():
    global game_mode, score,snake_x, snake_y
    # 分數.
    score = 0
    # 開始位置.
    snake_x = CONST_STARTING_SNAKE_POS_X
    snake_y = CONST_STARTING_SNAKE_POS_Y
    # 蛇身位置串列.
    for i in range(snake_body_linkedList.size()-3):
        snake_body_linkedList.remove_first()
    # 清除畫面陣列.
    for y in range(game_area_height):
        for x in range(game_area_width):             
            gameAreaArray[x][y] = 0
    # 亂數產生要吃的數字節點..
    randomEatData()
    # 開始遊戲.
    game_mode = 10

#-------------------------------------------------------------------------
# 主程式.
#-------------------------------------------------------------------------
if __name__=='__main__':
    # 初始.
    pygame.init()
    # 顯示Title.
    pygame.display.set_caption(u"貪吃蛇")
    # 建立畫佈大小.
    canvas = pygame.display.set_mode((canvas_width, canvas_height))
    
    # 時脈.
    clock = pygame.time.Clock()

    # 設定字型.
    font_24 = pygame.font.Font("Fonts/Cascadia.ttf", 24)
    font_40 = pygame.font.Font("Fonts/Cascadia.ttf", 40)
    
    # 亂數產生要吃的數字節點..
    randomEatData()

    #-------------------------------------------------------------------------    
    # 主迴圈.
    #-------------------------------------------------------------------------
    running = True
    while running:
        # 每秒執行fps次
        clock.tick(fps)
        
        #---------------------------------------------------------------------
        # 判斷輸入.
        #---------------------------------------------------------------------
        for event in pygame.event.get():
            # 離開遊戲.
            if event.type == pygame.QUIT:
                running = False
            # 判斷按下按鈕
            if event.type == pygame.KEYDOWN:
                # 判斷按下ESC按鈕
                if event.key == pygame.K_ESCAPE:
                    running = False
                # 除錯訊息開關.
                elif event.key == pygame.K_d:
                    debug_message = not debug_message

                # 10:遊戲開始.
                if(game_mode == 10):
                    #-----------------------------------------------------------------
                    # 上.
                    if event.key == pygame.K_UP:
                        direction = 0
                    #-----------------------------------------------------------------
                    # 下.
                    elif event.key == pygame.K_DOWN:
                        direction = 1
                    #-----------------------------------------------------------------
                    # 左.
                    elif event.key == pygame.K_LEFT:
                        direction = 2
                    #-----------------------------------------------------------------
                    # 右.
                    elif event.key == pygame.K_RIGHT:
                        direction = 3

                # 11:Game Over.
                elif (game_mode == 11):
                    if event.key == pygame.K_RETURN:
                        resetGame()

        #--------------------------------------------------------------------- 
        # 邏輯運算.   
        #---------------------------------------------------------------------    
        # 10:遊戲開始.
        if(game_mode == 10):
            # 判斷吃到數字節點.
            if(gameAreaArray[snake_x][snake_y] >= 1 and gameAreaArray[snake_x][snake_y] <= 9):
                # 加分數.
                score += gameAreaArray[snake_x][snake_y]
                # 設定要產生的蛇身體數量.
                generate_node = gameAreaArray[snake_x][snake_y]
                # 清除產生蛇身體數量節點.
                gameAreaArray[snake_x][snake_y] = 0
                # 亂數產生要吃的數字節點.
                randomEatData()

            # 蛇前進.
            if(gameAreaArray[snake_x][snake_y] == 0):
                # 設定蛇身體陣列編號.
                gameAreaArray[snake_x][snake_y] = 10
                
                # 將節點加入串列鏈節.
                snake_body_linkedList.insert_front([snake_x,snake_y])
                # 增加節點.
                if(generate_node > 0):
                    generate_node-=1
                else:
                    # 取得尾節點.
                    p = snake_body_linkedList.fetch(snake_body_linkedList.size()-1)
                    # 清除尾節點陣列編號.
                    gameAreaArray[p[0]][p[1]] = 0
                    # 刪除尾節點.
                    snake_body_linkedList.remove_last()

                # 控制蛇前進方向.
                # 0:上.
                if (direction == 0):
                    snake_y -= 1
                # 1:下.
                elif (direction == 1):
                    snake_y += 1
                # 2:左.
                elif (direction == 2):
                    snake_x -= 1
                # 3:右.
                elif (direction == 3):
                    snake_x += 1
            # 失敗.
            else:
                # 清除產生節點數.
                generate_node = 0
                # 11:GameOver.
                game_mode = 11

        #--------------------------------------------------------------------- 
        # 繪製畫面.   
        #---------------------------------------------------------------------    
        # 清除畫面.
        canvas.fill(darkBlock)
        
        # 外框.
        for x in range(game_area_width):
            if(gameAreaArray[x][3]==0):
                gameAreaArray[x][3] = 10
            if(gameAreaArray[x][5]==0):
                gameAreaArray[x][5] = 10
            if(gameAreaArray[x][game_area_height-1]==0):
                gameAreaArray[x][game_area_height-1] =  10
        for y in range(5,game_area_height):
            if(gameAreaArray[0][y]==0):
                gameAreaArray[0][y] = 10
            if(gameAreaArray[game_area_width-1][y]==0):
                gameAreaArray[game_area_width-1][y] = 10

        # 顯示分數.
        showFont( str(score), 14, 0, darkGreen, 40)

        # 繪製遊戲區.
        ix = 15
        iy = 2
        for y in range(game_area_height):
            for x in range(game_area_width): 
                # 顯示數字-1.
                if(gameAreaArray[x][y]==1):
                    showFont( u"1", ix, iy, darkGreen, 24)
                # 顯示數字-2.
                elif(gameAreaArray[x][y]==2):
                    showFont( u"2", ix, iy, darkGreen, 24)
                # 顯示數字-3.
                elif(gameAreaArray[x][y]==3):
                    showFont( u"3", ix, iy, darkGreen, 24)
                # 顯示數字-4.
                elif(gameAreaArray[x][y]==4):
                    showFont( u"4", ix, iy, darkGreen, 24)
                # 顯示數字-5.
                elif(gameAreaArray[x][y]==5):
                    showFont( u"5", ix, iy, darkGreen, 24)
                # 顯示數字-6.
                elif(gameAreaArray[x][y]==6):
                    showFont( u"6", ix, iy, darkGreen, 24)
                # 顯示數字-7.
                elif(gameAreaArray[x][y]==7):
                    showFont( u"7", ix, iy, darkGreen, 24)
                # 顯示數字-8.
                elif(gameAreaArray[x][y]==8):
                    showFont( u"8", ix, iy, darkGreen, 24)
                # 顯示數字-9.
                elif(gameAreaArray[x][y]==9):
                    showFont( u"9", ix, iy, darkGreen, 24)
                # 方塊.
                elif(gameAreaArray[x][y]==10):
                    showFont( u"⬛", ix, iy, darkGreen, 24)
                # 空.
                elif(gameAreaArray[x][y]==11):
                    showFont( u"⠀", ix, iy, darkGreen, 24)
                # 除錯.
                if(debug_message):
                    if(gameAreaArray[x][y]!=0):
                        # 顯示除錯訊息.
                        showFont( str(gameAreaArray[x][y]), ix, iy, (255, 0, 0), 24)
                        # 顯示FPS.
                        showFont( u"FPS:" + str(int(clock.get_fps())), 8, 2, (255, 0, 0), 24)
                ix+=12
            ix = 15
            iy+=12

        # 顯示 GameOver.
        if(game_mode == 11):
            showFont( u"GAME OVER", 300, 280, darkGreen, 40)

        # 更新畫面.
        pygame.display.update()

    # 離開遊戲.
    pygame.quit()
    quit()