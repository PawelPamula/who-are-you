from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

tedmask = imread('./visualization/tedxbw.png', flatten=True)

words = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis laoreet felis ipsum, id gravida lorem feugiat congue. Donec leo felis, vulputate nec nulla sed, sodales vehicula magna. Quisque eget ex magna. Morbi gravida nisl sit amet nulla mattis, placerat varius odio vestibulum. Maecenas auctor consectetur neque ac viverra. Mauris in hendrerit risus. Nullam semper metus in tempus venenatis"""

def color_func(word=None, font_size=None, position=None,
                      orientation=None, font_path=None, random_state=None):

    val = max(0, min(255, font_size * 6 - 30))
    return "rgb(%d, %d, %d)" % (val, val, val)

def generate():
  wordcloud = WordCloud(stopwords=STOPWORDS,
                        background_color='white',
                        width=400,
                        height=400,
                        scale=3,
                        mask=tedmask,
                        color_func=color_func).generate(words)

  img = wordcloud.to_image()
  pixdata = img.load()

  for y in xrange(img.size[1]):
      for x in xrange(img.size[0]):
          if pixdata[x, y] == (255, 255, 255, 255):
              pixdata[x, y] = (255, 255, 255, 0)

  return img