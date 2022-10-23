#!/usr/bin/bash

EDITOR=vim

./getquotes.py

read -p "Edit quotes in $EDITOR [y/N]? " yn

case $yn in
	[yY] ) $EDITOR quotes.json;;
	* ) break;;
esac
