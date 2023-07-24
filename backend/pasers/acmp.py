from .parser import Parser


class AcmpParser(Parser):
    URL_TEMPLATE = "https://acmp.ru/index.asp?main=task&lang=ru&id_task={}"
    def get_text(self, teg, clas, index):
        task_name = self.soup.find_all(teg, class_=clas)

        spisok_class = list(task_name)

        return spisok_class[index - 1].text

    def get_text1(self, teg, teg1, clas):
        task_name = self.soup.find_all(teg, class_=clas)

        spisok_class = list(task_name)

        examples_inpu = []
        examples_outpu = []
        for i in spisok_class:
            z = list(i.find_all(teg1))
            examples_inpu.append(z[1].text)
            examples_outpu.append(z[2].text)
        return examples_inpu, examples_outpu

    def parse(self, task_id: int):
        self.soup = self.get_html(task_id, 'windows-1251')
        # название
        self.name = self.get_text('h1', '', 1)
        # сложность
        limitations = list(self.get_text('i', '', 1).split())
        self.task_complexity = limitations[-1]
        self.task_complexity = self.task_complexity[0:-1]
        self.memory_limit = limitations[1] + ' ' + limitations[2]
        self.time_limit = limitations[4] + ' ' + limitations[5]

        # текст задачи
        self.task_text = self.get_text('p', 'text', 1)
        # входные данные
        self.input_txt = self.get_text('p', 'text', 2)
        # входные данные
        self.output_txt = self.get_text('p', 'text', 3)
        # примеры
        self.examples_input, self.examples_output = self.get_text1('tr', 'td', 'white2')


parser = AcmpParser()
parser.parse(706)
