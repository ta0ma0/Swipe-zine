import os
import base64

# Получаем все изображения в текущей папке
image_extensions = ('.png', '.jpg', '.jpeg', '.gif')
images = [f for f in os.listdir('.') if f.lower().endswith(image_extensions)]
images.sort()  # сортировка по имени

# Функция для конвертации изображения в Base64
def image_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Создание карточек с base64 изображениями
cards_html = ""
for img in images:
    ext = img.split('.')[-1].lower()
    mime = f"image/{'jpeg' if ext in ['jpg','jpeg'] else ext}"
    img_base64 = image_to_base64(img)
    cards_html += f'<div class="card"><img src="data:{mime};base64,{img_base64}" alt="{img}"></div>\n'

# HTML-шаблон с исправленным CSS и JS
html_template = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Swipe-zine</title>
<style>
  html, body {{
    margin: 0; padding: 0;
    overflow: hidden;
    font-family: sans-serif;
    background: #111;
    color: #fff;
  }}
  .container {{
    display: flex;
    height: 100vh;
    transition: transform 0.4s ease;
  }}
  .card {{
    flex: 0 0 100vw;
    min-width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
    background: #222;
    box-sizing: border-box;
  }}
  .card img {{
    max-width: 90%;
    max-height: 90%;
    border-radius: 12px;
  }}
  .nav {{
    position: absolute;
    top: 50%;
    width: 100%;
    display: flex;
    justify-content: space-between;
    transform: translateY(-50%);
    pointer-events: none;
  }}
  .nav button {{
    background: rgba(255,255,255,0.2);
    border: none;
    color: #fff;
    font-size: 2rem;
    padding: 0.5rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    pointer-events: all;
  }}
</style>
</head>
<body>

<div class="container">
{cards_html}
</div>

<div class="nav">
  <button id="prev">&#10094;</button>
  <button id="next">&#10095;</button>
</div>

<script>
let index = 0;
const container = document.querySelector('.container');
const total = {len(images)};

function updateSlide() {{
    const width = window.innerWidth;
    container.style.transform = `translateX(-${{index * width}}px)`;
}}

document.getElementById('next').onclick = () => {{
    index = (index + 1) % total;
    updateSlide();
}};
document.getElementById('prev').onclick = () => {{
    index = (index - 1 + total) % total;
    updateSlide();
}};

let startX = 0;
container.addEventListener('touchstart', e => startX = e.touches[0].clientX);
container.addEventListener('touchend', e => {{
    let endX = e.changedTouches[0].clientX;
    if(startX - endX > 50) index = (index + 1) % total;
    if(endX - startX > 50) index = (index - 1 + total) % total;
    updateSlide();
}});

window.addEventListener('resize', updateSlide);
</script>

</body>
</html>
"""

# Сохраняем файл
with open("Swipe-zine-file.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Готово! Файл 'Swipe-zine-file.html' создан. Откройте его в браузере.")
