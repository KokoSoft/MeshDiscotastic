"""
MeshBotastic
~~~~~~~~~~~~~~~~~~~

A basic extensible bot for Meshtastic network.

:copyright: (c) 2026-present KokoSoft
:license: MIT
"""
from typing import Literal, NamedTuple

__title__ = 'MeshBotastic'
__author__ = 'KokoSoft'
__license__ = 'MIT'
__copyright__ = 'Copyright 2026-present KokoSoft'
__version__ = '1.0.0a'

class _VersionInfo(NamedTuple):
	major: int
	minor: int
	micro: int
	releaselevel: Literal['alpha', 'beta', 'candidate', 'final']
	serial: int

version_info: _VersionInfo = _VersionInfo(major = 1, minor = 0, micro=0, releaselevel='alpha', serial=0)

del NamedTuple, _VersionInfo
