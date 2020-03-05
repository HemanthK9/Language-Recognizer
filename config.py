#This is the maximum word length we consider. Words longer than this are discarded
wordLength = 12

#These are the Wikipedia articles from which words of each language are extracted
articles = {

                'en':['actor', 'alcohol', 'cheque', 'cancer', 'chocolate', 'debate', 'hobby', 'melon', 'propaganda',
                      'religion', 'violin', 'england', 'MediaWiki'],

                'cs': ['praha', 'evropa', 'pyreneje', 'voda', 'housle', 'Náboženství', 'Příroda', 'Ekosystém',
                    'vzdělání', 'Irsko', 'Dům', 'Zpěvák', 'Zeus', 'Mykény', 'Starověké_Řecko', 'Renesance',
                    'Andrej_Babiš', 'Správa_železniční_dopravní_cesty', 'Kraje_v_Česku', 'Česko', 'Slezsko',
                    'Latina', 'Spojené_království', 'Římský_senát'],

                'de': ['Deutsche_Sprache', 'Deutschland', 'Kommunistische_Partei_der_Sowjetunion', 'Wasser',
                    'Festkörper', 'Seele', 'Geist', 'Dreifaltigkeit', 'Große', 'Christentum', 'Gott'],

                'sv': ['Svenska', 'Sverige', 'Danmark', 'Europeiska_unionen', 'Medeltiden', 'Feodalism', 'Kung',
                    'Kejsare', 'Monarki', 'Valmonarki', 'Choklad', 'Mjölk', 'Prolaktin', 'Kvinna', 'Eldvapen',
                    'Kina', 'Götar', 'Romantiken', 'Ideologi', 'Tänkande', 'Pedagogik', 'Sekund', 'Solen', 'Väder',
                    'Mellanöstern', 'Väte', 'Anatomi', 'Hjärta', 'Puls', 'Grekiska', 'Cypern'],

                'fr': ['Français', 'Langues_romanes', 'Charlemagne', 'Traité_de_Verdun', 'Louis_le_Pieux',
                    'Son_(physique)', 'Zoologie', 'Intelligence_animale', 'Intelligence', 'Tautologie',
                    'Pléonasme', 'Figure_de_style']
}

tags = {
    'en' : 'english',
    'fr' : 'french',
    'de' : 'german',
    'cs' : 'czech',
    'sv' : 'swedish'
}
