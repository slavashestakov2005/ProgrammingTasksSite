from parser import Parser


class CodeforcesParser(Parser):
    URL_TEMPLATE = "https://codeforces.com/problemset/problem/{}?lang=ru"
    def merge_tags(self, parent_tag):
        return ''.join(map(lambda x: x.text.strip() + '\n', parent_tag))

    def get_html_from_list(self, lst):
        return ' '.join(map(str, lst))

    def parse(self, task_id: str):
        soup = self.get_html(task_id)

        statement = soup.find_all('div', class_='problem-statement')[0]
        statement_parts = list(statement)

        header = statement_parts[0]
        self.name = header.findChildren('div', class_='title')[0].text
        self.time_limit = list(header.findChildren('div', class_='time-limit')[0])[1]
        self.memory_limit = list(header.findChildren('div', class_='memory-limit')[0])[1]
        inputfile = header.findChildren('div', class_='input-file')
        outputfile = header.findChildren('div', class_='output-file')

        self.task_text = self.get_html_from_list(statement_parts[1])
        self.input_txt = self.get_html_from_list(list(statement_parts[2])[1:])
        self.output_txt = self.get_html_from_list(list(statement_parts[3])[1:])
        self.note = self.get_html_from_list(list(statement_parts[5])[1:])

        sample_tests = statement_parts[4].findChildren('div', class_='sample-test')[0]

        input_ = [test.findChildren('pre') for test in sample_tests.findChildren('div', class_='input')]
        output_ = [test.findChildren('pre') for test in sample_tests.findChildren('div', class_='output')]

        # print(list(inputfile[0])[1])
        # print(list(outputfile[0])[1], '\n')
        for test_input, test_output in zip(input_, output_):
            self.examples_input.append(self.merge_tags(test_input[0]))
            self.examples_output.append(self.merge_tags(test_output[0]))


p = CodeforcesParser()
p.parse('1850/G')
