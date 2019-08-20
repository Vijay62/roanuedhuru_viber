#-*- coding: utf-8 -*-
#libraries
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen
import feedparser

class Jobs:
    @staticmethod
    def vazeefa():
        req = Request('https://vazeefa.mv/jobs', headers={'User-Agent': 'Mozilla/5.0'})
        vazeefa = urlopen(req)
        soup = BeautifulSoup(vazeefa, 'lxml')

        jobs_list = soup.find_all('div', class_='row jobListn')

        jobs = []
        
        for job in jobs_list:
            job_details = []
            title = job.find('h2').text.strip()
            link = 'https://vazeefa.mv/' + job.find('a').get('href')
            employer = job.find('span', itemprop='hiringOrganization').text.strip()
            location = job.find('span', itemprop='jobLocation').text.strip()
            apply_before = job.find('span', itemprop='validThrough').text.strip()
            salary = job.find('span', itemprop='baseSalary')
            if salary is not None:
                salary = 'MVR ' + salary.text.strip()
            else:
                salary = 'Not Stated'
            job_details.extend((title, link, employer, location, apply_before, salary))
            jobs.append(job_details)
        return jobs
            
    @staticmethod
    def gazette():
        req = Request('http://www.gazette.gov.mv/iulaan/type/vazeefaa', headers={'User-Agent': 'Mozilla/5.0'})
        gazette = urlopen(req)
        soup = BeautifulSoup(gazette, 'lxml')

        jobs_list = soup.find_all('div', class_= 'col-md-12 bordered items')

        jobs = []
        
        for job in jobs_list:
            job_details = []
            title = job.find('a', class_='iulaan-title').text
            link = job.find('a', class_='iulaan-title').get('href')
            employer = job.find('a', class_='iulaan-office').text
            info = job.find_all('div', class_='col-md-4 no-padding left info')
            published_date = info[0].text
            apply_before = info[1].text
            job_details.extend((title, link, employer, published_date, apply_before))
            jobs.append(job_details)
        return jobs

    @staticmethod
    def jobmv():
        feed = feedparser.parse('https://www.blogger.com/feeds/4665003579075051486/posts/default?alt=rss')

        jobs = []

        for entry in feed.entries[0:20]:
            job_details = []
            title = entry.title
            link = entry.link
            job_details.extend((title, link))
            jobs.append(job_details)
        return jobs



vazeefa = Jobs.vazeefa()
gazette = Jobs.gazette()
jobmv = Jobs.jobmv()
#print(vazeefa)
#print(gazette)
#print(jobmv)
