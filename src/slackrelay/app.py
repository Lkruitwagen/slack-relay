from typing import Union

from fastapi import FastAPI

from slackrelay import schemas
from slackrelay.callback import callback

app = FastAPI()


@app.post("/", response_model=Union[schemas.ChallengeResponse, schemas.RelayResponse])
async def main(event: Union[schemas.Challenge, schemas.RelayOuter]):
    print("EVENT", event)
    if event.type == "url_verification":
        return schemas.ChallengeResponse(challenge=event.challenge)
    else:
        return callback(event)
