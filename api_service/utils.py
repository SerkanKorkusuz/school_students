import uuid


def uuid_with_20() -> str:
    """
    Create an uuid string with 20 characters long
    :rtype: str
    """
    return str(uuid.uuid4())[:20]
