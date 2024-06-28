# Generate an image with dall e 3


def img_ai(msg):
  response = client.images.generate(
      model='dall-e-2',
      prompt=msg,
      size='256x256',
      n=1,
      quality='hd',  #standard
      style='natural'  #vivid
  )

  return print(response.data[0].url)
