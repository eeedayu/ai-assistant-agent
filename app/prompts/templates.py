CHAT_TEMPLATE = """
用户问题：

{question}

请认真回答。
"""


SUMMARIZE_TEMPLATE = """
请总结下面内容：

{text}
"""


REWRITE_TEMPLATE = """
请改写下面文本：

{text}
"""

RESUME_TEMPLATE = """
请分析下面的简历内容：

--------------------

{text}

--------------------

提取其中的候选人信息。
"""