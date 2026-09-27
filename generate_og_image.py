import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

W, H = 1200, 630

# 1. Base background: warm marigold and golden bokeh from footer-bg.jpg
bg_file = 'editable/assets/footer-bg.jpg'
if os.path.exists(bg_file):
    raw_bg = Image.open(bg_file).convert('RGB')
    # Resize & crop to 1200x630
    bg = ImageOps.fit(raw_bg, (W, H), method=Image.Resampling.LANCZOS)
    # Subtle blur for depth
    bg = bg.filter(ImageFilter.GaussianBlur(2.5))
else:
    bg = Image.new('RGB', (W, H), (30, 14, 10))

# 2. Rich royal dark overlay (deep burgundy / dark chocolate vignette)
overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ov_draw = ImageDraw.Draw(overlay)

# Gradient overlay from left to right (left 75% dark, right 88% dark for crystal-clear readability)
for x in range(W):
    # Ratio 0 to 1
    t = x / W
    # Left opacity ~185, right opacity ~225
    alpha = int(185 + t * 40)
    # Deep warm brown/charcoal
    r, g, b = int(24 - t * 8), int(12 - t * 4), int(8 - t * 3)
    ov_draw.line([(x, 0), (x, H)], fill=(r, g, b, alpha))

bg = Image.alpha_composite(bg.convert('RGBA'), overlay)

# 3. Double royal gold hairline outer frame with corner accents
frame_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
f_draw = ImageDraw.Draw(frame_layer)

GOLD_DARK   = (160, 120, 50, 220)
GOLD_MID    = (212, 175, 80, 240)
GOLD_LIGHT  = (248, 220, 140, 255)
GOLD_BRIGHT = (255, 242, 195, 255)

# Outer and inner border rects
inset1 = 18
inset2 = 24
f_draw.rectangle([(inset1, inset1), (W - inset1, H - inset1)], outline=GOLD_MID, width=1)
f_draw.rectangle([(inset2, inset2), (W - inset2, H - inset2)], outline=GOLD_DARK, width=1)

# Corner floral / diamond accents
def draw_corner_ornament(draw, cx, cy):
    # Diamond at corner
    d = 5
    draw.polygon([(cx, cy - d), (cx + d, cy), (cx, cy + d), (cx - d, cy)], fill=GOLD_LIGHT, outline=GOLD_MID)
    # Small cross accents
    draw.line([(cx - 10, cy), (cx - 6, cy)], fill=GOLD_MID, width=1)
    draw.line([(cx + 6, cy), (cx + 10, cy)], fill=GOLD_MID, width=1)
    draw.line([(cx, cy - 10), (cx, cy - 6)], fill=GOLD_MID, width=1)
    draw.line([(cx, cy + 6), (cx, cy + 10)], fill=GOLD_MID, width=1)

draw_corner_ornament(f_draw, inset1 + 3, inset1 + 3)
draw_corner_ornament(f_draw, W - inset1 - 3, inset1 + 3)
draw_corner_ornament(f_draw, inset1 + 3, H - inset1 - 3)
draw_corner_ornament(f_draw, W - inset1 - 3, H - inset1 - 3)

bg = Image.alpha_composite(bg, frame_layer)

# 4. Couple Photo Frame on Left (Royal Arched Frame)
fx, fy = 55, 48
fw, fh = 430, 534

# Prepare couple photo
couple_img = Image.open('editable/assets/photo-together.jpg').convert('RGB')
crop_box = (15, 140, 765, 980)
cropped_couple = couple_img.crop(crop_box)
couple_resized = cropped_couple.resize((fw, fh), Image.Resampling.LANCZOS)

# Create Arch Mask (straight bottom, arched top)
arch_mask = Image.new('L', (fw, fh), 0)
m_draw = ImageDraw.Draw(arch_mask)

# Top arch is a semicircle or rounded arch with radius fw // 2
arch_r = fw // 2
# Top circle
m_draw.pieslice([(0, 0), (fw, fw)], 180, 360, fill=255)
# Bottom rectangle with rounded corners at base
bot_r = 16
m_draw.rounded_rectangle([(0, arch_r), (fw, fh)], radius=bot_r, fill=255)

# Soft Drop Shadow behind couple arch
shadow = Image.new('RGBA', (W, H), (0, 0, 0, 0))
s_draw = ImageDraw.Draw(shadow)
# Draw shadow shape
s_draw.pieslice([(fx + 8, fy + 12), (fx + fw + 8, fy + fw + 12)], 180, 360, fill=(0, 0, 0, 180))
s_draw.rounded_rectangle([(fx + 8, fy + arch_r + 12), (fx + fw + 8, fy + fh + 12)], radius=bot_r, fill=(0, 0, 0, 180))
shadow = shadow.filter(ImageFilter.GaussianBlur(14))
bg = Image.alpha_composite(bg, shadow)

# Paste arched couple photo
photo_arched = Image.new('RGBA', (fw, fh), (0, 0, 0, 0))
photo_arched.paste(couple_resized, (0, 0), arch_mask)
bg.paste(photo_arched, (fx, fy), photo_arched)

# Draw royal gold multi-tier border over the arched photo
arch_border = Image.new('RGBA', (W, H), (0, 0, 0, 0))
ab_draw = ImageDraw.Draw(arch_border)

# Multi-line arch strokes for luxury framing
for i, col in enumerate([
    (150, 110, 45, 230),
    (215, 175, 75, 255),
    (250, 225, 140, 255),
    (215, 175, 75, 255),
    (140, 100, 40, 200)
]):
    off = i - 2
    # Arch outline
    ab_draw.arc([(fx + off, fy + off), (fx + fw - off, fy + fw - off)], 180, 360, fill=col, width=1)
    # Left and right vertical borders
    ab_draw.line([(fx + off, fy + arch_r), (fx + off, fy + fh - bot_r)], fill=col, width=1)
    ab_draw.line([(fx + fw - off, fy + arch_r), (fx + fw - off, fy + fh - bot_r)], fill=col, width=1)
    # Bottom border
    ab_draw.arc([(fx + off, fy + fh - 2 * bot_r + off), (fx + 2 * bot_r - off, fy + fh - off)], 90, 180, fill=col, width=1)
    ab_draw.arc([(fx + fw - 2 * bot_r + off, fy + fh - 2 * bot_r + off), (fx + fw - off, fy + fh - off)], 0, 90, fill=col, width=1)
    ab_draw.line([(fx + bot_r, fy + fh - off), (fx + fw - bot_r, fy + fh - off)], fill=col, width=1)

# Subtle inner inset gold hairline
inset_off = 6
ab_draw.arc([(fx + inset_off, fy + inset_off), (fx + fw - inset_off, fy + fw - inset_off)], 180, 360, fill=(245, 215, 130, 130), width=1)
ab_draw.line([(fx + inset_off, fy + arch_r), (fx + inset_off, fy + fh - bot_r)], fill=(245, 215, 130, 130), width=1)
ab_draw.line([(fx + fw - inset_off, fy + arch_r), (fx + fw - inset_off, fy + fh - bot_r)], fill=(245, 215, 130, 130), width=1)
ab_draw.line([(fx + bot_r, fy + fh - inset_off), (fx + fw - bot_r, fy + fh - inset_off)], fill=(245, 215, 130, 130), width=1)

bg = Image.alpha_composite(bg, arch_border)

# 5. Right Typography Section
draw = ImageDraw.Draw(bg)

rx_start = 520
rx_end = 1150
rx_center = (rx_start + rx_end) // 2

# Fonts
font_onkar = ImageFont.truetype(r'C:\Windows\Fonts\Nirmala.ttc', 34)
font_onkar_sub = ImageFont.truetype(r'C:\Windows\Fonts\Nirmala.ttc', 16)
font_badge_tag = ImageFont.truetype('fonts/Cinzel-Bold.ttf', 13)
font_couple = ImageFont.truetype('fonts/GreatVibes-Regular.ttf', 62)
font_amp = ImageFont.truetype('fonts/PlayfairDisplay-Italic.ttf', 38)
font_fullnames = ImageFont.truetype('fonts/PlayfairDisplay-Italic.ttf', 16)
font_date_badge = ImageFont.truetype('fonts/Cinzel-Bold.ttf', 17)
font_event_title = ImageFont.truetype('fonts/Cinzel-Bold.ttf', 13)
font_event_venue = ImageFont.truetype('fonts/PlayfairDisplay-Italic.ttf', 15)
font_compliments = ImageFont.truetype('fonts/PlayfairDisplay-Italic.ttf', 13)
font_url = ImageFont.truetype('fonts/Cinzel-Bold.ttf', 12)

# A. Ik Onkar and Sacred Shabad Header
y_onkar = 54
# Soft glow behind Ik Onkar
draw.text((rx_center + 1, y_onkar + 1), "ੴ", font=font_onkar, fill=(30, 10, 5), anchor="mm")
draw.text((rx_center, y_onkar), "ੴ", font=font_onkar, fill=GOLD_BRIGHT, anchor="mm")

# Decorative dividers flanking Ik Onkar
div_len = 110
draw.line([(rx_center - div_len - 30, y_onkar), (rx_center - 30, y_onkar)], fill=GOLD_MID, width=1)
draw.line([(rx_center + 30, y_onkar), (rx_center + div_len + 30, y_onkar)], fill=GOLD_MID, width=1)
# Small gold diamond on each side
for side in [-1, 1]:
    dx = rx_center + side * 30
    draw.polygon([(dx, y_onkar - 4), (dx + 4, y_onkar), (dx, y_onkar + 4), (dx - 4, y_onkar)], fill=GOLD_LIGHT)

# Punjabi Shabad blessing line
y_shabad = 85
draw.text((rx_center, y_shabad), "ਲਖ ਖੁਸੀਆ ਪਾਤਿਸਾਹੀਆ ਜੇ ਸਤਿਗੁਰੁ ਨਦਰਿ ਕਰੇਇ ॥", font=font_onkar_sub, fill=(245, 225, 175), anchor="mm")

# Header Tagline
y_tag = 116
draw.text((rx_center, y_tag), "SACRED WEDDING CELEBRATION", font=font_badge_tag, fill=GOLD_LIGHT, anchor="mm")

# Elegant Gold Flourish Divider
flourish_path = 'editable/assets/gold-flourish.png'
if os.path.exists(flourish_path):
    fl = Image.open(flourish_path).convert('RGBA')
    # Resize flourish to width ~220
    fl_w = 220
    fl_h = int(fl.height * (fl_w / fl.width))
    fl = fl.resize((fl_w, fl_h), Image.Resampling.LANCZOS)
    bg.paste(fl, (rx_center - fl_w // 2, 132), fl)
    y_couple_start = 186
else:
    # Fallback decorative line with diamond
    draw.line([(rx_center - 130, 142), (rx_center + 130, 142)], fill=GOLD_MID, width=1)
    y_couple_start = 182

# B. Couple Names: Dalwinder & Hardeep
# Shadow effect for names
y_name1 = y_couple_start
draw.text((rx_center + 2, y_name1 + 2), "Dalwinder", font=font_couple, fill=(15, 6, 4), anchor="mm")
draw.text((rx_center, y_name1), "Dalwinder", font=font_couple, fill=GOLD_BRIGHT, anchor="mm")

y_amp = y_name1 + 44
draw.text((rx_center + 1, y_amp + 1), "&", font=font_amp, fill=(20, 8, 5), anchor="mm")
draw.text((rx_center, y_amp), "&", font=font_amp, fill=GOLD_LIGHT, anchor="mm")

y_name2 = y_amp + 44
draw.text((rx_center + 2, y_name2 + 2), "Hardeep", font=font_couple, fill=(15, 6, 4), anchor="mm")
draw.text((rx_center, y_name2), "Hardeep", font=font_couple, fill=GOLD_BRIGHT, anchor="mm")

# Full Names
y_full = y_name2 + 42
draw.text((rx_center, y_full), "Dalwinder Kaur Sidhu   ·   Hardeep Singh Dhaliwal", font=font_fullnames, fill=(245, 230, 205), anchor="mm")

# C. Date Badge
y_badge = y_full + 46
bw, bh = 390, 36
bx0 = rx_center - bw // 2
by0 = y_badge - bh // 2
bx1 = rx_center + bw // 2
by1 = y_badge + bh // 2

# Badge background & golden border
draw.rounded_rectangle([(bx0, by0), (bx1, by1)], radius=18, fill=(22, 11, 7, 240), outline=GOLD_MID, width=1)
draw.rounded_rectangle([(bx0 + 3, by0 + 3), (bx1 - 3, by1 - 3)], radius=15, outline=(140, 105, 45, 160), width=1)
draw.text((rx_center, y_badge), "SUNDAY, 1ST NOVEMBER 2026", font=font_date_badge, fill=GOLD_LIGHT, anchor="mm")

# D. Key Ceremonies & Venues
y_ev1 = y_badge + 38
draw.text((rx_center, y_ev1), "ANAND KARAJ (LAVAAN)  ·  7:00 AM", font=font_event_title, fill=GOLD_MID, anchor="mm")
draw.text((rx_center, y_ev1 + 18), "Gurudwara Sri Guru Hargobind Sahib Ji, Bhaini (Bathinda)", font=font_event_venue, fill=(245, 235, 220), anchor="mm")

y_ev2 = y_ev1 + 44
draw.text((rx_center, y_ev2), "BARAT WELCOME & RECEPTION  ·  11:30 AM", font=font_event_title, fill=GOLD_MID, anchor="mm")
draw.text((rx_center, y_ev2 + 18), "The Grand Venice Resort, Barnala Road, Bhadaur", font=font_event_venue, fill=(245, 235, 220), anchor="mm")

# E. Bottom Divider, Blessings, & Production Link
y_bot_div = y_ev2 + 38
draw.line([(rx_center - 180, y_bot_div), (rx_center + 180, y_bot_div)], fill=(150, 110, 45, 200), width=1)
# Small center diamond on divider
draw.polygon([(rx_center, y_bot_div - 3), (rx_center + 4, y_bot_div), (rx_center, y_bot_div + 3), (rx_center - 4, y_bot_div)], fill=GOLD_LIGHT)

y_url = y_bot_div + 20
draw.text((rx_center, y_url), "dalwinder-weds-hardeep.invitingyou.top", font=font_url, fill=GOLD_LIGHT, anchor="mm")

# Convert to RGB & Save
final_img = bg.convert('RGB')
final_img.save('editable/assets/og-image.jpg', quality=95, optimize=True)
final_img.save('assets/og-image.jpg', quality=95, optimize=True)
final_img.save('og-image.jpg', quality=95, optimize=True)

print("OG Image successfully generated and saved to:")
print("1. editable/assets/og-image.jpg")
print("2. assets/og-image.jpg")
print("3. og-image.jpg")
