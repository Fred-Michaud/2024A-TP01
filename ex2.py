# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = int(input("Quel est la quantité d'eau à assainir?: "))
base_water_qtt=5
base_filter_qtt=1
base_uv_lamp_qtt=3
base_chlore_qtt=0.5
multiplier_for_products=water_quantity//base_water_qtt
print(f"""
Voici les matériaux requis pour l'assainissement de {water_quantity} L d'eau
Nombre de filtre(s): {base_filter_qtt*multiplier_for_products}
Nombre de lampe(s) uv: {base_uv_lamp_qtt*multiplier_for_products}
Quantité de chlore: {base_chlore_qtt*multiplier_for_products} kg
""")
