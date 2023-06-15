from typing import Optional

from pydantic import BaseModel


class RelayEvent(BaseModel):
    type: Optional[str]
    user: Optional[str]
    text: Optional[str]
    ts: Optional[str]
    channel: Optional[str]
    event_ts: Optional[str]


class RelayOuter(BaseModel):
    token: str
    team_id: Optional[str]
    api_app_id: Optional[str]
    event: RelayEvent
    type: Optional[str]
    event_id: Optional[str]
    event_time: Optional[str]
    authed_users: Optional[str]


class RelayResponse(BaseModel):
    message: str


class Challenge(BaseModel):
    token: str
    challenge: str
    type: str


class ChallengeResponse(BaseModel):
    challenge: str
