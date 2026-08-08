import json
import re


def clean_json_markdown(text: str) -> str:
    """
    去掉模型返回的

    ```json
    ...
    ```

    """

    text = text.strip()

    if text.startswith("```json"):
        text = re.sub(
            r"^```json",
            "",
            text,
        )

    if text.startswith("```"):
        text = re.sub(
            r"^```",
            "",
            text,
        )

    if text.endswith("```"):
        text = text[:-3]

    return text.strip()


def parse_json(text: str):

    text = clean_json_markdown(text)

    return json.loads(text)