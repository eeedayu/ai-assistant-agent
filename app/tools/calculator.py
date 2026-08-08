import ast
import operator 
from platform import node
from typing import Any, Union

from .base import BaseTool

Number = Union[int, float]


class CalculatorTool(BaseTool):

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return (
            "计算数学表达式，支持加、减、乘、除、"
            "乘方以及括号。例如：123 * 456"
        )

    def get_schema(self) -> dict[str, Any]:
        return {
            "type": "object",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": (
                                "需要计算的数学表达式，"
                                "例如 123 * 456"
                            ),
                        },
                    },
                    "required": ["expression"],
                    "additionalProperties": False,
                },
            }
        }

    def execute(self, expression: str) -> Number:
        if not expression:
            raise ValueError("Missing 'expression' parameter.")

        return self._calulate(expression)

    def _calulate(self, expression: str) -> Number:

        expression = expression.strip()
        if not expression:
            raise ValueError("Empty expression.")

        tree = ast.parse(expression, mode='eval')

        return self._eval_node(tree.body)

    def _eval_node(self, node: ast.AST) -> Number:

        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
        }

        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):
                return node.value
            else:
                raise ValueError(f"Unsupported constant type: {type(node.value)}")

        if isinstance(node, ast.BinOp):

            operator_type = type(node.op)

            if operator_type not in operators:
                raise ValueError(f"Unsupported operator: {operator_type}")

            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            return operators[operator_type](left, right)

        if isinstance(node, ast.UnaryOp):

            operand = self._eval_node(node.operand)  

            if isinstance(node.op, ast.USub):
                return -operand

            if isinstance(node.op, ast.UAdd):
                return operand

        raise ValueError(f"Unsupported unary operator: {type(node.op)}")