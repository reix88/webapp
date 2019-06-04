# -*- coding: utf-8 -*-

def search4w(word, letter):
	""" Возвращает гласные, найденные в указанном слове. """
	return set(letter).intersection(set(word))
