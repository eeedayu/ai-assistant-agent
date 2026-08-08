class PromptBuilder:
    @staticmethod
    def render(template: str, **kwargs):
        
        return template.format(**kwargs)
        