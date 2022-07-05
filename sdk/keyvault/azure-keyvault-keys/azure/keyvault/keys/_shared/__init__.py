# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
try:
    import urllib.parse as parse
except ImportError:
    # pylint:disable=import-error
    import urlparse as parse  # type: ignore

from typing import TYPE_CHECKING
from .challenge_auth_policy import ChallengeAuthPolicy
from .client_base import KeyVaultClientBase
from .http_challenge import HttpChallenge
from . import http_challenge_cache

HttpChallengeCache = http_challenge_cache  # to avoid aliasing pylint error (C4745)

if TYPE_CHECKING:
    # pylint: disable=unused-import
    from typing import Optional


__all__ = [
    "ChallengeAuthPolicy",
    "HttpChallenge",
    "HttpChallengeCache",
    "KeyVaultClientBase",
]

class KeyVaultResourceId():
    """Represents a Key Vault identifier and its parsed contents.

    :param str source_id: The complete identifier received from Key Vault
    :param str vault_url: The vault URL
    :param str name: The name extracted from the ID
    :param str version: The version extracted from the ID
    """

    def __init__(
        self,
        source_id,  # type: str
        vault_url,  # type: str
        name,  # type: str
        version=None  # type: Optional[str]
    ):
        self.source_id = source_id
        self.vault_url = vault_url
        self.name = name
        self.version = version


def parse_key_vault_id(source_id):
    # type: (str) -> KeyVaultResourceId
    try:
        parsed_uri = parse.urlparse(source_id)
    except Exception:  # pylint: disable=broad-except
        raise ValueError("'{}' is not a valid ID".format(source_id))
    if not (parsed_uri.scheme and parsed_uri.hostname):
        raise ValueError("'{}' is not a valid ID".format(source_id))

    path = list(filter(None, parsed_uri.path.split("/")))

    if len(path) < 2 or len(path) > 3:
        raise ValueError("'{}' is not a valid ID".format(source_id))

    vault_url = "{}://{}".format(parsed_uri.scheme, parsed_uri.hostname)
    if parsed_uri.port:
        vault_url += f":{parsed_uri.port}"

    return KeyVaultResourceId(
        source_id=source_id,
        vault_url=vault_url,
        name=path[1],
        version=path[2] if len(path) == 3 else None,
    )


try:
    # pylint:disable=unused-import
    from .async_challenge_auth_policy import AsyncChallengeAuthPolicy
    from .async_client_base import AsyncKeyVaultClientBase

    __all__.extend(["AsyncChallengeAuthPolicy", "AsyncKeyVaultClientBase"])
except (SyntaxError, ImportError):
    pass
