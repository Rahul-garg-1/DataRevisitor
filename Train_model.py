import spacy
import random

def train_model(data,iterations):
  TRAIN_DATA=data
  nlp=spacy.blank('en')

  if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)

  for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
      ner.add_label(ent[2])

  other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
  with nlp.disable_pipes(*other_pipes):  
    optimizer = nlp.begin_training()

    for itn in range(iterations):
      random.shuffle(TRAIN_DATA)
      losses = {}

      for text, annotations in TRAIN_DATA:
        nlp.update(
                    [text],  
                    [annotations],  
                    drop=0.2,  
                    sgd=optimizer,  
                    losses=losses)
  return nlp

nlp_model=train_model(TRAIN_DATA,30)

nlp_model.to_disk('Nlp_model')