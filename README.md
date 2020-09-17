# Star Wars Galaxies - Galactic Resource Manager - Extractor
This tool allows user to perform webscrapping in order to generate already existing resources and generates a pickle file.

This tool scrapes data from https://swgaide.com.

## Installation

This script has been developped to work on [Python 3.7](https://www.python.org/downloads/release/python-370/) it has not been tested on other versions of Python.

To use the script, you will need to install Python 3.7.

Also, you will have to install the librairies provided in the `requirements.txt` file.

```
$ pip3 install -r requirements.txt
```

## Usage

Once the librairies are installed, you can simply run the command : 

```
$ python3 swg-grm-extractor/extractor.py [-h] [--list-servers] [-r] [-v] [-u URL] -s SERVER
```

#### Further informations

```
This tool allows for users to scrape data and generate a pickle file containing
all actual resources from the specified SWG server.

optional arguments:
  -h, --help            show this help message and exit
  --list-servers        Put this flag to simply list the available servers.
                        This overrides other flags.
  -r, --refresh_data    Put this flag to refresh the resources classes list.
                        This overrides other flags.
  -v, --view_classes    Read the classes list.
  -u URL, --url URL     This value can override the default url (SWGAide) not
                        recommended since this tool is designed to work with
                        SWGAide.
  -s SERVER, --server SERVER
                        The SWG server number. Use flag '--list-servers' to
                        find your server.
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Mentions
* Special thanks to the contributors and maintainers of [SWGAide](https://github.com/twistedatrocity/SWGAide-NGE) for their projects which makes 
this project possible.
* Special thanks to the contributors and maintainers of [SWGCraft](http://swgcraft.net) for their project.
* Special thanks to the contributors and maintainers of [Galaxy Harvester](https://github.com/pwillworth/galaxyharvester) for their project.

Everyone of these projects helped understanding the crafting mechanics and resource qualities calculations.

## License
[MIT](https://choosealicense.com/licenses/mit/)