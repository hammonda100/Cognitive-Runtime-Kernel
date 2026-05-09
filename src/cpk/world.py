class WorldInterface:
    def call(self, tool_name, **kwargs):
        if tool_name == "calc":
            a = kwargs.get("a", 0)
            b = kwargs.get("b", 0)
            op = kwargs.get("op", "+")

            if op == "+":
                return {"result": a + b}

        return {"error": "unknown tool"}
