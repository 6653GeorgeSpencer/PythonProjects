import pygame as py
from levels import tileList


class Player(py.sprite.Sprite):
    def __init__(self) -> None:
        py.sprite.Sprite.__init__(self)
        self.a_KEY, self.d_KEY, self.w_key = False, False, False
        self.isOnGround, self.isJumping = False, False
        self.gravity, self.friction = .99, -.12
        self.image = py.Surface((32, 32))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1980
        self.pos, self.velocity = py.math.Vector2(0, 0), py.math.Vector2(0, 0)
        self.acceleration = py.math.Vector2(0, self.gravity)
        self.image.fill((0, 0, 0))
        self.Hasdash, self.doubleJump = False, False
        self.isDashing = False
        self.facingDir = {"left": False, "right": False}
        self.velocityLimiter = 0
        self.inAir = False
        self.drawnPos = 0
        self.isTouching = False

    def update(self, dt, off):
        self.horizontalMovement(dt, off)
        self.checkCollisionsx(tileList, off)
        self.verticalMovement(dt)
        self.checkCollisionsY(tileList, off)
        if self.velocityLimiter > 0:
            self.velocityLimiter -= 1

    def draw(self, display, off):
        display.blit(self.image, (self.rect.x, self.rect.y))

    def horizontalMovement(self, dt, off):
        self.acceleration.x = 0
        if self.a_KEY:
            self.acceleration.x -= 2
            self.facingDir["left"] = True
            self.facingDir["right"] = False
            self.facingDir["up"] = False
        elif self.d_KEY:
            self.acceleration.x += 2
            self.facingDir["right"] = True
            self.facingDir["left"] = False
            self.facingDir["up"] = False
        elif self.w_key:
            self.facingDir["up"] = True
            self.facingDir["left"] = False
            self.facingDir["right"] = False
        self.acceleration.x += self.velocity.x * self.friction
        self.velocity.x += self.acceleration.x * dt
        self.limitVelocity(3.5)
        self.pos.x += self.velocity.x * dt + (self.acceleration.x * 0.5) * (dt * dt)
        self.rect.x = self.pos.x - off

    def verticalMovement(self, dt):
        self.velocity.y += self.acceleration.y * dt
        if self.velocity.y > 12: self.velocity.y = 12
        self.pos.y += self.velocity.y * dt + (self.acceleration.y * 0.5) * (dt * dt)
        self.rect.bottom = self.pos.y

    def limitVelocity(self, maxVel):
        if self.velocityLimiter == 0:
            self.velocity.x = max(-maxVel, min(self.velocity.x, maxVel))
            self.isDashing = False
            if abs(self.velocity.x) < 0.01:
                self.velocity.x = 0


    def dash(self):
        if self.Hasdash:
            self.isDashing = True
        if self.Hasdash and self.facingDir["left"]:
            print("a")
            self.velocity.x -= 12
            self.Hasdash = False
            self.velocityLimiter = 5
        if self.Hasdash and self.facingDir["right"]:
            print("a")
            self.velocity.x += 12
            self.Hasdash = False
            self.velocityLimiter = 5
        if self.Hasdash and self.facingDir["up"]:
            if self.velocity.y > 0:
                self.velocity.y = 0
            self.velocity.y -= 16
            self.Hasdash = False
            self.velocityLimiter = 5

    def jump(self):
        if self.isOnGround:
            self.isJumping = True
            self.velocity.y -= 16
            self.isOnGround = False
            if self.d_KEY:
                self.velocity.x *= 1.25
            elif self.a_KEY:
                self.velocity.x *= 1.25

    def checkCollisions(self, tiles, off):
        hits = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                hits.append(tile)
        return hits

    def checkCollisionsx(self, tiles, off):
        hits = self.checkCollisions(tiles, off)
        for tile in hits:
            if self.velocity.x > 0:
                self.velocity.x = 0
                self.acceleration.x = 0
                self.isTouching = True
                self.rect.x = (tile.rect.left - self.rect.w)
                self.pos.x = self.rect.x + off





                print("right")
            elif self.velocity.x < 0:
                self.isTouching = True
                self.velocity.x = 0
                self.acceleration.x = 0
                self.rect.x = tile.rect.right
                self.pos.x = self.rect.x + off


            if self.pos.x < 0:
                self.pos.x = 0

        self.isTouching = False

    def checkCollisionsY(self, tiles, off):
        self.isOnGround = False
        if not self.isDashing:
            self.rect.bottom += 1

        self.inAir = True
        hits = self.checkCollisions(tiles, off)
        for tile in hits:
            if self.velocity.y > 0:
                self.isOnGround = True
                self.isJumping = False
                self.doubleJump = True
                self.Hasdash = True
                self.inAir = False
                self.velocity.y = 0
                self.pos.y = tile.rect.top
                self.rect.bottom = self.pos.y
            elif self.velocity.y < 0:
                self.velocity.y = 0
                self.pos.y = tile.rect.bottom + self.rect.h
                self.rect.bottom = self.pos.y
