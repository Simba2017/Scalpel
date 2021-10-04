# (generated with --quick)

import collections
from typing import Annotated, Any, Callable, Generator, Iterable, List, Sized, Tuple, Type, TypeVar, Union

BLACKLIST: List[Version]
GITHUB_API: str
STAGES: List[str]
argparse: module
itertools: module
operator: module
requests: module
sys: module

_TVersion = TypeVar('_TVersion', bound=Version)
_Tnamedtuple__Version_major_minor_patch_stage_edition = TypeVar('_Tnamedtuple__Version_major_minor_patch_stage_edition', bound=namedtuple__Version_major_minor_patch_stage_edition)

class Version(namedtuple__Version_major_minor_patch_stage_edition):
    major_minor: Annotated[Tuple[Any, Any], 'property']
    order: Annotated[tuple, 'property']
    def __str__(self) -> str: ...
    @classmethod
    def parse(cls: Type[_TVersion], version) -> _TVersion: ...

class namedtuple__Version_major_minor_patch_stage_edition(tuple):
    __slots__ = ["edition", "major", "minor", "patch", "stage"]
    __dict__: collections.OrderedDict[str, Any]
    _fields: Tuple[str, str, str, str, str]
    edition: Any
    major: Any
    minor: Any
    patch: Any
    stage: Any
    def __getnewargs__(self) -> Tuple[Any, Any, Any, Any, Any]: ...
    def __getstate__(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __new__(cls: Type[_Tnamedtuple__Version_major_minor_patch_stage_edition], major, minor, patch, stage, edition) -> _Tnamedtuple__Version_major_minor_patch_stage_edition: ...
    def _asdict(self) -> collections.OrderedDict[str, Any]: ...
    @classmethod
    def _make(cls: Type[_Tnamedtuple__Version_major_minor_patch_stage_edition], iterable: Iterable, new = ..., len: Callable[[Sized], int] = ...) -> _Tnamedtuple__Version_major_minor_patch_stage_edition: ...
    def _replace(self: _Tnamedtuple__Version_major_minor_patch_stage_edition, **kwds) -> _Tnamedtuple__Version_major_minor_patch_stage_edition: ...

def get_default(versions) -> Any: ...
def get_github_releases(projects) -> List[Version]: ...
def get_latest_versions(versions, num = ...) -> list: ...
def get_versions(tags) -> Generator[Version, Any, None]: ...
def group_versions(versions) -> List[list]: ...
def main(argv = ...) -> None: ...
def namedtuple(typename: str, field_names: Union[str, Iterable[str]], *, verbose: bool = ..., rename: bool = ...) -> type: ...
def parse_args(argv) -> argparse.Namespace: ...
