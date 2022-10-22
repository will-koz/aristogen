import json, random
import wikiquote
import conf

def choose_quotes (page_titles, raw_quotes):
	for i in range(conf.count):
		quote = get_quote(conf.languages[i])
		page_titles.append(quote[1])
		raw_quotes.append(quote[0])
		print(get_quote_header(conf.languages[i], page_titles[i]) + "\n" + raw_quotes[i] + "\n")

	ans = input(conf.lookgoodq).lower()
	if len(ans) == 0 or ans[0] != 'y':
		print()
		while len(page_titles) > 0:
			page_titles.pop()
		while len(raw_quotes) > 0:
			raw_quotes.pop()
		choose_quotes(page_titles, raw_quotes)

def fancyprint (x):
	chars_this_line = 0
	return_string = ""
	for i in range(len(x)):
		return_string += " " + x[i] + " "
		chars_this_line += 1
		if i < len(x) - 1 and chars_this_line < conf.characters_per_line:
			# return_string += "|"
			pass
		else:
			return_string += "\n"
			# For vertical lines, uncomment the += line above and add a vertical line at the end of
			# these three spaces
			return_string += ("   " * (chars_this_line - 1)) + "\n\n"
			chars_this_line = 0
	return return_string

def format_txt_to_html (target):
	data = ""
	with open(target, "r") as file:
		data = file.read()
	with open(target + conf.html_extension, "w") as file:
		file.write(conf.html_header)
		file.write(data.replace(" ", "&nbsp;").replace("\n", conf.html_line_break))
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
	data = {}
	with open(conf.quotes_json, "r") as file:
		data = json.loads(file.read())
	with open(conf.txt_ciphers, "w") as file:
		file.write(conf.cipher_delim)
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
			# TODO handle patristocrats
			# TODO make this based on a variable in conf:
			file.write(conf.hint_text % (i["lang"], i["hint"]) + "\n")
			file.write(fancyprint(cipher))
			for i in range(len(alpha)):
				if i % 10 == 0:
					file.write("\n")
				else:
					file.write("\t")
				file.write(alpha[i].upper() + ": " + str(cipher.count(alpha[i].upper())))
			file.write("\n" + conf.cipher_delim)

def save_key ():
	with open(conf.txt_key, "w") as key:
		with open(conf.quotes_json, "r") as file:
			data = json.loads(file.read())
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
