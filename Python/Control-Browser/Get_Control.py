from selenium import webdriver

# Use the chromedriver.exe
driver = webdriver.Chrome(executable_path="chromedriver.exe")
# Get the url of the website, for example my github
driver.get("https://github.com/x33lyS?tab=repositories")

# Write on a the search-bar :
# search_bar = driver.find_element_by_id("search")
# search_bar.send_keys("x33lyS")

# Click on a button :
# continue_link = driver.find_element_by_link_text('/x33lyS?tab=repositories')
# continue_link.click()

# Print all repos :
all_titles = driver.find_elements_by_class_name("wb-break-all")

for title in all_titles:
    print(title.text)

# If you want more things to do go on :
# https://selenium-python.readthedocs.io/index.html
