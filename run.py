from app import app
import config

app.config.from_object(config)

if __name__ == '__main__':
    app.run()
