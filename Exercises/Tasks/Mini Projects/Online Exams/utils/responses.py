import json


def send_json(handler, data, status=200, headers=None):

    response = json.dumps(data).encode("utf-8")

    handler.send_response(status)

    handler.send_header(
        "Content-Type",
        "application/json"
    )

    handler.send_header(
        "Content-Length",
        str(len(response))
    )

    if headers:

        for key, value in headers.items():

            handler.send_header(
                key,
                value
            )

    handler.end_headers()

    handler.wfile.write(response)


def get_json_body(handler):

    content_length = int(
        handler.headers.get(
            "Content-Length",
            0
        )
    )

    body = handler.rfile.read(content_length)

    return json.loads(
        body.decode("utf-8")
    )