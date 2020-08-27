import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


from rasa.nlu.training_data import load_data
from rasa.nlu.model import Trainer
## from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu import config
from pprint import pprint

training_data = load_data('data/nlu.md')
trainer = Trainer(config.load('config.yml'))
interpreter = trainer.train(training_data, verbose=False)
model_directory = trainer.persist('models/nlu', fixed_model_name = 'current')

def speak(text):
    pprint(interpreter.parse(text))
