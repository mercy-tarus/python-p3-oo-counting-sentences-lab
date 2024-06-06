#!/usr/bin/env python3

import io
import sys

class MyString:
  def __init__(self, value=''):
        if not isinstance(value, str):
            raise TypeError("The value must be a string.\n")
        self.value = value

  def is_sentence(self):
        return self.value.endswith('.')

  def is_question(self):
        return self.value.endswith('?')

  def is_exclamation(self):
        return self.value.endswith('!')

  def count_sentences(self):
        
        temp_value = self.value.replace('.', '|').replace('?', '|').replace('!', '|')
        
        sentences = [sentence for sentence in temp_value.split('|') if sentence.strip()]
        return len(sentences)
  pass
