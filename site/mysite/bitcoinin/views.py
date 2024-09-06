from django.shortcuts import render
import requests 
import json
import re 
import random
# Create your views here.
bible_chapters = {
    "Genesis": random.randint(1,51),
    "1 Exodus": random.randint(1, 41),
    "Leviticus": random.randint(1, 28),
    "Numbers": random.randint(1, 37),
    "Deuteronomy": random.randint(1, 35),
    "Joshua": random.randint(1, 25),
    "Judges": random.randint(1, 22),
    "Ruth": random.randint(1, 5),
    "1 Samuel": random.randint(1, 32),
    "2 Samuel": random.randint(1, 25),
    "1 Kings": random.randint(1, 23),
    "2 Kings": random.randint(1, 26),
    "1 Chronicles": random.randint(1, 30),
    "2 Chronicles": random.randint(1, 37),
    "Ezra": random.randint(1, 11),
    "Nehemiah": random.randint(1, 14),
    "Esther": random.randint(1, 11),
    "Job": random.randint(1, 43),
    "Psalms": random.randint(1, 151),
    "Proverbs": random.randint(1, 32),
    "Ecclesiastes": random.randint(1, 13),
    "Song of Solomon": random.randint(1, 9),
    "Isaiah": random.randint(1, 67),
    "Jeremiah": random.randint(1, 53),
    "Lamentations": random.randint(1, 6),
    "Ezekiel": random.randint(1, 49),
    "Daniel": random.randint(1, 13),
    "Hosea": random.randint(1, 15),
    "Joel": random.randint(1, 4),
    "Amos": random.randint(1, 10),
    "Obadiah": random.randint(1, 2),
    "Jonah": random.randint(1, 5),
    "Micah": random.randint(1, 8),
    "Nahum": random.randint(1, 4),
    "Habakkuk": random.randint(1, 4),
    "Zephaniah": random.randint(1, 4),
    "Haggai": random.randint(1, 3),
    "Zechariah": random.randint(1, 15),
    "Malachi": random.randint(1, 5),
    "Matthew": random.randint(1, 29),
    "Mark": random.randint(1, 17),
    "Luke": random.randint(1, 25),
    "John": random.randint(1, 22),
    "Acts": random.randint(1, 29),
    "Romans": random.randint(1, 17),
    "1 Corinthians": random.randint(1, 17),
    "2 Corinthians": random.randint(1, 14),
    "Galatians": random.randint(1, 7),
    "Ephesians": random.randint(1, 7),
    "Philippians": random.randint(1, 5),
    "Colossians": random.randint(1, 5),
    "1 Thessalonians": random.randint(1, 6),
    "2 Thessalonians": random.randint(1, 4),
    "1 Timothy": random.randint(1, 7),
    "2 Timothy": random.randint(1, 5),
    "Titus": random.randint(1, 4),
    "Philemon": random.randint(1, 2),
    "Hebrews": random.randint(1, 14),
    "James": random.randint(1, 6),
    "1 Peter": random.randint(1, 6),
    "2 Peter": random.randint(1, 4),
    "1 John": random.randint(1, 6),
    "2 John": random.randint(1, 2),
    "3 John": random.randint(1, 2),
    "Jude": random.randint(1, 2),
    "Revelation": random.randint(1, 23)
}

def index(request):
    l = "https://bible-api.com/"
    lan = l + ecriture()
    resq = requests.get(lan)
    data1 = resq.json()
    reference = data1['reference']
    text = data1['reference'],data1['text']

    res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = res.json()
    houre = data['time']['updated']
    price = data['bpi']['EUR']['rate_float']
    prixfcfa = price* 655
    prixcom = price * 495
    return render(request, 'bitcoin/index.html', {
        'houre': houre,
        'price': price,
        'pricefc': prixfcfa,
        'pricecom': prixcom,
        'reference': reference,
        'text': text,
    })


def ecriture():
    bib = random.choice(list(bible_chapters.keys()))
    b = bible_chapters[bib]
    a = re.split(r'\W+', bib)
    if len(a) == 1: 
        return str(a[0]+ "+1"+":"+str(b))   
    else:
        return str(a[1]+"+"+a[0]+":"+str(b))
    

    