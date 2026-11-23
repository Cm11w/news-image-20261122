#!/usr/bin/env python3
"""Draw the news-image-20261122 entry: one 1024x1024 PNG summarising
Sunday 22 November 2026 world news (refreshed Monday 23 Nov ~07:00 WIB,
after 22 Nov ended UTC — see research-22nov.md, section "REFRESH — HASIL").

Layout: dark masthead, one full-width lead story, a 2x2 grid of four
more stories, one-line source footer. All text is ASCII only (the
minus sign is the plain hyphen "-"); any text that would overflow its
card aborts the run with an error instead of drawing outside it.

Deterministic: fixed fonts, fixed layout, no timestamps, so two runs
produce byte-identical PNG output.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(HERE, "entry.png")

W, H = 1024, 1024

# ---- palette ------------------------------------------------------------
PAPER = (247, 243, 236)      # warm off-white page
INK = (22, 26, 34)           # near-black text
NAVY = (20, 33, 61)          # masthead band
NAVY_LINE = (232, 184, 75)   # gold rule under masthead
GOLD = (232, 184, 75)        # date colour on navy
CARD = (255, 255, 255)       # story cards
CARD_EDGE = (214, 206, 192)  # card border
MUTED = (96, 100, 110)       # secondary text
RED = (178, 34, 34)          # WAR accent
BLUE = (24, 78, 140)         # MARKETS accent
BROWN = (122, 74, 18)        # MIDDLE EAST accent
GREEN = (34, 110, 52)        # CLIMATE accent
PURPLE = (88, 44, 120)       # CYBER accent (unused after refresh)
TEAL = (13, 110, 109)        # GULF accent
WHITE = (255, 255, 255)
LIGHT = (205, 212, 224)      # masthead subline

FONT_DIR = "/usr/share/fonts/truetype/noto"


def load_font(name, size):
    path = os.path.join(FONT_DIR, name)
    if not os.path.exists(path):
        raise SystemExit("missing font: %s" % path)
    return ImageFont.truetype(path, size)


F_TITLE = None   # set in main()
F_DATE = None
F_KICKER = None
F_SUB = None
F_TAG = None
F_HEAD = None
F_HEAD_SM = None
F_BODY = None
F_BODY_SM = None
F_FOOT = None


def check_ascii(text, where):
    for ch in text:
        if ord(ch) > 127:
            raise SystemExit("non-ASCII char %r in %s" % (ch, where))
    if "\u2212" in text:
        raise SystemExit("U+2212 minus sign found in %s" % where)


def wrap(draw, text, font, max_w):
    """Greedy word wrap; aborts if a single word is wider than max_w."""
    words = text.split(" ")
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if not cur:
                raise SystemExit("word too wide for its box: %r" % word)
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, text, font, x, y, max_w, max_lines, line_h, fill):
    """Draw wrapped text; abort if it needs more than max_lines lines."""
    lines = wrap(draw, text, font, max_w)
    if len(lines) > max_lines:
        raise SystemExit(
            "text overflow: %d lines > %d allowed: %r"
            % (len(lines), max_lines, text[:60])
        )
    for i, line in enumerate(lines):
        draw.text((x, y + i * line_h), line, font=font, fill=fill)
    return y + len(lines) * line_h


def tag_chip(draw, x, y, label, colour):
    """Small filled tag chip; returns width used."""
    pad_x, pad_y = 10, 5
    w = int(draw.textlength(label, font=F_TAG)) + 2 * pad_x
    h = F_TAG.size + 2 * pad_y
    draw.rounded_rectangle([x, y, x + w, y + h], radius=4, fill=colour)
    draw.text((x + pad_x, y + pad_y - 1), label, font=F_TAG, fill=WHITE)
    return w, h


def draw_lead(draw, box):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=CARD,
                           outline=CARD_EDGE, width=2)
    # green accent bar on the left edge
    draw.rounded_rectangle([x0, y0, x0 + 10, y1], radius=5, fill=GREEN)
    inner_x = x0 + 28
    inner_w = x1 - inner_x - 24
    y = y0 + 16
    tag_w, tag_h = tag_chip(draw, inner_x, y, "CLIMATE - COP31", GREEN)
    draw.text((inner_x + tag_w + 12, y + 1),
              "Antalya - summit ends with no deal",
              font=F_SUB, fill=MUTED)
    y += tag_h + 12
    head = "COP31 collapses with no deal at all"
    y = draw_wrapped(draw, head, F_HEAD, inner_x, y, inner_w, 2, 42, INK)
    y += 8
    body = (
        "The summit in Antalya ended on Sunday after the EU and others "
        "rejected a final text with no mention of fossil fuels; the "
        "president conceded there was no agreement."
    )
    y = draw_wrapped(draw, body, F_BODY, inner_x, y, inner_w, 3, 26, INK)
    y += 6
    body2 = (
        "It is the longest COP ever and the first to end with no deal "
        "since 2000. UN chief Guterres called the outcome deeply "
        "disappointing."
    )
    y = draw_wrapped(draw, body2, F_BODY, inner_x, y, inner_w, 3, 26, INK)
    if y > y1 - 12:
        raise SystemExit("lead card overflow: text bottom %d > %d" % (y, y1 - 12))


def draw_panel(draw, box, tag, colour, head, body):
    x0, y0, x1, y1 = box
    draw.rounded_rectangle([x0, y0, x1, y1], radius=10, fill=CARD,
                           outline=CARD_EDGE, width=2)
    draw.rectangle([x0 + 12, y0, x1 - 12, y0 + 5], fill=colour)
    inner_x = x0 + 20
    inner_w = x1 - inner_x - 20
    y = y0 + 14
    tag_w, tag_h = tag_chip(draw, inner_x, y, tag, colour)
    y += tag_h + 8
    y = draw_wrapped(draw, head, F_HEAD_SM, inner_x, y, inner_w, 2, 32, INK)
    y += 5
    y = draw_wrapped(draw, body, F_BODY_SM, inner_x, y, inner_w, 4, 24,
                     (52, 56, 66))
    if y > y1 - 8:
        raise SystemExit("panel %s overflow: text bottom %d > %d"
                         % (tag, y, y1 - 8))


def main():
    global F_TITLE, F_DATE, F_KICKER, F_SUB, F_TAG
    global F_HEAD, F_HEAD_SM, F_BODY, F_BODY_SM, F_FOOT

    F_TITLE = load_font("NotoSans-Bold.ttf", 66)
    F_DATE = load_font("NotoSans-Bold.ttf", 34)
    F_KICKER = load_font("NotoSans-Bold.ttf", 20)
    F_SUB = load_font("NotoSans-Regular.ttf", 19)
    F_TAG = load_font("NotoSans-Bold.ttf", 18)
    F_HEAD = load_font("NotoSans-Bold.ttf", 34)
    F_HEAD_SM = load_font("NotoSans-Bold.ttf", 25)
    F_BODY = load_font("NotoSans-Regular.ttf", 20)
    F_BODY_SM = load_font("NotoSans-Regular.ttf", 18)
    F_FOOT = load_font("NotoSans-Regular.ttf", 16)

    texts = [
        "THE WORLD IN ONE IMAGE",
        "WORLD NEWS",
        "Sunday, November 22, 2026",
        "Top stories of the day - as reported on Sunday",
    ]
    for t in texts:
        check_ascii(t, "masthead")

    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- masthead -------------------------------------------------------
    mast_h = 172
    draw.rectangle([0, 0, W, mast_h], fill=NAVY)
    draw.rectangle([0, mast_h - 4, W, mast_h], fill=NAVY_LINE)
    draw.text((36, 18), "THE WORLD IN ONE IMAGE",
              font=F_KICKER, fill=GOLD)
    draw.text((36, 46), "WORLD NEWS", font=F_TITLE, fill=WHITE)
    draw.text((36, 122), "Sunday, November 22, 2026",
              font=F_DATE, fill=GOLD)
    sub = "Top stories of the day - as reported on Sunday"
    sub_w = draw.textlength(sub, font=F_SUB)
    kicker_w = draw.textlength("THE WORLD IN ONE IMAGE", font=F_KICKER)
    if W - 36 - sub_w < 36 + kicker_w + 24:
        raise SystemExit("masthead subline collides with kicker")
    draw.text((W - 36 - sub_w, 20), sub, font=F_SUB, fill=LIGHT)

    # ---- lead story -----------------------------------------------------
    draw_lead(draw, (36, 192, W - 36, 476))

    # ---- 2x2 grid --------------------------------------------------------
    gx0, gy0 = 36, 490
    gw = (W - 72 - 16) // 2
    gh = 220
    panels = [
        ("WAR", RED,
         "Drone collapses block near Kyiv",
         "A Russian drone hit a five-storey block in Dymer, near Kyiv, "
         "on Sunday; at least 14 people are missing, Zelensky said. "
         "Russia fired 3 missiles and 148 drones overnight, Kyiv said."),
        ("MIDDLE EAST", BROWN,
         "Israeli strike kills 3 in Gaza",
         "Three people were killed in Gaza City on Saturday, the Gaza "
         "Health Ministry said. Israel said it hit Islamic Jihad "
         "militants in a truck with a WCK logo; WCK said it was not "
         "its vehicle."),
        ("GULF", TEAL,
         "Iran strikes US bases in Bahrain",
         "Iran said it fired missiles and drones at US Patriot radars "
         "at two bases on Saturday night. Bahrain said a civilian site "
         "was hit, two hurt; the US said its forces were unharmed."),
        ("MARKETS", BLUE,
         "Bitcoin rebounds past $61,000",
         "Bitcoin fell to $55,830 on Friday, its lowest since September "
         "2024. It rose 8% on Saturday and past $61,000 on Sunday, "
         "after $2.4bn in futures were liquidated."),
    ]
    for i, (tag, colour, head, body) in enumerate(panels):
        check_ascii(head, "panel head " + tag)
        check_ascii(body, "panel body " + tag)
        col = i % 2
        row = i // 2
        x0 = gx0 + col * (gw + 16)
        y0 = gy0 + row * (gh + 14)
        draw_panel(draw, (x0, y0, x0 + gw, y0 + gh),
                   tag, colour, head, body)

    # ---- footer ----------------------------------------------------------
    foot = ("Sources: Reuters - AP - UN News - Al Jazeera - IBTimes  |  "
            "Reported Sunday, Nov 22, 2026")
    check_ascii(foot, "footer")
    fw = draw.textlength(foot, font=F_FOOT)
    if fw > W - 72:
        raise SystemExit("footer too wide: %d" % fw)
    draw.text(((W - fw) / 2, 958), foot, font=F_FOOT, fill=MUTED)

    img.save(OUT_PATH, format="PNG", optimize=True)
    print("wrote %s (%dx%d)" % (OUT_PATH, W, H))


if __name__ == "__main__":
    main()
