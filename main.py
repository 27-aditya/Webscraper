from bs4 import BeautifulSoup
import requests
import time

print('Enter the skills that you do not know')

unfamiliar_skills = input('>' )
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text.replace(' ','')
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open('files/{}.txt'.format(index),'w') as f:
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skills: {skills.strip()} \n")
                    f.write(f"More Info: {more_info} \n")
                print(f'File Saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting Time {time_wait} minutes....')
        time.sleep(time_wait * 60)