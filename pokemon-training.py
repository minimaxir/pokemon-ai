import pandas as pd
from textgenrnn import textgenrnn

df = pd.read_csv('pokemon.csv')
pokemon = df['identifier'].str.replace(
    '(-[a-z0-9]+)', '').str.capitalize().unique().tolist()

textgen = textgenrnn(name="pokemon")

textgen.train_on_texts(pokemon, max_length=4, num_epochs=100,  gen_epochs=20,
                       new_model=True, rnn_size=16, rnn_layers=4, dropout=0.5)
