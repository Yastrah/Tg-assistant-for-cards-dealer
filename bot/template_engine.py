from jinja2 import Environment, FileSystemLoader

class TemplateEngine:
    def __init__(self, template_dir):
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def render_template(self, template_name, **kwargs) -> str:
        """
        Рендерит HTML-шаблон с указанными данными
        :param template_name: имя шаблона (без расширения)
        :param kwargs: аргументы для подстановки
        :return: отрендеренный HTML в виде строкм
        """
        template = self.env.get_template(f"{template_name}.html")
        return template.render(**kwargs)


template_dir = "../templates"
engine = TemplateEngine(template_dir)
