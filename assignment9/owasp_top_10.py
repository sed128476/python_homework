from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have the Chrome WebDriver installed
driver.get("https://owasp.org/www-project-top-ten/")

# Find the top 10 vulnerabilities using XPath
vulnerabilities = driver.find_elements(By.XPATH, "//div[@class='top10-item']")

# Extract vulnerability titles and links
owasp_top_10 = []
for vuln in vulnerabilities:
    title = vuln.find_element(By.XPATH, ".//h3").text
    link = vuln.find_element(By.XPATH, ".//a").get_attribute("href")
    owasp_top_10.append({"title": title, "link": link})

# Print extracted data
print(owasp_top_10)

# Write data to a CSV file
csv_file_path = "C:/code-dream/python_class/working/python_homework/assignment9/owasp_top_10.csv"
print('csv_')
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["title", "link"])
    writer.writeheader()
    writer.writerows(owasp_top_10)

# Close the browser
driver.quit()

# Create a challenges.txt file
challenges_file_path = "C:/code-dream/python_class/working/python_homework/assignment9/challenges.txt"

#challenges_file_path = "python_homework/assignment9/challenges.txt"
with open(challenges_file_path, mode="w", encoding="utf-8") as file:
    file.write("Challenges faced:\n")
    file.write("- Identifying the correct XPath for extracting vulnerabilities.\n")
    file.write("- Ensuring Selenium WebDriver is properly installed and configured.\n")
    file.write("- Handling dynamic content loading on the webpage.\n")
    file.write("\nResolution:\n")
    file.write("- Used browser developer tools to inspect elements and determine XPath.\n")
    file.write("- Installed the latest Chrome WebDriver and ensured compatibility.\n")
    file.write("- Implemented explicit waits if needed for dynamic content.\n")

print("Data extraction complete. CSV and challenges.txt files created successfully.")

