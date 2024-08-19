import pywikibot as pwb

site = pwb.Site('wikipedia:en')
page = pwb.Page(site, 'User:CanonNiBot/sandbox')

new_text = page.text + '\n\n The quick brown fox jumps over the lazy dog'

page.put(new_text, summary='test edit by bot')