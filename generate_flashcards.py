import requests
import genanki

def get_surah(surah_number):
    # Obtenir le texte en arabe
    url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/ara-quransimple/{surah_number}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ayahs = data['chapter']
        return [ayah['text'] for ayah in ayahs]
    else:
        print(f"Erreur lors de la récupération de la sourate {surah_number}")
        return []

def get_surah_name(surah_number):
    # Liste des noms des sourates en arabe (indexée à partir de 1)
    surah_names = [
        "",  # Index 0 inutilisé pour correspondre au numéro de la sourate
        "الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة",
        "يونس", "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه",
        "الأنبياء", "الحج", "المؤمنون", "النور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الروم",
        "لقمان", "السجدة", "الأحزاب", "سبأ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر",
        "فصلت", "الشورى", "الزخرف", "الدخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق",
        "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة",
        "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج",
        "نوح", "الجن", "المزمل", "المدثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس",
        "التكوير", "الإنفطار", "المطففين", "الإنشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد",
        "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات",
        "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر",
        "المسد", "الإخلاص", "الفلق", "الناس"
    ]
    return surah_names[int(surah_number)]

def generate_flashcards(ayahs):
    flashcards = []
    for i in range(len(ayahs)):
        front = ' '.join(ayahs[max(0, i-5):i])
        back = ayahs[i]
        flashcards.append({'Front': front, 'Back': back})
    return flashcards

def create_anki_deck(flashcards, surah_number, surah_name):
    # Créer un modèle de carte
    my_model = genanki.Model(
        1607392319,
        'QuranModel',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Back}}',
            },
        ],
        css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: right;
            direction: rtl;
        }
        """
    )

    # Créer un paquet Anki avec le nom de la sourate
    deck_id = abs(hash(f'surah_{surah_number}')) % (10 ** 10)
    my_deck = genanki.Deck(
        deck_id,
        f'Sourate {surah_number} - {surah_name}'
    )

    # Ajouter les notes au paquet
    for card in flashcards:
        note = genanki.Note(
            model=my_model,
            fields=[card['Front'], card['Back']]
        )
        my_deck.add_note(note)

    # Générer le fichier .apkg
    filename = f'sourate_{surah_number}_{surah_name}.apkg'
    genanki.Package(my_deck).write_to_file(filename)
    print(f"Le fichier {filename} a été généré avec succès.")

def main():
    surah_number = input("Entrez le numéro de la sourate que vous souhaitez apprendre (1-114) : ")
    ayahs = get_surah(surah_number)
    if ayahs:
        surah_name = get_surah_name(surah_number)
        flashcards = generate_flashcards(ayahs)
        create_anki_deck(flashcards, surah_number, surah_name)
    else:
        print("Impossible de récupérer les données de la sourate.")

if __name__ == "__main__":
    main()
