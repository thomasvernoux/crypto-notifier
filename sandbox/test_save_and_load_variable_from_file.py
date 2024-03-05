
import pickle

# Définir les variables à stocker
variable1 = {'nom': 'John', 'age': 30}
variable2 = [1, 2, 3, 4, 5]

# Stocker les variables dans un tuple
variables_a_stocker = (variable1, variable2)

# Enregistrer le tuple dans un fichier
with open('sandbox/mes_variables.pkl', 'wb') as fichier:
    pickle.dump(variables_a_stocker, fichier)

# Rappeler les variables depuis le fichier
with open('mes_variables.pkl', 'rb') as fichier:
    variables_chargees = pickle.load(fichier)

# Assigner les variables chargées à leurs noms respectifs
variable1_chargee, variable2_chargee = variables_chargees

# Afficher les variables rappelées
print("Variable 1:", variable1_chargee)
print("Variable 2:", variable2_chargee)



