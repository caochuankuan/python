import turtle
import random

# 设置窗口大小
window_size = 600
# 设置面板行数列数
board_size = 4
# 设置面板大小
cell_size = window_size // board_size

# 初始化窗口和画笔
window = turtle.Screen()
window.title("2048(4x4版)小游戏\tby:曹传宽")
window.setup(window_size, window_size)
window.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

# 创建游戏板
board = [[0] * board_size for _ in range(board_size)]


# 添加随机数字
def add_random_number():
    empty_cells = [(i, j) for i in range(board_size) for j in range(board_size) if board[i][j] == 0]  # 列表推导式
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = random.choice([2, 4])


# 绘制方块
def draw_square(row, col, value):
    # 游戏框坐标
    x = (col - board_size / 2 - 0.5) * cell_size + cell_size / 2
    y = (board_size / 2 - row + 0.5) * cell_size - cell_size / 2

    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(get_color(value))
    pen.begin_fill()

    # 笔记：
    # 在这个特定的示例中，for _ in range(4) 循环的意义可能不太明显，因为在循环体中并没有使用到变量 _。这种情况下，可以使用任何变量名替代 _，例如 for i in range(4)。
    # 然而，有时候在编程中，我们可能只关心循环的次数，而不需要使用循环变量的值。在这种情况下，使用_作为循环变量可以传达一个清晰的信号，告诉其他人或自己，这个循环变量的值并不重要。
    # 此外，使用_作为循环变量还可以避免产生未使用的变量警告，这在某些编程语言或开发环境中是一个常见的问题。
    # 总的来说，使用_作为循环变量在这个示例中可能没有特别的意义，但在其他情况下，它可以提供一种简洁和清晰的方式来表示循环次数不重要或不需要使用循环变量的情况。
    for _ in range(4):
        pen.forward(cell_size - 2)
        pen.right(90)

    pen.end_fill()
    pen.penup()

    if value != 0:
        # 数字坐标
        pen.goto(x + 70, y - 120)
        pen.write(str(value), align="center", font=("Arial", 50, "normal"))


# 获取方块颜色
def get_color(value):
    colors = {
        0: "#CDC1B4",
        2: "#EEE4DA",
        4: "#EDE0C8",
        8: "#F2B179",
        16: "#F59563",
        32: "#F67C5F",
        64: "#F65E3B",
        128: "#EDCF72",
        256: "#EDCC61",
        512: "#EDC850",
        1024: "#EDC53F",
        2048: "#EDC22E"
    }
    return colors.get(value, "#CDC1B4")


# 绘制游戏界面
def draw_board():
    pen.clear()
    for row in range(board_size):
        for col in range(board_size):
            value = board[row][col]
            draw_square(row, col, value)
    window.update()


# 移动游戏板
def move(dir):
    if dir == "up":
        for col in range(board_size):
            merge_column_up(col)
    elif dir == "down":
        for col in range(board_size):
            merge_column_down(col)
    elif dir == "left":
        for row in range(board_size):
            merge_row_left(row)
    elif dir == "right":
        for row in range(board_size):
            merge_row_right(row)
    add_random_number()
    draw_board()


# 合并列（向上移动）
def merge_column_up(col):
    for row in range(1, board_size):
        if board[row][col] != 0:
            for k in range(row, 0, -1):
                if board[k - 1][col] == 0:
                    board[k - 1][col] = board[k][col]
                    board[k][col] = 0
                elif board[k - 1][col] == board[k][col]:
                    board[k - 1][col] *= 2
                    board[k][col] = 0
                    break


# 合并列（向下移动）
def merge_column_down(col):
    for row in range(board_size - 2, -1, -1):
        if board[row][col] != 0:
            for k in range(row, board_size - 1):
                if board[k + 1][col] == 0:
                    board[k + 1][col] = board[k][col]
                    board[k][col] = 0
                elif board[k + 1][col] == board[k][col]:
                    board[k + 1][col] *= 2
                    board[k][col] = 0
                    break


# 合并行（向左移动）
def merge_row_left(row):
    for col in range(1, board_size):
        if board[row][col] != 0:
            for k in range(col, 0, -1):
                if board[row][k - 1] == 0:
                    board[row][k - 1] = board[row][k]
                    board[row][k] = 0
                elif board[row][k - 1] == board[row][k]:
                    board[row][k - 1] *= 2
                    board[row][k] = 0
                    break


# 合并行（向右移动）
def merge_row_right(row):
    for col in range(board_size - 2, -1, -1):
        if board[row][col] != 0:
            for k in range(col, board_size - 1):
                if board[row][k + 1] == 0:
                    board[row][k + 1] = board[row][k]
                    board[row][k] = 0
                elif board[row][k + 1] == board[row][k]:
                    board[row][k + 1] *= 2
                    board[row][k] = 0
                    break


# 检查游戏是否结束
def is_game_over():
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return False

    for row in range(3):
        for col in range(3):
            if board[row][col] == board[row + 1][col] or board[row][col] == board[row][col + 1]:
                return False

    pen.goto(0, 0)
    pen.write("游戏结束", align="center", font=("黑体", 50, "normal"))
    window.update()

    return True


# 处理按键事件
def handle_key(key):
    if key == "Up":
        move("up")
    elif key == "Down":
        move("down")
    elif key == "Left":
        move("left")
    elif key == "Right":
        move("right")

    if is_game_over():
        # 用于关闭界面
        # window.bye()
        pass


# 初始化游戏
def init_game():
    add_random_number()
    add_random_number()
    draw_board()


# 注册按键事件
window.listen()  # 事件监听
window.onkey(lambda: handle_key("Up"), "Up")
window.onkey(lambda: handle_key("Down"), "Down")
window.onkey(lambda: handle_key("Left"), "Left")
window.onkey(lambda: handle_key("Right"), "Right")

# 启动游戏
init_game()
turtle.done()
