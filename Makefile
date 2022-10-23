all: quotes.json cipher.txt cipher.txt.html

# Also generates the key
cipher.txt: quotes.json
	./scramble.py

# Also generates the formatted key
cipher.txt.html: cipher.txt
	./formatter.py

clean:
	rm -rf __pycache__
	rm -rf quotes.json cipher.txt cipher.txt.html key.txt key.txt.html

quotes.json:
	./getquotes.sh

# Similar to make clean, this doesn't remove pycache, so it can be used in run.sh
tidy:
	rm -rf quotes.json cipher.txt cipher.txt.html key.txt key.txt.html

.PHONY: all clean
