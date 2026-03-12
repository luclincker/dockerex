from counter import add_one_to_count, remove_one_to_count

def main():
    count = add_one_to_count(0)
    print('Affichage du compteur après ajout : ' + str(count))
    count = remove_one_to_count(1)
    print('Affichage du compteur après retrait : ' + str(count))

main()
