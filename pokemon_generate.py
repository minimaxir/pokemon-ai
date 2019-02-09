from textgenrnn import textgenrnn
textgen = textgenrnn(weights_path='pokemon_weights.hdf5',
                     vocab_path='pokemon_vocab.json',
                     config_path='pokemon_config.json')

textgen.generate_to_file('pokemon_gen.txt', n=5000, temperature=[1.0, 0.5, 0.5])
