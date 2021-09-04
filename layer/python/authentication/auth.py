import json
import requests


def get_user_details(conn, headers):
    return requests.get(conn + "/auth/get_user", headers=headers)


def authenticated(connectionurl):
    def check_authenticated(func):
        def wrapper(event, context):
            user_details = get_user_details(connectionurl, event['headers'])
            if user_details.status_code >= 300:
                return {
                    'statusCode': user_details.status_code,
                    'body': 'Not Authorized'
                }
            context.user_details = json.loads(user_details.content)
            return func(event, context)

        return wrapper

    return check_authenticated
