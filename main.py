# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# driver = webdriver.Chrome()
# driver.get("www.google.com")
# try:
#     element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"element_id")))
#     element1 = driver.find_element(By.XPATH,"")
#     action = ActionChains(driver)
#     action.click(element1)
#     action.perform()
# except:
#     pass
# finally:
#     driver.quit()
#

# capgemini interview
# Function to read and print lines from a file
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:  # Open the file in read mode
            for line in file:  # Iterate through each line in the file
                print(line.strip())  # Print the line after stripping any leading/trailing whitespace
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'C:\\Users\\DELL\\Desktop\\BABI\\git_hub_token.txt'  # Replace with the path to your file
read_file(file_path)
