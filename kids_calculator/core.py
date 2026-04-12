import math
from typing import List

class Calculator:
    def __init__(self):
        self.history: List[str] = []
        self.memory: float = 0.0
        self.angle_mode: str = "deg"

    def set_angle_mode(self, mode: str):
        if mode.lower() in ("deg", "rad"):
            self.angle_mode = mode.lower()

    def get_safe_dict(self):
        is_deg = self.angle_mode == "deg"

        def make_trig(func, inverse=False):
            if inverse:
                def wrapper(x): 
                    res = func(x)
                    return math.degrees(res) if is_deg else res
                return wrapper
            else:
                def wrapper(x):
                    arg = math.radians(x) if is_deg else x
                    return func(arg)
                return wrapper

        return {
            "sin": make_trig(math.sin), "cos": make_trig(math.cos), "tan": make_trig(math.tan),
            "asin": make_trig(math.asin, True), "acos": make_trig(math.acos, True), "atan": make_trig(math.atan, True),
            "sqrt": math.sqrt, "log": math.log, "log10": math.log10, "exp": math.exp,
            "factorial": math.factorial, "pi": math.pi, "e": math.e,
            "abs": abs, "round": round, "pow": pow,
        }

    def calculate(self, expression: str) -> float:
        if not expression.strip():
            raise ValueError("Empty expression")
        try:
            result = eval(expression, {"__builtins__": {}}, self.get_safe_dict())
            result = round(float(result), 8)
            self.history.append(f"{expression} = {result}")
            if len(self.history) > 20:
                self.history.pop(0)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def get_history(self):
        return self.history[::-1]