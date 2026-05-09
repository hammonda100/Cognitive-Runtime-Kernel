from .base import CognitiveProvider


class MockProvider(CognitiveProvider):

    async def generate(
        self,
        prompt,
        system=None,
        tools=None,
        memory=None,
    ):
        return f"[MOCK] {prompt}"
