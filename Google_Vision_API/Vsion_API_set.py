#reference: https://cloud.google.com/vision/docs/detect-labels-image-client-libraries

#install lib

!pip install --upgrade google-cloud-vision

#!protoc --version
#!pip show protobuf
####right now tensor wants 3.9 protobuf while google vision wants 4.19 so lets try to install uninstal this package when we are using correspponding GOOGLE_APPLICATION_CREDENTIALS
!pip uninstall protobuf 3.19.6 Y
!wget https://raw.githubusercontent.com/googleapis/python-vision/master/samples/snippets/quickstart/resources/wakeupcat.jpg



from google.api_core.protobuf_helpers import get_messages
from google.cloud import vision

import sys, types, os;
from google.cloud.vision_v1 import types
                                    #    /Users/divya.mereddy/Documents/Divya/GitHub/MachineLearningProjects/Home_Automation/Outfit_Suggestions/cobalt-upgrade-335321-c19b741b41c0.json
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/Users/divyamereddy/Documents/GitHub/ML_Research_Projects/Home_Automation/Outfit_Suggestions/Key/learned-spider-364816-cbb90b65cb6d.json"
client = vision.ImageAnnotatorClient()

import io


path = '/Users/divyamereddy/Documents/GitHub/ML_Research_Projects/Home_Automation/Outfit_Suggestions/Data/Picture/Training/Sample.jpg'
with io.open(path, 'rb') as image_file:
        content = image_file.read()

from __future__ import print_function
from google.cloud import vision

image_uri = 'gs://cloud-samples-data/vision/using_curl/shanghai.jpeg'


client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = image_uri

objects = client.object_localization(image=image).localized_object_annotations

print('Number of objects found: {}'.format(len(objects)))
for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))

client.safe_search_detection(image=image)

response = client.label_detection(image=image)


print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))

#

response = client.image_properties(image=image)
props = response.image_properties_annotation
print('Properties:')

for color in props.dominant_colors.colors:
    print('fraction: {}'.format(color.pixel_fraction))
    print('\tr: {}'.format(color.color.red))
    print('\tg: {}'.format(color.color.green))
    print('\tb: {}'.format(color.color.blue))
    print('\ta: {}'.format(color.color.alpha))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))

#################


client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri =
response = client.label_detection(image=image)

print('Labels (and confidence score):')
print('=' * 30)
for label in response.label_annotations:
    print(label.description, '(%.2f%%)' % (label.score*100.))

#########################
# #below is not working as detech Labels are not importing but I think its not needed####
# from utils import detectLabels, detectObjects
# image_source = types.ImageSource(image_uri=path)
# labels = detectLabels(image=image)
#   # Only save images that have the label "Fashion"
# if any([x.description == "Fashion" for x in labels]):
#     fashionPics.append(uri)
