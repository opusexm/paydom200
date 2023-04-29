import requests
from tqdm import tqdm
import concurrent.futures

# The list of payment systems to be searched
payment_systems = ['visa', 'mastercard', 'amex', 'paypal', 'stripe', 'authorize.net']

# Disabling all HTTPS connection security warnings
requests.packages.urllib3.disable_warnings()

# Function to check for payment systems on a website
def check_site(url):
    try:
        response = requests.get(url, timeout=5, verify=False)
        if response.status_code == 200:
            # Проверяем наличие платежных систем в тексте страницы
            page_text = response.text.lower()
            for payment_system in payment_systems:
                if payment_system in page_text:
                    # Сохраняем домен с найденной платежной системой в файл
                    with open("payDom.txt", "a") as f:
                        f.write(url + "\n")
                    return True
            return False
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Opening the file with domains for checking
with open("dom.txt", "r") as f:
    domains = f.readlines()

# Variable to store the number of found domains with payment systems
pay_domains_count = 0

# Number of threads
num_threads = 10

# Creating a thread pool
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Checking each domain for payment systems
    future_to_domain = {executor.submit(check_site, "https://" + domain.strip()): domain for domain in domains}
    # Using the tqdm library to display progress
    for future in tqdm(concurrent.futures.as_completed(future_to_domain), total=len(domains)):
        if future.result():
            pay_domains_count += 1

# Displaying the total number of found domains with payment systems
print(f"Found {pay_domains_count} domains with payment systems")

