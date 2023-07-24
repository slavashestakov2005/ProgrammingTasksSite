import requests
from bs4 import BeautifulSoup as bs


class Parser:
    URL_TEMPLATE = ''

    name = ''
    memory_limit = ''
    time_limit = ''
    task_complexity = ''
    task_text = ''
    input_txt = ''
    output_txt = ''
    examples_input = []
    examples_output = []
    note = ''

    def get_html(self, task_id, encoding: str = 'utf-8'):
        url = self.URL_TEMPLATE.format(task_id)
        r = requests.get(url)
        r.encoding = encoding
        return bs(r.text, "html.parser")

    def parse(self, task_id):
        pass

    def to_json(self):
        return {
            "title": self.name,
            "memory_limit": self.memory_limit,
            "time_limit": self.time_limit,
            "complexity": self.task_complexity,
            "task_condition": self.task_text,
            "input_data": self.input_txt,
            "output_data": self.output_txt,
            "examples_input": self.examples_input,
            "examples_output": self.examples_output,
            "note": self.note
        }
