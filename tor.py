import requests

response = requests.get('https://check.torproject.org/')

content = response.text

ip_start = content.find('<p>Your IP address appears to be:  <strong>')
ip_end = content.find('</strong></p>', ip_start)
ip_address = content[ip_start + len('<p>Your IP address appears to be:  <strong>'):ip_end]

the_string = 'Congratulations. This browser is configured to use Tor.'
if the_string in content:
    print(the_string)
    print(ip_address)
