import requests
from bs4 import BeautifulSoup as bs


def merge_tags2(parent_tag):
    text = ''
    for v in parent_tag:
        text += v.text.strip() + '\n'
    return text.strip()


URL_TEMPLATE = "https://codeforces.com/problemset/problem/1848/F?lang=ru"
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, "html.parser")

statement = soup.find_all('div', class_='problem-statement')[0]
statement_parts = list(statement)

header = statement_parts[0]
tasktitle = header.findChildren('div', class_='title')
timelimit = header.findChildren('div', class_='time-limit')
memorylimit = header.findChildren('div', class_='memory-limit')
inputfile = header.findChildren('div', class_='input-file')
outputfile = header.findChildren('div', class_='output-file')

content = statement_parts[1]
input_specification = statement_parts[2]
output_specification = statement_parts[3]
sample_tests = statement_parts[4].findChildren('div', class_='sample-test')[0]
note = statement_parts[5].findChildren('p')

input_ = [test.findChildren('pre') for test in sample_tests.findChildren('div', class_='input')]
output_ = [test.findChildren('pre') for test in sample_tests.findChildren('div', class_='output')]


div = statement.findChildren('div', class_='header')[0]


print(tasktitle[0].getText())
print(list(timelimit[0])[1])
print(list(memorylimit[0])[1])
print(list(inputfile[0])[1])
print(list(outputfile[0])[1], '\n')
print(content.text, '\n')
print(list(input_specification)[0].text)
print(list(input_specification)[1].text, '\n')
print(list(output_specification)[0].text)
print(list(output_specification)[1].text, '\n')
print('Пример:')
for test_input, test_output in zip(input_, output_):
    print('Входные данные')
    print(merge_tags2(test_input[0]))
    print('Выходные данные')
    print(merge_tags2(test_output), '\n')
print(note[0].getText())
