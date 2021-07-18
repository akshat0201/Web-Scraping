from bs4 import BeautifulSoup
import requests
import time

print('Put skills you do not know')
fake_skill = input('>')
print(f'Filtering out {fake_skill}')


def find_jobs():
  html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

  soup = BeautifulSoup(html_text, 'lxml')
  jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
  for index, job in enumerate(jobs):
    list_date = job.find('span', class_ = 'sim-posted').span.text
    if 'few' in list_date:
      comp_name = job.find('h3', class_ = 'joblist-comp-name').text.strip().replace(' ', '')
      skills = job.find('span', class_ = 'srp-skills').text.replace(' ', '')
      more_info = job.header.h2.a['href']

      if fake_skill not in skills:
        with open(f'Jobs Website/posts/{comp_name}.txt', 'w') as f:
          f.write(f"Company Name: {comp_name.strip()}\n")
          f.write(f'Skills Needed: {skills.strip()}\n')
          f.write(f'More Info: {more_info}\n')
        print(f'File Saved {comp_name}.txt')


if __name__ == '__main__':
  while True:
    find_jobs()
    wait = 5
    print(f'Waiting {wait} mins...')
    time.sleep(wait*60);
    
