# pokemon-ai

A [textgenrnn](https://github.com/minimaxir/textgenrnn) text-generating AI to generate Pokémon names, using data from [PokéAPI](https://pokeapi.co).

The network is deliberately small (16-cell RNNs x 4 layers) to prevent overfitting.

`pokemon_training.py` processes the data and trains the model, `pokemon_generate.py` generates the names from the trained AI.

## Maintainer/Creator

Max Woolf ([@minimaxir](http://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT