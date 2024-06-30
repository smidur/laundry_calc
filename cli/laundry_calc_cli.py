import re

num_pattern = re.compile(r'[0-9]+[,.][0-9]*|[0-9]+')
quit_pattern = re.compile(r'q|quit')

vat_str = input('Type VAT: ')
rate_str = input('Type rate: ')
# type the cost from the sheet

vat_re = re.search(num_pattern, vat_str).group()
rate_re = re.search(num_pattern, rate_str).group()

vat_re = float(vat_re)

vat = vat_re / 100.0
rate = float(rate_re)
