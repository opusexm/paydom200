import concurrent.futures
import requests
from tqdm import tqdm

# Disable all HTTPS connection security warnings
requests.packages.urllib3.disable_warnings()

# Open the file with IP addresses to be checked
with open("ip_addresses.txt", "r") as f:
    ip_addresses = f.readlines()

# Function to check if a website is working using its IP address
def check_site(ip):
    url = f"https://{ip.strip()}"
    try:
        response = requests.get(url, timeout=5, verify=False)
        if response.status_code == 200:
            # Сохраняем IP-адреса с рабочими сайтами в файл
            with open("input.txt", "a") as f:
                f.write(ip)
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False

# Variable to store the number of found working sites
working_sites_count = 0

# Number of threads
num_threads = 100

# Create a thread pool
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Проверяем каждый IP-адрес на работоспособность сайта
    future_to_ip = {executor.submit(check_site, ip): ip for ip in ip_addresses}
    # Используем библиотеку tqdm для отображения прогресса
    for future in tqdm(concurrent.futures.as_completed(future_to_ip), total=len(ip_addresses)):
        if future.result():
            working_sites_count += 1

# Print the total number of found working sites
print(f"Found {working_sites_count} working sites")

