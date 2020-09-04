from helpers.push_id import PushID


def fancy_id_generator() -> str:
    """A function to generate unique identifiers on insert."""
    push_id = PushID()
    return push_id.next_id()
