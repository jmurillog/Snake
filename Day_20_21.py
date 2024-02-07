#Day 20 & 21

from turtle import Screen, update
from snakes import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()

def main():


    screen.clear()
    screen.setup(width = 600, height = 600)
    screen.title("Snake game")
    screen.bgcolor("black")
    scoreboard = Scoreboard()

    scoreboard.print_highest_score()
    scoreboard.hideturtle()
    time.sleep(1)
    screen.tracer(0)

    snake = Snake()
    food = Food()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game = True

    while game:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detectar si toca la comida
        if snake.head.distance(food) < 18:
            food.refresh()
            snake.extend()
            scoreboard.increase_scoreboard()
            
        #Detectar si choca con la pared
        if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
            game = False
            scoreboard.highes_score()
            scoreboard.game_over()
            user_bet = screen.textinput(title = "Volver a jugar", prompt = "¿Quieres volver a jugar?\nPresiona 'Enter'\n").lower().strip()
            while user_bet != "":
                user_bet = screen.textinput(title = "Volver a jugar", prompt = "¿Quieres volver a jugar?\nPresiona 'Enter'\n").lower().strip()
            if user_bet == "":
                main()
            else:
                return

        #Detectar si choca con la cola 
        for i in snake.snakes[1:]:
            if snake.head.distance(i) < 10:
                game = False
                scoreboard.highes_score()
                scoreboard.game_over()
                user_bet = screen.textinput(title = "Volver a jugar", prompt = "Quieres volver a jugar?\nPresiona 'Enter'").lower().strip()
                if user_bet == "":
                    main()
                else:
                    return


main()
screen.exitonclick()