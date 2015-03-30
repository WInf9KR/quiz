import json
out_file = open('fragen.txt', 'wt')

# Weitere Fragen können nach selbigem Prinzip in die "Fragen"-Liste angefügt werden:
# ["Frage""\n",["A: AntwortA", "B: AntwortB", "C: AntwortC", "D: AntwortD""\n"], "BuchstabeDerRichtigenAntwort"]

Fragen=[["Wie heißt die Hauptstadt von Deutschland?""\n",["A: Bonn","B: Hamburg","C: Berlin","D: München", "\n"],"C"],
        ["Welches Teilchen ist positiv?""\n",["A: Proton","B: Neutron","C: Elektron","D: Anion""\n"],"A"],
        ["Wie viele Einwohner hat Deutschland?""\n",["A: 82","B: 82.000","C: 82 Mrd.","D: 82 Mio.""\n"],"D"],
        ["Wann begann der erste Weltkrieg?""\n",["A: 1913","B: 1914","C: 1933","D: 1892""\n"],"B"],
        ["Wann wurde Angela Merkel geboren?""\n",["A: 1954", "B: 1960", "C: 1964", "D: 1950""\n"], "A"],
        ["Wo wurde Barack Obama geboren?""\n",["A: Süd Afrika", "B: Toronto", "C: New York", "D: Hawaii""\n"], "D"],
        ["Wie viele Einwohner hat Berlin?""\n",["A: 1,5 Millionen", "B: 2 Millionen", "C: 3,5 Millionen", "D: 4 Millionen""\n"], "C"]]
out_file.write(json.dumps(Fragen))
out_file.close()
