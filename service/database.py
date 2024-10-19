# временно используется обычный JSON файл

import logging
import json
import aiofiles


logger = logging.getLogger(__name__)


async def read_data(file_path) -> list[dict]:
    file_path = f"../data/{file_path}.json"
    try:
        async with aiofiles.open(file_path, mode='r') as file:
            data = json.loads(await file.read())
            return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON data in file: {file_path}")
        return None

async def write_data(file_path, data) -> bool:
    file_path = f"../data/{file_path}.json"
    try:
        async with aiofiles.open(file_path, mode='w') as file:
            await file.write(json.dumps(data, indent=4))
            return True
    except Exception as e:
        logger.error(f"Error writing to file: {file_path} - {str(e)}")
        return False

# data = await read_data(file_path)
# await write_data(file_path, data)
