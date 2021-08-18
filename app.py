from controllers import app
import awsgi


def lambda_handler(event, context):
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run()
