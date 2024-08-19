import pywikibot as pwb

site = pwb.Site('wikipedia:en')
page = pwb.Page(site, 'User:CanonNiBot/sandbox')

new_text = page.text + '\n\n The quick brown fox jumps over the lazy dog'

for i in range(10):
    page.put(new_text, summary=f'test edit by bot, iteration {i}')