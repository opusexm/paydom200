import socket
import xlwt
import concurrent.futures

# Number of threads to use for processing
num_threads = 10

# Read input IP addresses from a file
with open('input.txt', 'r') as input_file:
    ip_addresses = [line.strip() for line in input_file.readlines()]

# Create a new Excel workbook and worksheet
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('Domains')

# Write header row to the worksheet
worksheet.write(0, 0, 'IP')
worksheet.write(0, 1, 'Domain')

# Function to get the domain name from an IP address
def get_domain_name(ip_address):
    try:
        domain_name = socket.gethostbyaddr(ip_address)[0]
        # Check if the domain is a DNS name, mail server, etc.
        if domain_name.startswith('dns') or domain_name.startswith('mail'):
            return None
        # Remove newline character from the domain name
        domain_name = domain_name.strip()
        # Check if the domain name contains any periods
        if '.' not in domain_name:
            return None
        # Extract the top-level domain from the domain name
        domain_name = domain_name.split('.')[-2] + '.' + domain_name.split('.')[-1]
        return domain_name
    except socket.herror:
        return None
    except socket.gaierror:
        return None

# Process IP addresses in parallel using a thread pool
with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
    futures = []
    for ip_address in ip_addresses:
        future = executor.submit(get_domain_name, ip_address)
        futures.append(future)

    # Set to collect unique domain names
    domains = set()

    # Iterate over completed futures and write domain names to the worksheet
    for i, future in enumerate(concurrent.futures.as_completed(futures), start=1):
        domain_name = future.result()
        if domain_name is not None:
            worksheet.write(i, 0, ip_addresses[i-1])
            worksheet.write(i, 1, domain_name)
            domains.add(domain_name)

        # Print progress to the console
        progress = i / len(ip_addresses) * 100
        print(f'Processed {i}/{len(ip_addresses)} IP addresses ({progress:.2f}%)')

    # Write unique domain names to a text file
    with open('dom.txt', 'w') as dom_file:
        dom_file.write('\n'.join(sorted(domains)))

# Save the workbook to an Excel file
workbook.save('output.xls')

# Print a message to the console when done
print('Done')

