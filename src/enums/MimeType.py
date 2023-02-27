from enum import Flag, auto


class MimeType(Flag):
    image_jpeg = auto()
    image_png = auto()
    application_pdf = auto()
