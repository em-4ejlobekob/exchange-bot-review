TOKEN = 'TOKEN'

exceptions = ['<tr>', '</tr>', '<th>', '</th>', '<td>', '</td>', '[<table class="data">',
              '<tbody>', 'Цифр. код', 'Букв. код', 'Единиц', 'Валюта', 'Курс', '</tbody>', '</table>]', '\n']

main_notes = {'$': ['dollar by', 'USD'], '€': ['euro by', 'EUR'], '£': ['pound by', 'GBP'],
              '¥': ['jena by', 'JPY'], '₣': ['frank by', 'CHF']}

notes = ['$', '€', '£', '¥', '₣']
settings = ['🇷🇺', '🇬🇧', '🇰🇿', 'ℹ', '⚙']
to_convert_txt = '💱'

dict_data = dict()
dict_data['RUB'] = 1
pair = ['USD', 'RUB']

flag_pairs = {'RUB': ['🇷🇺', 'name_ru'], 'AUD': ['🇦🇺', 'name_au'], 'AZN': ['🇦🇿', 'name_az'], 'AMD': ['🇦🇲', 'name_am'],
              'BYN': ['🇧🇾', 'name_by'], 'BGN': ['🇧🇬', 'name_bg'], 'BRL': ['🇧🇷', 'name_br'], 'HUF': ['🇭🇺', 'name_hu'],
              'KRW': ['🇰🇷', 'name_kr'], 'HKD': ['🇭🇰', 'name_hk'], 'DKK': ['🇩🇰', 'name_dk'], 'USD': ['🇺🇸', 'name_us'],
              'EUR': ['🇪🇺', 'name_eu'], 'INR': ['🇮🇳', 'name_in'], 'KZT': ['🇰🇿', 'name_kz'], 'CAD': ['🇨🇦', 'name_ca'],
              'KGS': ['🇰🇬', 'name_kg'], 'CNY': ['🇨🇳', 'name_cn'], 'MDL': ['🇲🇩', 'name_md'], 'TMT': ['🇹🇲', 'name_tm'],
              'NOK': ['🇳🇴', 'name_no'], 'PLN': ['🇵🇱', 'name_pl'], 'RON': ['🇷🇴', 'name_ro'], 'TJS': ['🇹🇯', 'name_tj'],
              'TRY': ['🇹🇷', 'name_tr'], 'UZS': ['🇺🇿', 'name_uz'], 'UAH': ['🇺🇦', 'name_ua'], 'GBP': ['🇬🇧', 'name_gb'],
              'CZK': ['🇨🇿', 'name_cz'], 'SEK': ['🇸🇪', 'name_se'], 'CHF': ['🇨🇭', 'name_ch'], 'JPY': ['🇯🇵', 'name_jp']}
