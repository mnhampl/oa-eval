def replace_incorrect_dois(datenbanken):
    dois_to_replace = {
        '10.1163/15691330-12241517': '10.1163/15691330-12341517',   # eine Ziffer falsch
        '10.12989/aas.2019.6.6.531': '10.12989/aas.2019.6.6.529'    # unklar. Nachrecherchiert, DOI entspricht der Angabe online 
                                                                    # beim Verlag. Habe aber zweite DOI gefunden, diese wird auch 
                                                                    # in den Dublette in den Daten verwendet
    }
    
    for db in datenbanken:
        for dokument in db.content:
            if dokument.DOI in dois_to_replace:
                dokument.DOI = dois_to_replace[dokument.DOI]
                # Bearbeitungsnotiz
                dokument.notes += 'DOI corrected manually. '
                print('DOI corrected manually. ')