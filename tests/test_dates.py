from spacy.language import Language

examples = [
    ("le 06/02/2020", dict(day="06", month="02", year="2020")),
    ("Le 4 aout", dict(day="4", month="aout")),
    ("le 0 6 1 2 2 0 2 2", dict(day="0 6", month="1 2", year="2 0 2 2")),
]


def test_dates(nlp: Language):
    nlp.add_pipe("pseudonymisation-dates")

    for example, date_string in examples:
        doc = nlp(example)
        assert doc.ents
        assert doc.ents[0]._.date_string.dict(exclude_none=True) == date_string
