import pygame
import random
import math
import numpy as np

WIDTH, HEIGHT    = 800, 600
FPS              = 60
NUM_CREATURES    = 20
NUM_FOOD         = 20   
ENERGY_MAX       = 400  
MUTATION_RATE    = 0.25 

WHITE  = (255, 255, 255)
BLACK  = (0,   0,   0)
GREEN  = (0,   255, 0)
BLUE   = (50,  150, 255)
RED    = (220, 50,  50)
YELLOW = (255, 215, 0)
ORANGE = (255, 140, 0)

pygame.init()
screen   = pygame.display.set_mode((WIDTH, HEIGHT))
clock    = pygame.time.Clock()
font     = pygame.font.SysFont("Arial", 18)
pygame.display.set_caption("EvoLife Simulation - Direction Lock Fix")

class NeuralNetwork:
    def __init__(self):
        self.weights = np.random.uniform(-0.6, 0.6, (3, 2))

    def think(self, inputs):
        raw_output = np.dot(inputs, self.weights)
        return np.tanh(raw_output)

    def copy(self):
        new_brain = NeuralNetwork()
        new_brain.weights = self.weights.copy()
        return new_brain

    def mutate(self, rate=MUTATION_RATE):
        mask = np.random.random(self.weights.shape) < rate
        self.weights[mask] += np.random.uniform(-0.3, 0.3, self.weights[mask].shape)
        self.weights = np.clip(self.weights, -1.5, 1.5)

class Creature:
    def __init__(self, brain=None):
        self.x       = random.randint(100, WIDTH - 100)
        self.y       = random.randint(100, HEIGHT - 100)
        self.speed   = 2.2  
        self.radius  = 10
        self.brain   = brain if brain else NeuralNetwork()
        self.energy  = ENERGY_MAX
        self.fitness = 0
        self.alive   = True

    def move(self, foods):
        if not self.alive:
            return
            
        inputs = self.get_inputs(foods)
        output = self.brain.think(inputs)
        
        self.x += output[0] * self.speed
        self.y += output[1] * self.speed
        
        if self.x <= self.radius: self.x = self.radius + 5
        elif self.x >= WIDTH - self.radius: self.x = WIDTH - self.radius - 5

        if self.y <= self.radius: self.y = self.radius + 5
        elif self.y >= HEIGHT - self.radius: self.y = HEIGHT - self.radius - 5
        
        self.energy -= 1
        if self.energy <= 0:
            self.alive = False

    def draw(self, surface):
        if not self.alive:
            return
        
        ratio = self.energy / ENERGY_MAX
        color = (int(255 * (1 - ratio)), int(150 * ratio), 255)
        
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.radius, 2)
        
        bar_width = 20
        filled    = int(bar_width * ratio)
        pygame.draw.rect(surface, RED,   (int(self.x) - 10, int(self.y) - 18, bar_width, 3))
        pygame.draw.rect(surface, GREEN, (int(self.x) - 10, int(self.y) - 18, filled,    3))

def get_inputs(self, foods):
    nearest  = None
    min_dist = float('inf')
    for food in foods:
        dist = math.hypot(food.x - self.x, food.y - self.y)
        if dist < min_dist:
            min_dist = dist
            nearest  = food

    if nearest is None:
        return np.array([0.0, 0.0, 1.0])

    dx = nearest.x - self.x
    dy = nearest.y - self.y
    
    if min_dist > 0:
        dx_unit = dx / min_dist
        dy_unit = dy / min_dist
    else:
        dx_unit, dy_unit = 0.0, 0.0

    bias = 1.0 
    return np.array([dx_unit, dy_unit, bias])

def eat(self, foods):
    for food in foods[:]:
        dist = math.hypot(food.x - self.x, food.y - self.y)
        if dist < self.radius + food.radius:
            foods.remove(food)
            foods.append(Food()) 
            self.energy   = min(ENERGY_MAX, self.energy + 175) 
            self.fitness += 1

Creature.get_inputs = get_inputs
Creature.eat        = eat

class Food:
    def __init__(self):
        self.x      = random.randint(50, WIDTH  - 50)
        self.y      = random.randint(50, HEIGHT - 50)
        self.radius = 5

    def draw(self, surface):
        pygame.draw.circle(surface, GREEN, (int(self.x), int(self.y)), self.radius)

def evolve(creatures):
    sorted_creatures = sorted(creatures, key=lambda c: c.fitness, reverse=True)
    parents      = sorted_creatures[:5] 
    best_fitness = parents[0].fitness

    new_creatures = []

    for i in range(2):
        new_creatures.append(Creature(brain=parents[i].brain.copy()))

    while len(new_creatures) < (NUM_CREATURES - 4):
        parent = random.choice(parents)
        child_brain = parent.brain.copy()
        child_brain.mutate()
        new_creatures.append(Creature(brain=child_brain))

    for _ in range(4):
        new_creatures.append(Creature())

    return new_creatures, best_fitness

creatures     = [Creature() for _ in range(NUM_CREATURES)]
foods         = [Food()     for _ in range(NUM_FOOD)]
generation    = 1
all_time_best = 0

running = True
while running:

    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    alive_count = 0
    force_evolution_reset = False
    
    for creature in creatures:
        creature.move(foods)
        creature.eat(foods)
        creature.draw(screen)
        if creature.alive:
            alive_count += 1
            
        if creature.fitness >= 20:
            force_evolution_reset = True

    for food in foods:
        food.draw(screen)

    if alive_count == 0 or force_evolution_reset:
        creatures, best_fitness = evolve(creatures)
        foods         = [Food() for _ in range(NUM_FOOD)]
        generation   += 1
        if best_fitness > all_time_best:
            all_time_best = best_fitness

    best_now = max((c.fitness for c in creatures), default=0)

    line1 = font.render(f"Generation : {generation}", True, YELLOW)
    line2 = font.render(f"Alive      : {alive_count} / {NUM_CREATURES}", True, WHITE)
    line3 = font.render(f"Best Now   : {best_now} eaten", True, GREEN)
    line4 = font.render(f"Best Ever  : {all_time_best} eaten", True, ORANGE)

    screen.blit(line1, (10, 10))
    screen.blit(line2, (10, 35))
    screen.blit(line3, (10, 60))
    screen.blit(line4, (10, 85))

    pygame.display.flip()

pygame.quit()
