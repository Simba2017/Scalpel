# (generated with --quick)

from typing import Any, Dict

doctest: module

class Provider:
    msg_queue: list
    subscribers: Dict[Any, list]
    def __init__(self) -> None: ...
    def notify(self, msg) -> None: ...
    def subscribe(self, msg, subscriber) -> None: ...
    def unsubscribe(self, msg, subscriber) -> None: ...
    def update(self) -> None: ...

class Publisher:
    provider: Any
    def __init__(self, msg_center) -> None: ...
    def publish(self, msg) -> None: ...

class Subscriber:
    name: Any
    provider: Any
    def __init__(self, name, msg_center) -> None: ...
    def run(self, msg) -> None: ...
    def subscribe(self, msg) -> None: ...
    def unsubscribe(self, msg) -> None: ...

def main() -> None: ...
