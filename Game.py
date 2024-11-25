import pygame
import math

pygame.init()

screen_width = 1100
screen_height = 800

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sierpiński Hexagon Fractal")

# Colors of the Backgroud and Fractal
dark_orange = (255, 140, 0)
yellow = (255, 255, 0, 255)
# Backgroud 
screen.fill(yellow)

# Function to calculate the vertices of a hexagon
def calculate_hexagon(center_x, center_y, radius, rotation=0):
    points = []
    for i in range(6):  # A hexagon has 6 sides
        angle = math.radians(60 * i + rotation)  # Include rotation in the angle
        x = center_x + radius * math.cos(angle)  
        y = center_y + radius * math.sin(angle)  
        points.append((x, y))
    return points

# Function to draw a hexagon
def draw_hexagon(center_x, center_y, radius, color, width=1, rotation=0):
    points = calculate_hexagon(center_x, center_y, radius, rotation)
    pygame.draw.polygon(screen, color, points, width)

# Recursive function to draw the Sierpiński hexagon
def draw_sierpinski_hexagon(center_x, center_y, radius, depth, rotation=0):
    if depth <= 0:
        return

    # Draw the main hexagon
    draw_hexagon(center_x, center_y, radius, dark_orange, 5, rotation)

    # Radius of the smaller hexagons
    inner_radius = radius / 3

    # Distance from the center to the smaller hexagon centers
    distance_to_center = (2 * radius) / 3

    # Calculate and draw the 6 smaller hexagons
    for i in range(6):
        angle = math.radians(60 * i + rotation)  
        child_center_x = center_x + distance_to_center * math.cos(angle)
        child_center_y = center_y + distance_to_center * math.sin(angle)
        draw_sierpinski_hexagon(child_center_x, child_center_y, inner_radius, depth - 1, rotation)

    # Draw the central hexagon
    draw_sierpinski_hexagon(center_x, center_y, inner_radius, depth - 1, rotation)

# Main loop
running = True
fixed_rotation_angle = 90  # Set the fixed rotation angle (90 degrees)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Quit when the user closes the window
            running = False

    

    # Center and radius of the main hexagon
    center_x = screen_width // 2
    center_y = screen_height // 2
    radius = 200
    depth = 3  # Change depth to increase the fractal level

    
    
    # Draw the Sierpiński hexagon with the fixed rotation angle
    draw_sierpinski_hexagon(center_x, center_y, radius, depth, fixed_rotation_angle)
    pygame.display.update()


pygame.quit()

