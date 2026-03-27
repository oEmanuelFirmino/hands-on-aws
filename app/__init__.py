"""
Pacote principal da aplicação.

Responsável por expor a factory function `create_app`
para inicialização do FastAPI.
"""

from .main import app

__all__ = ["app"]
