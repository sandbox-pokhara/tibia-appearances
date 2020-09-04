# Tibia Appearances Extractor

Python script to convert tibia appearances.dat to json.

## Installation

Windows

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Linux

```
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
(venv) $ python main.py -h
usage: main.py [-h] appearances_dat output

positional arguments:
  appearances_dat
  output

optional arguments:
  -h, --help       show this help message and exit
```

## Example

```
(venv) $ python main.py assets/appearances.dat appearances.json
```

## Output Format

```
    {
      "id": 3003,
      "frameGroup": [
        {
          "fixedFrameGroup": "FIXED_FRAME_GROUP_OBJECT_INITIAL",
          "id": 2,
          "spriteInfo": {
            "patternWidth": 1,
            "patternHeight": 1,
            "patternDepth": 1,
            "layers": 1,
            "spriteId": [
              120779
            ],
            "isOpaque": false,
            "boundingBoxPerDirection": [
              {
                "x": 4,
                "y": 7,
                "width": 24,
                "height": 20
              }
            ]
          }
        }
      ],
      "flags": {
        "usable": true,
        "multiuse": true,
        "take": true,
        "market": {
          "category": "ITEM_CATEGORY_TOOLS",
          "tradeAsObjectId": 3003,
          "showAsObjectId": 3003
        },
        "npcsaledata": [
          {
            "name": "Al Dee",
            "location": "Rookgaard",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "John",
            "location": "Treasure Island",
            "salePrice": 100,
            "buyPrice": 0
          },
          {
            "name": "Larek",
            "location": "Ogre Village",
            "salePrice": 50,
            "buyPrice": 0
          },
          {
            "name": "Lee'Delle",
            "location": "Rookgaard",
            "salePrice": 45,
            "buyPrice": 8
          },
          {
            "name": "Nelliem",
            "location": "Venore City",
            "salePrice": 50,
            "buyPrice": 0
          },
          {
            "name": "Pompan",
            "location": "Farmine City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Pompan",
            "location": "Farmine City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Raffael",
            "location": "Isle of Destiny",
            "salePrice": 50,
            "buyPrice": 0
          },
          {
            "name": "Rafzan",
            "location": "Venore Surroundings",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "Rafzan",
            "location": "Venore Surroundings",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "Rafzan",
            "location": "Venore Surroundings",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "Richard",
            "location": "Dawnport Centre",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "Zethra",
            "location": "Adventurers' Guild",
            "salePrice": 50,
            "buyPrice": 8
          },
          {
            "name": "Hireling",
            "location": "Unknown",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Ahmet",
            "location": "Ankrahmun City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Bashira",
            "location": "Ab'Dendriel City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Beatrice",
            "location": "Edron Castle",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Bertha",
            "location": "Svargrond City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Bezil",
            "location": "Kazordoon City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Gladys",
            "location": "Grimvale",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Gorn",
            "location": "Thais City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Gree Dee",
            "location": "Yalahar Centre",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Halif",
            "location": "Darashia City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Lubo",
            "location": "Thais Surroundings",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Maro",
            "location": "Rathleton City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Maun",
            "location": "Lower Roshamuul",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Nezil",
            "location": "Kazordoon City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Perod",
            "location": "Port Hope City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Red Lilly",
            "location": "Liberty Bay City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Sarina",
            "location": "Carlin City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Shiantis",
            "location": "Venore City",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Rock in a Hard Place",
            "location": "Gray Beach",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Tefrit",
            "location": "Kilmaresh Mountains",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Timur",
            "location": "Fibula",
            "salePrice": 50,
            "buyPrice": 15
          },
          {
            "name": "Zora",
            "location": "Tyrsung",
            "salePrice": 50,
            "buyPrice": 15
          }
        ],
        "cyclopediaitem": {
          "cyclopediaType": 3003
        }
      },
      "name": "rope"
    }
```
