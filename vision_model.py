import base64
import requests
import os

# Openai Vision

#vision with image url


def vision_url(url, client):
  response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
          {
              "role":
              "user",
              "content": [
                  {
                      "type": "text",
                      "text": "What is the content of the image?"
                  },
                  {
                      "type": "image_url",
                      "image_url": {
                          "url": url,
                      },
                  },
              ],
          },
      ],
      max_tokens=10,
  )

  return print(response.choices[0].message.content)


def encode_image(file_path):
  with open(file_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')


def vision_file(file_path, client):
  base64_image = encode_image(file_path)

  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
  }
  payload = {
      "model":
      "gpt-4o",
      "messages": [{
          "role":
          "user",
          "content": [{
              "type": "text",
              "text": "Describe this image"
          }, {
              "type": "image_url",
              "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image}"
              }
          }]
      }],
      "max_tokens":
      10
  }
  response = requests.post("https://api.openai.com/v1/chat/completions",
                           headers=headers,
                           json=payload)
  print(response.json()['choices'][0]['message']['content'])
