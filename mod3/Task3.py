def get_domain_hierarchy(url):
    parts = url.split('.')
    parts.reverse()
    domain_hierarchy = []
    for i in range(len(parts)):
        domain = '.'.join(parts[:i+1])
        domain_hierarchy.append(domain)
    return domain_hierarchy

# Пример использования
url = input("Введите доменное имя сайта: ")
domains = get_domain_hierarchy(url)
for domain in domains:
    print(domain)
