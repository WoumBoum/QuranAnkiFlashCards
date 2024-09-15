# Anki Deck Generator for Learning the Quran

Welcome to this project aimed at facilitating the learning of the Quran using Anki flashcards. This project automatically generates Anki decks for each Surah (chapter) of the Quran, enabling a structured and efficient learning experience.

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Card Structure](#card-structure)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## About the Project

This project was created to offer an effective method for learning the Quran by leveraging Anki's spaced repetition system. The generated decks allow users to learn each Surah by focusing on the progressive assimilation of verses (ayahs).

## Features

- Automatic generation of Anki decks (`.apkg`) for all 114 Surahs of the Quran.
- Each deck is named according to the Surah's number and name for easy organization.
- Cards are designed to help memorize verses by providing context from previous verses.
- Text is in Arabic with proper formatting for correct display in Anki.
- Provided Python scripts allow for customized deck generation.

## Prerequisites

- **Python 3.6** or higher
- Python Libraries:
  - `requests`
  - `genanki`
- **Anki** installed on your computer to import and use the decks.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your_username/quran-anki-decks.git
   cd quran-anki-decks
   ```

2. **Install Python Dependencies**

   Ensure you have Python 3.6 or higher installed.

   ```bash
   pip install -r requirements.txt
   ```

   *If the `requirements.txt` file does not exist, you can manually install the dependencies:*

   ```bash
   pip install requests genanki
   ```

## Usage

### Importing Pre-generated Anki Decks

1. **Download the Decks**

   Anki decks for all Surahs are available in the `decks` folder. Download the deck corresponding to the Surah you wish to learn.

2. **Import into Anki**

   - Open Anki.
   - Go to **File > Import**.
   - Select the downloaded `.apkg` file.
   - Click **Import** to add the deck to your collection.

### Generating the Decks Yourself

If you wish to generate the decks yourself, for example, to customize the cards:

1. **Run the Generation Script**

   ```bash
   python generate_all_surahs.py
   ```

   This script generates Anki decks for all Surahs and saves them in the `decks` folder.

2. **Customization**

   You can modify the provided Python scripts to change the number of previous verses displayed on the front, add translations, etc.

## Card Structure

- **Front**: Contains the 5 verses preceding the current verse (or fewer if the verse is among the first in the Surah).
- **Back**: Contains the current verse to memorize.

This structure provides context and facilitates memorization by building upon previously learned verses.

## Customization

You can customize the scripts to adapt the cards to your needs:

- **Modify the Number of Previous Verses**: In the `generate_flashcards` function, change the value `5` to the desired number.

  ```python
  front = ' '.join(ayahs[max(0, i-5):i])
  ```

- **Add Translations**: You can extend the script to include translations by fetching data from the API and adding an extra field to the cards.

- **Change Formatting**: Modify the CSS in the Anki model definition to change the appearance of the cards.

  ```python
  css="""
  .card {
      font-family: 'Arial';
      font-size: 24px;
      text-align: right;
      direction: rtl;
  }
  """
  ```

## Contributing

Contributions are welcome! If you wish to improve this project:

1. **Fork the Repository**

   Click the **Fork** button at the top of the page to create a copy of the repository on your GitHub account.

2. **Create a Branch for Your Feature**

   ```bash
   git checkout -b your-feature-branch
   ```

3. **Commit Your Changes**

   ```bash
   git commit -am "Add a new feature"
   ```

4. **Push the Branch**

   ```bash
   git push origin your-feature-branch
   ```

5. **Create a Pull Request**

   Go to your forked repository on GitHub and click on **New Pull Request**.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgments

- **Anki**: For the spaced repetition software that makes learning more efficient.
- **Quran API**: Thanks to [fawazahmed0](https://github.com/fawazahmed0/quran-api) for the API providing Quran data.
- **Contributors**: Everyone who has contributed to this project.

---

*May Allah facilitate your learning of the Quran.*