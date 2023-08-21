from boot_framework.FrameInit import FrameInit


if __name__ == '__main__':
    app = FrameInit(__name__, __file__)
    app.init_frame()
    app.run()
