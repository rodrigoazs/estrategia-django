"""Script para gerar aleatoriamente cursos, aulas,
apostilas e suas relações ManyToMany.

As relações são geradas obtendo uma aula e uma apostila
de forma aleatória e com reposição.
"""

import os
import json
import datetime
import random
import urllib.request
import lorem

LOREM_PICSUM = 'https://picsum.photos/200/150/?blur=2'
STATIC_PATH = 'static/images/cursos/{}/{}'
STATIC_URL = 'static/images/cursos/{}/{}/{}.jpg'
CURSOS_SIZE = 20
AULAS_SIZE = 70
APOSTILAS_SIZE = 50
PACOTES_SIZE = 300

def generate():
    data = []
    current_time = datetime.datetime.now()
    year = current_time.strftime('%Y')
    month = current_time.strftime('%m')
    dir_path = '../../' + STATIC_PATH.format(year, month)

    # generando cursos
    for pk in range(1, CURSOS_SIZE+1):
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
        print('Gerado curso {}'.format(pk))

    # gerando aulas
    for pk in range(1, AULAS_SIZE+1):
        model = {'model': 'cursos.aula',
                 'pk': pk,
                 'fields': {
                     'titulo': ' '.join(lorem.sentence().split()[:2]),
                     'curso': random.randint(1, CURSOS_SIZE),
                     'created_at': str(current_time),
                     'updated_at': str(current_time),
                     }
                }
        data.append(model)
        print('Gerado aula {}'.format(pk))

    # gerando apostilas
    for pk in range(1, APOSTILAS_SIZE+1):
        model = {'model': 'cursos.apostila',
                 'pk': pk,
                 'fields': {
                     'titulo': ' '.join(lorem.sentence().split()[:3]),
                     'created_at': str(current_time),
                     'updated_at': str(current_time),
                     }
                }
        data.append(model)
        print('Gerado apostila {}'.format(pk))

    # gerando pacotes
    for pk in range(1, PACOTES_SIZE+1):
        model = {'model': 'cursos.pacote',
                 'pk': pk,
                 'fields': {
                     'apostila': random.randint(1, APOSTILAS_SIZE),
                     'aula': random.randint(1, AULAS_SIZE),
                     }
                }
        data.append(model)
        print('Gerado pacote {}'.format(pk))

    with open('cursos.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    generate()
