from frame.App import AppContainer


if __name__ == '__main__':
    AppContainer(
        __name__, __file__
    ).init_frame().run(
        host='0.0.0.0',
        port=8082,
        debug=True
    )
