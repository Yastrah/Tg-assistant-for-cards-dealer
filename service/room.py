import logging
import string
import random

from .database import read_data, write_data


logger = logging.getLogger(__name__)


def generate_id(length=5):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
    # while True:
    #         id = ''.join(random.choice(characters) for _ in range(length))
    #         if id not in generated_ids:
    #             generated_ids.add(id)
    #             return id


async def create_room(name: str, owner_id: int) -> str:
    try:
        data = await read_data("rooms")
        id = generate_id()
        data.append(dict(
            name=name,
            owner_id=owner_id,
            room_id=id,
            members=[owner_id]
        ))
        await write_data("rooms", data)
        return id
    except:
        return None


