"""
STUB — This file is replaced by Kiota-generated code when you run:
  yarn sdk:generate

It exists so the package is importable before the first generation pass.
"""

from __future__ import annotations

from kiota_abstractions.request_adapter import RequestAdapter


class FormalingoClient:
    """Formalingo API client (Kiota-generated stub)."""

    def __init__(self, request_adapter: RequestAdapter) -> None:
        if not request_adapter:
            raise TypeError("request_adapter cannot be None")
        self.request_adapter = request_adapter
