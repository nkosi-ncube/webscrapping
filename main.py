from bs4 import BeautifulSoup
import request

html_text=requests.get('https://www.news24.com/parent/learn/freeexamresources/nsc-past-exam-papers-mathematics-20161006  ').text
soup =BeautifulSoup(html_text,'lxml')


my_list_of_papers =[]
matches=[]
paper_urls = soup.find('div',class_="article__content")
papers = paper_urls.find_all("p")
user_input=input("Enter year Mathematics and P1 or P2 download a paper from year 2008-2018:")
for paper in papers:
    if paper.find("a") != None:
        my_list_of_papers.append(str(paper.find("a").text))
for i  in range(len(my_list_of_papers)-1):
    if user_input == my_list_of_papers[i]:
        matches,append(user_input)
#print(my_list_of_papers)       

print(matches)
        




        




