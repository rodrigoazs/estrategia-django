import os
import lorem
import json
import datetime
import urllib.request

LOREM_PICSUM = 'https://picsum.photos/200/150/?blur=2'
STATIC_PATH = 'static/images/cursos/{}/{}'
STATIC_URL = 'static/images/cursos/{}/{}/{}.jpg'
CURSOS_SIZE = 20

def generate():
    data = []
    current_time = datetime.datetime.now()

    for pk in range(1, CURSOS_SIZE+1):
        year = current_time.strftime('%Y')
        month = current_time.strftime('%m')
        dir_path = '../../' + STATIC_PATH.format(year, month)
        image_path = STATIC_URL.format(year, month, pk)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        urllib.request.urlretrieve(LOREM_PICSUM, '../../' + image_path)
        model = {'model': 'cursos.curso',
                 'pk': pk,
                 'fields': {
                     'titulo': lorem.sentence(),
                     'descricao': lorem.paragraph(),
                     'imagem': image_path,
                     'created_at': str(current_time),
                     'updated_at': str(current_time),
                     }
                }
        data.append(model)
        print('Generated curso {}'.format(pk))

    with open('cursos.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    generate()
