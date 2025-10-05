from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

# Текст и параметры
text = "WELCOM TO SWIPE-ZINE \n AUTONOMUS WEB PAGE"
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
text_color = (255, 20, 147)  # яркий розово-фиолетовый неон
bg_color = (10, 10, 20)
glow_color = (255, 0, 120)
width, height = 600, 150
frames = []

# Создание анимации с пульсацией яркости
for i in range(30):  # 30 кадров
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Плавное изменение интенсивности свечения (синусоида)
    glow_strength = (math.sin(i / 5) + 1) / 2  # от 0 до 1
    glow_intensity = int(150 + glow_strength * 100)

    # Нарисуем текст с "ореолом"
    text_pos = (width // 2 - 200, height // 2 - 30)
    glow = Image.new("RGB", (width, height), bg_color)
    gdraw = ImageDraw.Draw(glow)
    gdraw.text(text_pos, text, font=font, fill=(glow_color[0], glow_color[1], glow_color[2]))
    for _ in range(2):  # размываем несколько раз для эффекта свечения
        glow = glow.filter(ImageFilter.GaussianBlur(1))
    img = Image.blend(img, glow, glow_strength)

    # Сам текст — чуть ярче и с контуром
    draw.text(text_pos, text, font=font, fill=text_color)

    frames.append(img)

# Сохранение GIF
frames[0].save(
    "neon_sign.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0,
    optimize=True
)
