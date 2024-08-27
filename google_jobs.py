import datetime
from threading import Thread
from DrissionPage import ChromiumPage
from DataRecorder import Recorder

GJOBS_URL = "https://www.google.com/search?q=php%20developer%20jobs%20birmingham&jbr=sep:0&udm=8&ved=2ahUKEwidv-yJ-JWIAxWkT0EAHSmbKnIQ3L8LegQIJBAM"

def collect(page, recorder, title):
    num = 1 
    while True:
        for i in page.eles('.GoEOPd'):
            data = i.click('.tNxQIb')
            recorder.add_data((title, i.eles('.JmvMcb'), num))

    recorder.record() 


def main():
    page = ChromiumPage()
    page.get(GJOBS_URL)
    recorder = Recorder(f"data_{datetime.datetime.now():%d-%b-%Y}.csv")

    Thread(target=collect, args=(page, recorder, 'job')).start()


if __name__ == '__main__':
    main()


