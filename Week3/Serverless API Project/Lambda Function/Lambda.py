import json

tasks = [
    {"id":1,"title":"Learn AWS"},
    {"id":2,"title":"Finish Internship"}
]

def lambda_handler(event, context):

    method = event["requestContext"]["http"]["method"]

    if method == "GET":
        return {
            "statusCode":200,
            "body":json.dumps(tasks)
        }

    return {
        "statusCode":400,
        "body":"Unsupported Method"
    }
