# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle quantité d'eau faut-il assainir ? "))
base_water_qtt=5
base_filter_qtt=1
base_uv_lamp_qtt=3
base_chlore_qtt=0.5
multiplier_for_products=water_quantity/base_water_qtt
print(f"""Voici les éléments requis pour assainir {water_quantity}L d'eau:
\t- Filtre(s) : {int(base_filter_qtt*multiplier_for_products)}
\t- Lampe(s) UV : {int(base_uv_lamp_qtt*multiplier_for_products)}
\t- Chlore : {base_chlore_qtt*multiplier_for_products}kg""")
