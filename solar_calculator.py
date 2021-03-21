#Daves wo ist die Sonne ausrechner

#Notiere hier die Uhrzeit

Stunde =14
Minuten=43



Uhrzeit=Stunde+Minuten/60

Grad=360*(Uhrzeit/24)

Grad = round(Grad, 1)

if Grad >= 22.5 and Grad < 67.5:
    print("Die Sonne steht im " + "Nordosten, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 67.5 and Grad < 112.5:
    print("Die Sonne steht im " + "Osten, in Richtung "+ str(Grad) + " Grad.")
elif Grad >=122.5 and Grad < 157.5:
    print("Die Sonne steht im " + "Südosten, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 157.5 and Grad < 205.5:
    print("Die Sonne steht im " + "Süden, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 205.5 and Grad < 247.5:
    print("Die Sonne steht im " + "Südwesten, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 247.5 and Grad < 292.5:
    print("Die Sonne steht im " + "Westen, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 292.5 and Grad < 337.5:
    print("Die Sonne steht im " + "Nordwesten, in Richtung "+ str(Grad) + " Grad.")
elif Grad >= 337.5 and Grad <= 360 or Grad >= 0 and Grad <22.5:
    print("Die Sonne steht im " + "Norden, in Richtung "+ str(Grad) + " Grad.")
