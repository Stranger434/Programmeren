# Gegevens
personen = 4
toegangsticket = 7.45
vip = 0.37
vip_tijd = 5
tijd = 45

# Berekening tijd
totale_tijd_vip = tijd / vip_tijd

# Berekening prijs
totale_prijs_toegang = round(toegangsticket * personen, 2)
totale_prijs_vip = round(totale_tijd_vip * (vip * personen), 2)
totale_prijs = round(totale_prijs_toegang + totale_prijs_vip, 2)

#Kosten Printen
print(f"BON")
print("--------------------------")
print(f"|Totaal aantal mensen {personen}")
print(f"|Toegangstickets €{totale_prijs_toegang:.2f}")
print("--------------------------")
print("VIP")
print(f"|Tijd {tijd} Minuten")
print(f"|Prijs €{totale_prijs_vip:.2f}")
print("--------------------------")
print("TOTAL")
print(f"|€{totale_prijs:.2f}")