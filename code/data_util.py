#Candace Edwards
#cedward2@hawaii.edu
#ICS 690B Final Project
#Fall 2022

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.error import HTTPError



#scrape department links from UH course catalog page and registration page
#desc_url = 'https://manoa.hawaii.edu/catalog/courses-overview/'
#tagIn = 'ul'
#classIn = 'course-directory'

#reg_url = 'https://www.sis.hawaii.edu/uhdad/avail.classes?i=MAN&t=202330'
#tagIn='div'
#classIn="columns"

def get_all_links(url,tagIn, classIn):
  req = Request(url)
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page, "lxml")

  links = list()

  search_area = soup.find(tagIn, class_= classIn)

  for link in search_area.findAll('a'):
      links.append(link.get('href'))
  
  return links


#remove . character returns cleaned list of link suffixes for scrape
#link_list = get_all_links()
def trim_link(link_list):
    cleaned_list = list()

    for i in range(len(link_list)):
        l_link = link_list[i]
        link = l_link[1:]
        cleaned_list.append(link)
    
    return cleaned_list

#used in pull_course_desc parses title string in description page; return tuple [course_num, course_title]
def course_num_title(course_title):
    k=2
    new_string_list = course_title.split(" ",k)
    #print(new_string_list)
    course_num = new_string_list[0]+ " "+ new_string_list[1]
    #print(course_num)
    try:
      new_string_list_1 = new_string_list[-1].split("(")
      new_string_list_1.pop()
      course_title = new_string_list_1[0]

      #print(course_title)
      return [course_num, course_title]
      
    except IndexError:
      print(IndexError)
      print(course_title)
      return [course_num,'title error']


#scrapes course description from catalog page
def pull_course_desc(url,desc_list_in):

    try:  
      req = Request(url)
      html_page = urlopen(req)
      soup = BeautifulSoup(html_page, "lxml")
    except HTTPError:
      print(HTTPError)
      print(url)
      return

    try:
      courses = soup.find_all("div", class_="post-content")
      #print(type(courses))
      #print(len(courses))

      #desc_list = list()

      for course in courses:
          title = course.find('h2').getText()
          #print(title) 
          course_info = course_num_title(title)
          #description = course.find("div",class_="entry-content").getText() #or p tag
          description = course.find('p').getText()
          course_info.append(description)
          desc_list_in.append(course_info)
    
    except AttributeError:
      print(AttributeError)
      print(url)
      return
   
    #return desc_list


#scrapes registration information from banner
def pull_course_reg(url, rows):

    try:
      req = Request(url)
      html_page = urlopen(req)

      soup = BeautifulSoup(html_page, "lxml")

      dept_name = soup.find('h1')
      dept_name_cleaned = dept_name.text.strip()
      #print(dept_name_cleaned)

      search_table=soup.find_all("table", class_="listOfClasses")
      #print(len(search_table))
      #print(type(search_table))
    
    except HTTPError:
      print(HTTPError)
      print(url)
      return

    try:
        working_table = search_table[0]
    except IndexError:
        print(IndexError)
        print(dept_name_cleaned)
        return -1  #flag an error

    #rows = list()
    # Find all `tr` tags
    data_rows = working_table.find_all('tr')

    for row in data_rows:
        value = row.find_all('td')
        beautified_value = [ele.text.strip() for ele in value]
        
    # Remove data arrays that are empty
        if len(beautified_value) == 0:
            #continue
            return
        beautified_value.append(dept_name_cleaned) #add depatment name to end of row
        rows.append(beautified_value)
    
    #return rows