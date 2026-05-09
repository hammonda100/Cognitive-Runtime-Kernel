from abc import ABC, abstractmethod


class CognitiveProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system: str | None = None,
        tools: list | None = None,
        memory: dict | None = None,
    ) -> str:
        ...
