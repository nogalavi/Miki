from PictureChanger import *
from Renderer import *


def main():
    path = "/Users/nogalavi/Downloads/" + raw_input('Enter picture name (needs to be in downloads folder):')

    picture_changer = PictureChanger()
    try:
        picture_changer.change_picture(path)
    except IOError:
        return

    renderer = Renderer()
    renderer.render()

if __name__ == '__main__':
    main()