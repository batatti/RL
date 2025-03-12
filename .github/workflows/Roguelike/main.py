import pygame
import random

import pygame
import asyncio

# 非同期のメイン関数
async def main():
    pygame.init()

    # 画面サイズの設定
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Rogue-like Game")

    # 色の定義
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    # プレイヤーの設定
    player_size = 20
    player_x = screen_width // 2
    player_y = screen_height // 2
    player_speed = 5

    # ゲームループのフラグ
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # キー入力の処理
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed

        # 画面のクリア
        screen.fill(BLACK)

        # プレイヤーの描画
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

        # 画面の更新
        pygame.display.flip()

        # フレームレートの設定
        clock.tick(30)

        # 非同期の待機
        await asyncio.sleep(0)

    pygame.quit()

# 非同期のエントリーポイントを実行
asyncio.run(main())
