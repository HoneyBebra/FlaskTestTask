from app import app
import config


# TODO: add tests (models, parser)
# TODO: deploy via docker, add instructions


def main():
    app.run(debug=config.FLASK_DEBUG, host=config.host, port=config.port)


if __name__ == '__main__':
    main()
