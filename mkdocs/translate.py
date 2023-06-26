import os
import glob
import openai

# Votre clé d'API OpenAI
openai.api_key = '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'

# Chemin vers le dossier "docs"
docs_folder = 'docs/'

# Créer un sous-dossier "fr" s'il n'existe pas déjà
fr_folder = os.path.join(docs_folder, 'fr')
os.makedirs(fr_folder, exist_ok=True)

# Liste des fichiers Markdown (*.md) dans le dossier "docs"
md_files = glob.glob(os.path.join(docs_folder, '*.md'))

# Traduire et enregistrer les fichiers dans le sous-dossier "fr"
for md_file in md_files:
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Traduction automatique en utilisant l'API ChatGPT
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'Translate the following text to French:\n\n{content}',
        temperature=0.7,
        max_tokens=100
    )

    translation = response.choices[0].text.strip()

    # Créer le chemin de destination pour le fichier traduit
    translated_file = os.path.join(fr_folder, os.path.basename(md_file))

    # Enregistrer le contenu traduit dans le fichier
    with open(translated_file, 'w', encoding='utf-8') as file:
        file.write(translation)

    print(f"Traduction effectuée pour le fichier : {md_file} --> {translated_file}")
