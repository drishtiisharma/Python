import os


def serve_html(handler, base_dir, filename):

    filepath = os.path.join(
        base_dir,
        "templates",
        filename
    )

    if not os.path.exists(filepath):

        handler.send_error(
            404,
            "HTML file not found"
        )

        return

    with open(filepath, "rb") as file:
        content = file.read()

    handler.send_response(200)

    handler.send_header(
        "Content-Type",
        "text/html"
    )

    handler.send_header(
        "Content-Length",
        str(len(content))
    )

    handler.end_headers()

    handler.wfile.write(content)


def serve_static(handler, base_dir, filepath, content_type):

    full_path = os.path.join(
        base_dir,
        filepath
    )

    if not os.path.exists(full_path):

        handler.send_error(
            404,
            "File not found"
        )

        return

    with open(full_path, "rb") as file:
        content = file.read()

    handler.send_response(200)

    handler.send_header(
        "Content-Type",
        content_type
    )

    handler.send_header(
        "Content-Length",
        str(len(content))
    )

    handler.end_headers()

    handler.wfile.write(content)