from PIL import Image


def hex_to_rgb(s):
    s = s.lstrip("#")
    return tuple([int(s[i:i + 2], 16) for i in range(0, 5, 2)])


def crab_alien(picture_name: str, file_for_save: str, **colors):
    img = Image.open(picture_name)
    img.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90).save('rotate_crab.png')
    img2 = Image.open('rotate_crab.png')
    for key, value in colors:


if __name__ == '__main__':
    crab_alien(
        'start_crab.png',
        'pythonProject3',
        fb97ab=(240, 221, 207),
        f6d9c5=(209, 151, 35),
        d9d9f8=(155, 216, 237),
    )
