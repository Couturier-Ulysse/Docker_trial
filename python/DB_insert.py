import mysql.connector

# Connexion à la base de données
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port='3306', database='db'
)
print("DB Connected")
cursor = connection.cursor()

# Fonction pour ajouter un étudiant
def add_student(first_name, last_name):
    try:
        sql = "INSERT INTO students (FirstName, Surname) VALUES (%s, %s)"
        val = (first_name, last_name)
        cursor.execute(sql, val)
        connection.commit()
        print(f"Étudiant {first_name} {last_name} ajouté avec succès.")
    except Exception as e:
        print(f"Erreur lors de l'ajout de l'étudiant : {e}")

# Fonction pour afficher le contenu de la base de données
def show_students():
    try:
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        if students:
            print("Contenu de la base de données :")
            for student in students:
                print(f"ID : {student[0]}, Prénom : {student[1]}, Nom : {student[2]}")
        else:
            print("La base de données ne contient aucun étudiant.")
    except Exception as e:
        print(f"Erreur lors de la récupération des étudiants : {e}")

if __name__ == "__main__":
    while (1):
        print("Entrez le prénom et le nom de l'étudiant (séparés par un espace) :")
        user_input = input()
        
        # Diviser l'entrée en prénom et nom
        first_name, last_name = user_input.split(" ", 1)
        
        # Ajouter l'étudiant à la base de données
        add_student(first_name, last_name)
        
        # Afficher le contenu mis à jour de la base de données
        show_students()
    
    # Fermer la connexion à la base de données
    connection.close()
