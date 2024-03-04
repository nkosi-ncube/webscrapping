from bs4 import BeautifulSoup

# r means i want to read the file only
'''
with open('saexampapers.co.za/grade-12-mathematics','r') as html_file:
    content = html_file.read()
    print(content)
    #work with tags as objects
    soup =BeautifulSoup(content,'lxml')
    '''
    #print(soup.prettify())
    tags = soup.find_all('h2')
    #print(tags)
    for tag in tags:
        print(tag.text)
    '''
    course_cards = soup.find_all('div',class_='card')
    for course  in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
''''
