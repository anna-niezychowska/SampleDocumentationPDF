Reference
=========

def capitalize()
----------------

   .. code-block::

      def capitalize(input_string):
          """Capitalizes the first character of each word in the input string.

          Args:
              input_string (str)

          Returns:
              str: A new string

          """
          return input_string.title()

def lowercase()
---------------

   .. code-block::

      def lowercase(input_string):
          """
          Args:
              input_string (str)

          Returns:
              str: A new string with all characters converted to lowercase.

          """
          return input_string.lower()

def uppercase()
---------------

   .. code-block::

      def uppercase(input_string):
          """
          Args:
              input_string (str): The input string to be converted to uppercase.

          Returns:
              str: A new string with all characters converted to uppercase.

          """
             return input_string.upper()

def sort_list()
---------------

   .. code-block::

      def sort_list(word_list):
          """
       Args:
           word_list (list): The list of elements to be sorted.

       Returns:
           list: A new list with the elements sorted in ascending order.

       """
          return sorted(word_list)

def count_word_occurrences()
----------------------------

   .. code-block::

      def count_word_occurrences(word_list, target_word):
          """
          Args:
              word_list (list): The list of words to search for occurrences.
              target_word (str): The word to be counted in the word_list.

          Returns:
              int: The number of occurrences of the target_word in the word_list.

          """
          word_count = 0
          for word in word_list:
              if word == target_word:
                  word_count += 1
          return word_count

def find_and_replace()
----------------------

   .. code-block::

      def find_and_replace(source_string, target_word, replacement_word):
          """
          Args:
              source_string (str): The original string to perform the replacement on.
              target_word (str): The word to be replaced in the source string.
              replacement_word (str): The word to replace the target_word with.

          Returns:
              str: A new string with all occurrences of the target word replaced with the replacement word.

          """
          return source_string.replace(target_word, replacement_word)


