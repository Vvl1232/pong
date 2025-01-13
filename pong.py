from turtle import Turtle, Screen

# Setup the screen
s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong game")
s.tracer(0)

# Score variables
left_score = 0
right_score = 0

#===================================================left paddle==========================================================
def create_left_paddle():
    t = Turtle()
    t.shape("square")
    t.color("red")
    t.shapesize(stretch_wid=5, stretch_len=1)
    t.penup()
    t.goto(x=-360, y=0)

    def go_up():
        if t.ycor() < 250:
            new_y = t.ycor() + 20
            t.goto(t.xcor(), new_y)

    def go_down():
        if t.ycor() > -240:
            new_y = t.ycor() - 20
            t.goto(t.xcor(), new_y)

    s.listen()
    s.onkeypress(go_up, "w")
    s.onkeypress(go_down, "s")

    return t

#=======================================================right paddle=======================================================
def create_right_paddle():
    t = Turtle()
    t.shape("square")
    t.color("skyblue")
    t.shapesize(stretch_wid=5, stretch_len=1)
    t.penup()
    t.goto(x=350, y=0)

    def go_up():
        if t.ycor() < 250:
            new_y = t.ycor() + 20
            t.goto(t.xcor(), new_y)

    def go_down():
        if t.ycor() > -240:
            new_y = t.ycor() - 20
            t.goto(t.xcor(), new_y)

    s.listen()
    s.onkeypress(go_up, "Up")
    s.onkeypress(go_down, "Down")

    return t

#============================================================ball=========================================================
def create_ball():
    t = Turtle()
    t.shape("circle")
    t.color("white")
    t.goto(x=0, y=0)
    t.shapesize(stretch_wid=1.3, stretch_len=1.3)
    t.penup()
    t.dx = 0.12  # Increased ball speed
    t.dy = 0.12  # Increased ball speed

    return t

#===========================================================score display===================================================
def display_score():
    score.clear()
    score.color("white")
    score.penup()
    score.goto(0, 260)
    score.hideturtle()
    score.write(f"{left_score}  {right_score}", align="center", font=("Courier", 24, "normal"))

#=======================================================function call=======================================================
left_paddle = create_left_paddle()
right_paddle = create_right_paddle()
ball = create_ball()
score = Turtle()

display_score()  # Initial score display

# Function to display Game Over and restart the game
def game_over():
    global game_is_on
    game_is_on = False

    # Display Game Over
    game_over_turtle = Turtle()
    game_over_turtle.color("white")
    game_over_turtle.hideturtle()
    game_over_turtle.penup()
    game_over_turtle.goto(0, 0)
    game_over_turtle.write("Game Over", align="center", font=("Courier", 24, "normal"))

#=======================================================game loop=======================================================
game_is_on = True
while game_is_on:
    s.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Bounce off top and bottom edges
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Ball reset when out of bounds on left and right edges
    if ball.xcor() > 410 or ball.xcor() < -410:
        game_over()

    # Ball and paddle collision
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 340) or (ball.distance(left_paddle) < 50 and ball.xcor() < -340):
        ball.dx *= -1

        # Update score
        if ball.xcor() > 0:
            right_score += 1
        else:
            left_score += 1
        display_score()

s.exitonclick()
