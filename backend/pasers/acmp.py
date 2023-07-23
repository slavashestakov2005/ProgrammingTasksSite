import requests
from bs4 import BeautifulSoup as bs
from .parser import Parser


class AcmpParser(Parser):
    
    def get_text(self, teg, clas, index):
        soup = bs(self.r.text, "html.parser")

        task_name = soup.find_all(teg, class_=clas)
        
        spisok_class=list(task_name)
        
        return spisok_class[index-1].text

    def get_text1(self, teg, teg1, clas):
        soup = bs(self.r.text, "html.parser")
        
        task_name = soup.find_all(teg, class_=clas)
        
        spisok_class=list(task_name)
        
        for i in spisok_class:
            z=list(i.find_all(teg1))
            self.examples_input.append(z[1].text)
            self.examples_output.append(z[2].text)
                

    def parse(self, task_id: int):
        URL_TEMPLATE = "https://acmp.ru/index.asp?main=task&lang=ru&id_task=" + str(task_id)
        self.r = requests.get(URL_TEMPLATE)
        self.r.encoding = 'windows-1251'
        #название
        self.name = self.get_text('h1', '', 1)
        #сложность
        limitations=list(self.get_text('i', '', 1).split())
        self.task_complexity=limitations[-1]
        self.memory_limit=limitations[1]+' '+limitations[2]
        self.time_limit=limitations[4]+' '+limitations[5]
        
        
        #текст задачи
        self.task_text = self.get_text('p', 'text', 1)
        #входные данные
        self.input_txt = self.get_text('p', 'text', 2)
        #входные данные
        self.output_txt = self.get_text('p', 'text', 3)
        #примеры
        self.get_text1('tr', 'td', 'white2')




parser = AcmpParser()
parser.parse(706)
print(parser.name)
print(parser.memory_limit)
print(parser.time_limit)
print(parser.examples_input)