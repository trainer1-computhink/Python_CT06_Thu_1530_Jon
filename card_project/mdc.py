from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import numpy as np
import math

WIDTH = 608
HEIGHT = 400


FRAMES = 150
FPS = 30
CLASS = "CT06"
DAY = "WED"
TIME = "1500"
STUDENT_NAME = "Z"
FOLDER_NAME = "card_project"
MESSAGE_ASSET_FILE = "blessing.png"
FLOATING_ASSET_FILE = "cloud.png"
MESSAGE_FONT_FILE = "Montserrat-Regular.ttf"
SUBMESSAGE_FONT_FILE = "Montserrat-Regular.ttf"
MESSAGE_FONT_SIZE = 50
SUBMESSAGE_FONT_SIZE= 25

message = "Happy Mother's Day"
sub_message = "Thank you for everything!"


message_asset_fullpath =  f"{FOLDER_NAME}/{MESSAGE_ASSET_FILE}"
floating_asset_fullpath =  f"{FOLDER_NAME}/{FLOATING_ASSET_FILE}"
image_file_name = f"{FOLDER_NAME}/{CLASS}_{DAY}_{TIME}_{STUDENT_NAME}_mothers_day_animation.mp4"

frames = []

font_big_file = f"{FOLDER_NAME}/{MESSAGE_FONT_FILE}"
font_small_file = f"{FOLDER_NAME}/{SUBMESSAGE_FONT_FILE}"
font_big = ImageFont.truetype(font_big_file, MESSAGE_FONT_SIZE)
font_small = ImageFont.truetype(font_small_file, SUBMESSAGE_FONT_SIZE)

# =========================
# ASSETS
# =========================

# BACKGROUND FLOATING IMAGE
# Replace "floating_asset.png" with your own image.
#
# VARIATIONS:
# Change (40, 40) to resize the image.
#
# Example:
# (20, 20) = smaller
# (40, 40) = normal
# (80, 80) = bigger

floating_asset_img = Image.open(
    floating_asset_fullpath
).convert("RGBA")

floating_asset_img = floating_asset_img.resize((40, 40))


# MESSAGE IMAGE
# Image shown beside the main message.
#
# VARIATIONS:
# Change (40, 40) to resize the image.

message_asset_img = Image.open(
    message_asset_fullpath
).convert("RGBA")

message_asset_img = message_asset_img.resize((40, 40))


def draw_floating_assets(img, frame):

    # =========================
    # FLOATING ASSET SETTINGS
    # =========================

    # Change this to increase/reduce number of floating images.
    #
    # Example:
    # 6  = fewer images
    # 12 = normal
    # 20 = crowded

    number_of_assets = 12

    # Distance between images.
    #
    # Smaller number:
    # images closer together
    #
    # Larger number:
    # images further apart

    spacing = 45

    # Floating speed.
    #
    # Smaller:
    # slower floating
    #
    # Larger:
    # faster floating

    speed = 4

    for i in range(number_of_assets):

        x = 50 + i * spacing
        y = HEIGHT - ((frame * speed + i * 25) % HEIGHT)

        img.paste(
            floating_asset_img,
            (x, y),
            floating_asset_img
        )


def draw_waterfall(draw, frame):

    # VARIATIONS:
    # Change 40 to create more/fewer water streams.
    # Change frame * 8 to control waterfall speed.
    # Change width=3 to make water thicker/thinner.

    for i in range(40):

        x = (i * 17) % WIDTH
        y = (frame * 8 + i * 30) % HEIGHT

        draw.line(
            (x, y, x, y + 35),
            fill="#7dd3fc",
            width=3
        )

        draw.ellipse(
            (x - 3, y + 35, x + 3, y + 41),
            fill="#bae6fd"
        )


def draw_sparkles(draw, frame):

    # VARIATIONS:
    # Change 20 to create more/fewer sparkles.
    # Change frame * 0.3 for sparkle speed.
    # Change "*" into ".", "+", or "x".

    for i in range(20):

        x = (i * 73) % WIDTH
        y = (i * 41) % HEIGHT

        brightness = int(
            150 + 100 * math.sin(frame * 0.3 + i)
        )

        color = (255, brightness, brightness)

        draw.text(
            (x, y),
            "*",
            fill=color,
            font=font_small
        )


def draw_sliding_message(
    img,
    draw,
    frame,
    asset_position="after"
):

    # =========================
    # MESSAGE SETTINGS
    # =========================

    # Controls how far the message slides.
    #
    # Larger:
    # message travels further
    #
    # Smaller:
    # shorter slide distance

    slide_distance = WIDTH + 350

    # Space between text and image.

    gap = 10

    progress = frame / FRAMES

    text_x = int(
        WIDTH - progress * slide_distance
    )

    text_y = 140

    draw.text(
        (text_x, text_y),
        message,
        fill="#7a1f44",
        font=font_big
    )

    text_bbox = draw.textbbox(
        (text_x, text_y),
        message,
        font=font_big
    )

    text_width = text_bbox[2] - text_bbox[0]

    if asset_position == "after":

        asset_x = text_x + text_width + gap

    elif asset_position == "before":

        asset_x = (
            text_x
            - message_asset_img.width
            - gap
        )

    else:

        asset_x = text_x + text_width + gap

    asset_y = text_y + 8

    img.paste(
        message_asset_img,
        (asset_x, asset_y),
        message_asset_img
    )


def draw_rotating_pulsing_flower(draw, frame):

    # VARIATIONS:
    #
    # Change 20:
    # normal flower size
    #
    # Change 8:
    # pulse strength
    #
    # Change frame * 0.2:
    # pulse speed
    #
    # Change rotation = frame * 5:
    # spin speed
    #
    # Change:
    # range(0, 360, 45)
    #
    # 45 = 8 petals
    # 30 = 12 petals
    # 60 = 6 petals

    size = 20 + int(
        8 * math.sin(frame * 0.2)
    )

    rotation = frame * 5

    center_x = WIDTH // 2
    center_y = 250

    for angle in range(0, 360, 45):

        rad = math.radians(
            angle + rotation
        )

        x = center_x + int(
            math.cos(rad) * size
        )

        y = center_y + int(
            math.sin(rad) * size
        )

        draw.ellipse(
            (x - 12, y - 12, x + 12, y + 12),
            fill="#ff8fab"
        )

    draw.ellipse(
        (
            center_x - 10,
            center_y - 10,
            center_x + 10,
            center_y + 10
        ),
        fill="#ffd166"
    )


def draw_subtitle(draw, frame):

    # VARIATIONS:
    #
    # Change frame > 45:
    # subtitle appears earlier/later
    #
    # Change 180, 310:
    # subtitle position

    if frame > 45:

        draw.text(
            (180, 310),
            sub_message,
            fill="#5c2a3d",
            font=font_small
        )


for frame in range(FRAMES):

    img = Image.new(
        "RGB",
        (WIDTH, HEIGHT),
        "#ffd6e8"
    )

    draw = ImageDraw.Draw(img)

    draw_waterfall(draw, frame)

    draw_floating_assets(img, frame)

    draw_sparkles(draw, frame)

    draw_sliding_message(
        img,
        draw,
        frame,
        asset_position="after"
    )

    draw_rotating_pulsing_flower(draw, frame)

    draw_subtitle(draw, frame)

    frames.append(np.array(img))

writer = imageio.get_writer(
    image_file_name,
    fps=FPS
)

for frame in frames:
    writer.append_data(frame)

writer.close()

print(f"MP4 created:{image_file_name}")
