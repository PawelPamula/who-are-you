from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from functools import partial

tedmask = imread('tedxbw.png', flatten=True)

def color_func(word=None, font_size=None, position=None,
                      orientation=None, font_path=None, random_state=None, dictionary=None):

    # val = max(0, min(255, font_size * 6 - 30))
    val = dictionary[word] * 42 - 50
    return "rgb(%d, %d, %d)" % (0, 0, val)

def generate(words):
  """
  Words are supposed to be a list of tuples [(word, weight)]
  """

  words_dict = dict(words)
  words = " ".join(words_dict.keys())

  wordcloud = WordCloud(stopwords=STOPWORDS,
                        background_color='white',
                        width=400,
                        height=400,
                        scale=3,
                        mask=tedmask,
                        color_func=partial(color_func, dictionary=words_dict)).generate(words)

  img = wordcloud.to_image()
  pixdata = img.load()

  for y in xrange(img.size[1]):
      for x in xrange(img.size[0]):
          if pixdata[x, y] == (255, 255, 255, 255):
              pixdata[x, y] = (255, 255, 255, 0)

  return img