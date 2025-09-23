import segno
from PIL import Image, ImageDraw
from io import BytesIO
from pathlib import Path
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel

class QQrViz(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__("No QR Generated", *args, **kwargs)

    def _up_coords(self, size):
        w, h = size
        greater = max(w, h)
        r = greater + (10 - (greater % 10))
        return (r, r)
    
    def _overlay_image(self, buf: BytesIO, logo_file: Path):
        buf.seek(0)

        img = Image.open(buf)
        img = img.convert('RGBA')
        img_width, img_height = img.size
        logo_max_size = img_height // 3

        logo_img = Image.open(logo_file)
        logo_img.thumbnail((logo_max_size, logo_max_size), Image.Resampling.BICUBIC)

        circ_img = Image.new("RGBA", self._up_coords(logo_img.size))
        circ_draw = ImageDraw.Draw(circ_img)
        w, h = circ_img.size
        circ_draw.circle((w / 2, h / 2), radius=w / 2, fill="white")

        box = ((w - logo_img.size[0]) // 2, (h - logo_img.size[1]) // 2)
        box2 = ((img_width - circ_img.size[0]) // 2, (img_height - circ_img.size[1]) // 2)

        circ_img.alpha_composite(logo_img, box)
        img.alpha_composite(circ_img, box2)

        img_buffer = BytesIO()

        img.save(img_buffer, format="PNG")

        return img_buffer


    def regen_preview(self, content, light, dark, logo_file):
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=9)
        
        pix = QPixmap()

        if logo_file:
            img_buf = self._overlay_image(buf, logo_file)
            pix.loadFromData(img_buf.getvalue())
        else:
            pix.loadFromData(buf.getvalue())
        
        self.clear()
        self.setPixmap(pix)

    def create_image(self, content, light, dark, logo_file, scale):
        buf = BytesIO()
        qrc = segno.make(content, error='H', micro=False)
        qrc.save(buf, kind="png", dark=dark, light=light, scale=scale)

        if logo_file:
            img_buf = self._overlay_image(buf, logo_file)
            return img_buf.getvalue()

        return buf.getvalue()
