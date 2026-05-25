import socket
import whois
import dns.resolver

def gather_osint(domain):

    data = {}

    try:

        # IP ADDRESS
        ip = socket.gethostbyname(domain)

        data['ip_address'] = ip

        # WHOIS INFO
        domain_info = whois.whois(domain)

        data['registrar'] = str(domain_info.registrar)

        data['creation_date'] = str(domain_info.creation_date)

        data['expiration_date'] = str(domain_info.expiration_date)

        # DNS RECORDS
        dns_records = []

        answers = dns.resolver.resolve(domain, 'A')

        for record in answers:
            dns_records.append(record.to_text())

        data['dns_records'] = dns_records

        return data

    except Exception as e:

        return {
            'error': str(e)
        }