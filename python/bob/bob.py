def hey(phrase):
  phrase_is_question = phrase.strip().endswith("?")
  phrase_says_nothing = phrase.isspace() or phrase is ""
  phrase_is_yell = phrase.isupper()
  if phrase_is_question:
    if phrase_is_yell:
      return "Calm down, I know what I'm doing!"
    return "Sure."
  if phrase_is_yell:
    return "Whoa, chill out!"
  if phrase_says_nothing:
    return  "Fine. Be that way!"
  return "Whatever."
