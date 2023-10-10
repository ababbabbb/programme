from boot_framework.BootFrame import Frame


if __name__ == '__main__':
    Frame(
        __name__, __file__
    ).init_frame().run(
        host='0.0.0.0',
        port=8082,
        debug=True
    )
