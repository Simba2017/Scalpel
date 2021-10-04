# (generated with --quick)

import collections
from typing import Any, Dict, List, Optional, Type

OrderedDict: Type[collections.OrderedDict]

class Node:
    children: Dict[Any, Node]
    key: Any
    parent: Any
    terminates: bool
    def __init__(self, key, parent = ..., terminates = ...) -> None: ...

class Trie:
    root: Node
    def __init__(self) -> None: ...
    def _list_words(self, node, curr_word, result) -> None: ...
    def find(self, word) -> Optional[Node]: ...
    def insert(self, word) -> None: ...
    def list_words(self) -> List[str]: ...
    def remove(self, word) -> None: ...
