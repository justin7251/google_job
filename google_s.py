from DrissionPage import ChromiumPage
import csv
import time

# Google Jobs search URL
GJOBS_URL = "https://www.google.com/search?q=php%20developer%20jobs%20birmingham&jbr=sep:0&udm=8&ved=2ahUKEwjHp9regJaIAxUnTkEAHWHTAUgQ3L8LegQIMhAM"

# Initialize Drission and ChromiumPage
page = ChromiumPage()

# Open the Google Jobs page
page.get(GJOBS_URL)
time.sleep(3)  # Wait for the page to load

# Open a CSV file to write the data
with open('google_jobs.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Location", "Posted Time", "Job Link"])

    # Scroll to load all jobs (if needed)
    # for _ in range(5):
    #     page.scroll.down(200)
    #     time.sleep(2)  # Adjust based on your internet speed

    # Extract job listings
    job_cards = page.eles('.GoEOPd')
    for job in job_cards:
        try:
            job.click('.tNxQIb')
            title = job.ele('css:>div').text
            company = job.ele('@class:waQ7qe').text
            location = job.ele('@class:mLdNec').text
            posted_time = job.ele('@class:RcZtZb').text
            job_link = job.ele("a[href]")

            # Write job details to CSV
            writer.writerow([title, company, location, posted_time, job_link])

        except Exception as e:
            print(f"Error occurred: {e}")
            continue

# Close the DrissionPage
page.close()

print("Job data has been successfully saved to google_jobs.csv")
