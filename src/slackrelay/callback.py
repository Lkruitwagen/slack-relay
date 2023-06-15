from slackrelay import schemas


def callback(event: schemas.RelayEvent) -> schemas.RelayResponse:
    # YOUR CODE HERE!

    return schemas.RelayResponse(message="200 - success")
