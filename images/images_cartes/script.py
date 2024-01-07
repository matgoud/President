import os 

val = ["2", "3", "4" ,"5" ,"6","7","8","9","10","A", "J", "K", "Q"]
col = ["c","d","h","s"]

replace = {
	"A": "as",
	"J" : "valet",
	"K": "roi",
	"Q": "reine",
	"c": "trefle",
	"d": "carreau",
	"h": "coeur",
	"s": "pique"
}

for valeur in val:
    for color in col:
        old_name = os.path.join("M:\\Vacataire\\2021\\Second semestre\\Campus 2\\Conception logiciel - L1\\test-jacquier\\images", (replace[valeur] if valeur in replace else valeur) +"_"+replace[color]+".png")
        new_name = os.path.join("M:\\Vacataire\\2021\\Second semestre\\Campus 2\\Conception logiciel - L1\\test-jacquier\\images", (replace[valeur] if valeur in replace else valeur) +"_de_"+replace[color]+".png")
        print(old_name)
        print(new_name)
        
        os.rename(old_name, new_name)