import turtle

# Yurakni yasash uchun funksiya
def draw_heart():
    turtle.color('red')  # Yurakning rangi
    turtle.begin_fill()  # To'ldirishni boshlash
    turtle.left(50)      # Burchakni o'ngga aylantirish
    turtle.forward(135)  # Birinchi qirradi to'ldirish
    turtle.circle(50, 200)  # Yurakning qismi
    turtle.right(140)     # Qaytish burchagi
    turtle.circle(50, 200)  # Yurakning qismi
    turtle.forward(120)   # Ikkinchi qirradi to'ldirish
    turtle.end_fill()     # To'ldirishni tugatish

# Asosiy kod
turtle.speed(0)  # Turtle ni tezligini sozlash
turtle.bgcolor('black')  # Foni qora rangga sozlash
draw_heart()  # Yurak rasmini chizish
turtle.hideturtle()  # Turtle ni yashirish
turtle.done()  # Dasturni tugatish

