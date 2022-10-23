from datetime import datetime
from hashlib import sha256

import json, random
import wikiquote
import conf

def choose_quotes (page_titles, raw_quotes):
	for i in range(conf.count):
		quote = get_quote(conf.languages[i])
		print(get_quote_header(conf.languages[i], quote[1]) + "\n" + quote[0] + "\n")
		ans = input(conf.lookgoodq).lower()
		print()
		while len(ans) == 0 or ans[0] != 'y':
			quote = get_quote(conf.languages[i])
			print(get_quote_header(conf.languages[i], quote[1]) + "\n" + quote[0] + "\n")
			ans = input(conf.lookgoodq).lower()
			print()
		page_titles.append(quote[1])
		raw_quotes.append(quote[0])

def fancyprint (x):
	chars_this_line = 0
	return_string = ""
	for i in range(len(x)):
		return_string += " " + (x[i] if x[i] != '\n' else '_') + " "
		chars_this_line += 1
		if i < len(x) - 1 and chars_this_line < conf.characters_per_line:
			if conf.vertical_lines:
				return_string += "|"
		else:
			return_string += "\n"
			return_string += (("   |" if conf.vertical_lines else "   ") * (chars_this_line - 1)) \
				+ "\n\n"
			chars_this_line = 0
	return return_string

def file_header (data):
	return datetime.now().strftime("%Y-%m-%d %A ") + sha256(data.encode()).hexdigest()

def format_txt_to_html (target):
	data = ""
	with open(target, "r") as file:
		data = file.read()
	with open(target + conf.html_extension, "w") as file:
		file.write(conf.html_header)
		file.write(data.replace(" ", conf.spaces_character)
			.replace("\n", conf.html_line_break)
			.replace("\t", conf.spaces_character * conf.tab_size))
		file.write(conf.html_footer)

def get_quote (lang = conf.default_language):
	page = random.choice(wikiquote.random_titles(lang = lang))
	try:
		quote = random.choice(wikiquote.quotes(page, lang = lang))
	except:
		return get_quote(lang)
	if (len(quote) > conf.quote_maxlen) or (len(quote) < conf.quote_minlen):
		return get_quote(lang)
	else:
		return (quote, page)

def get_quote_header (lang, title):
	lang_tag = "[" + lang + "]"
	page = conf.wikiquote_page % (lang, title.replace(" ", "_"))
	return lang_tag + " " + title + " " + page

def save_cipher ():
	strdata = ""
	data = {}
	with open(conf.quotes_json, "r") as file:
		strdata = file.read()
	with open(conf.txt_ciphers, "w") as file:
		data = json.loads(strdata)
		file.write(file_header(strdata) + "\n")
		file.write(conf.cipher_delim)
		count = 0
		for i in data:
			alpha = conf.alphabets[i["lang"]]
			shufalpha = ""
			for j in alpha:
				shufalpha += j
			shufalpha = shufalpha.upper()
			shufalpha = ''.join(random.sample(shufalpha, len(shufalpha)))
			cipher = ""
			for j in i["quote"].lower():
				try:
					cipher += shufalpha[alpha.index(j)]
				except:
					cipher += j
			if conf.is_patristocrat[count]:
				cipher = cipher.replace(" ", "")
				offset = 0
				for j in range(len(cipher) // conf.block_size):
					inx = (j * conf.block_size + offset + conf.block_size)
					cipher = cipher[:inx] + ' ' + cipher[inx:]
					offset += 1
			file.write(conf.hint_text % (i["lang"], conf.hint_pat if conf.is_patristocrat[count]
				else "", i["hint"] if conf.has_hint[count] else conf.no_hint) + "\n")
			file.write(fancyprint(cipher))
			for i in range(len(alpha)):
				if i % 10 == 0:
					file.write("\n")
				else:
					file.write("\t")
				file.write(alpha[i].upper() + "-> : " + str(cipher.count(alpha[i].upper())))
			file.write("\n" + conf.cipher_delim)
			count += 1

def save_key ():
	with open(conf.txt_key, "w") as key:
		with open(conf.quotes_json, "r") as file:
			strdata = file.read()
			key.write(file_header(strdata) + "\n\n")
			data = json.loads(strdata)
			for i in data:
				key.write(get_quote_header(i["lang"], i["hint"]) + "\n" + i["quote"] + "\n\n")

def save_quotes_as_json (page_titles, raw_quotes):
	output = []
	for i in range(0, conf.count):
		output.append({})
		output[i]["lang"] = conf.languages[i]
		output[i]["hint"] = page_titles[i]
		output[i]["quote"] = raw_quotes[i]
	with open(conf.quotes_json, "w") as file:
		file.write(json.dumps(output, indent = "\t"))

def setup_lang ():
	while len(conf.languages) < conf.count:
		conf.languages.append(conf.default_language)

	conf.languages = conf.languages[:conf.count]
	random.shuffle(conf.languages)

def setup_cipher_settings ():
	while len(conf.is_patristocrat) < conf.count:
		conf.is_patristocrat.append(conf.default_is_patristocrat)

	while len(conf.has_hint) < conf.count:
		conf.has_hint.append(conf.default_has_hint)

	conf.is_patristocrat = conf.is_patristocrat[:conf.count]
	conf.has_hint = conf.has_hint[:conf.count]
	random.shuffle(conf.is_patristocrat)
	random.shuffle(conf.has_hint)
