from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from functools import partial
from PIL import ImageColor

tedmask = imread('./visualization/tedxbw.png', flatten=True)

def color_func(word=None, font_size=None, position=None,
                      orientation=None, font_path=None, random_state=None, dictionary=None):

    # val = max(0, min(255, font_size * 6 - 30))
    try:
      val = max(0, min(255, dictionary[word] * 42 - 50))
    except KeyError:
      val = 100
    return "rgb(%d, %d, %d)" % (255, 255 - val, 255 - val)

def generate(words):
  """
  Words are supposed to be a list of tuples [(word, weight)]
  """

  words_dict = dict(words)
  words = " ".join(words_dict.keys())

  wordcloud = WordCloud(stopwords=STOPWORDS,
                        background_color=ImageColor.getcolor('#36394c', 'RGB'),
                        width=400,
                        height=400,
                        scale=3,
                        mask=tedmask,
                        color_func=partial(color_func, dictionary=words_dict)).generate(words)

  img = wordcloud.to_image()
  pixdata = img.load()

  return img
