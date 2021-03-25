from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import os
import spacy


def train_nlu (data, config_file, model_dir):
    # Load training nlu data
    training_data = load_data(data)
    # Load config file and create trainer object
    trainer = Trainer(config.load(config_file))
    # train the nlu model
    trainer.train(training_data)
    model_directory = trainer.persist(model_dir, fixed_model_name = 'chat')


def get_intent_confidence(text):
    # loading the interpreter 
    interpreter = Interpreter.load('/models/nlu/default/chat')
    # Predict intent
    intent=interpreter.parse(text)
    # Print the predicted intent dictionary with confidence
    return intent['intent']

def train_dialogue(path="python -m rasa_core.train -d domain.yml -s data/stories.md -o models/dialogue --debug"):

    x=os.system(path)
    if x==0:
    	print("Model Trained Successfully")
    else:
    	print("Error, Please chcek the issue")
    	
if __name__ == '__main__':

    spacy.load('en_core_web_sm')

	# Calling NLU training tunction
    train_nlu('data/nlu.md', 'nlu_config.yml', 'models/nlu')

	# Calling dialogue training function
    train_dialogue()

