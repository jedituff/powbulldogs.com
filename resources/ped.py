from re import L


dog = "Dog"
pedigree_dogs = [["Sire"], ["Dam"], ["Grandsire 1"], ["Granddam 1"], ["Grandsire 2"], ["Granddam 2"], ["Great-grandsire 1"], ["Great-granddam 1"], ["Great-grandsire 2"], ["Great-granddam 2"], ["Great-grandsire 3"], ["Great-granddam 3"], ["Great-grandsire 4"], ["Great-granddam 4"], ["Great-Great-grandsire 1"], ["Great-Great-granddam 1"], ["Great-Great-grandsire 2"], ["Great-Great-granddam 2"], ["Great-Great-grandsire 3"], ["Great-Great-granddam 3"], ["Great-Great-grandsire 4"], ["Great-Great-granddam 4"], ["Great-Great-grandsire 5"], ["Great-Great-granddam 5"], ["Great-Great-grandsire 6"], ["Great-Great-granddam 6"], ["Great-Great-grandsire 7"], ["Great-Great-granddam 7"], ["Great-Great-grandsire 8"], ["Great-Great-granddam 8"]]

view_default = input("Would you like to view the default ped? y/n: ")


if view_default == "n" or view_default == "N" or view_default == "no" or view_default == "No" or view_default == "NO":
    dog = input("What is the dog's name?")
    pedigree_dogs[0][0] = input("Sire?")
    pedigree_dogs[1][0] = input("Dam?")
    pedigree_dogs[2][0] = input("Grandsire 1?")
    pedigree_dogs[3][0] = input("Granddam 1?")
    pedigree_dogs[4][0] = input("Grandsire 2?")
    pedigree_dogs[5][0] = input("Granddam 2?")
    pedigree_dogs[6][0] = input("Great-grandsire 1?")
    pedigree_dogs[7][0] = input("Great-granddam 1?")
    pedigree_dogs[8][0] = input("Great-grandsire 2?")
    pedigree_dogs[9][0] = input("Great-granddam 2?")
    pedigree_dogs[10][0] = input("Great-grandsire 3?")
    pedigree_dogs[11][0] = input("Great-granddam 3?")
    pedigree_dogs[12][0] = input("Great-grandsire 4?")
    pedigree_dogs[13][0] = input("Great-granddam 4?")
    pedigree_dogs[14][0] = input("Great-Great-grandsire 1?")
    pedigree_dogs[15][0] = input("Great-Great-granddam 1?")
    pedigree_dogs[16][0] = input("Great-Great-grandsire 2?")
    pedigree_dogs[17][0] = input("Great-Great-granddam 2?")
    pedigree_dogs[18][0] = input("Great-Great-grandsire 3?")
    pedigree_dogs[19][0] = input("Great-Great-granddam 3?")
    pedigree_dogs[20][0] = input("Great-Great-grandsire 4?")
    pedigree_dogs[21][0] = input("Great-Great-granddam4?")
    pedigree_dogs[22][0] = input("Great-Great-grandsire 5?")
    pedigree_dogs[23][0] = input("Great-Great-granddam 5?")
    pedigree_dogs[24][0] = input("Great-Great-grandsire 6?")
    pedigree_dogs[25][0] = input("Great-Great-granddam 6?")
    pedigree_dogs[26][0] = input("Great-Great-grandsire 7?")
    pedigree_dogs[27][0] = input("Great-Great-granddam 7?")
    pedigree_dogs[28][0] = input("Great-Great-grandsire 8?")
    pedigree_dogs[29][0] = input("Great-Great-granddam 8?")



sire = pedigree_dogs[0][0]
dam = pedigree_dogs[1][0]

gs1 = pedigree_dogs[2][0]
gd1 = pedigree_dogs[3][0]
gs2 = pedigree_dogs[4][0]
gd2 = pedigree_dogs[5][0]

ggs1 = pedigree_dogs[6][0]
ggd1 = pedigree_dogs[7][0]
ggs2 = pedigree_dogs[8][0]
ggd2 = pedigree_dogs[9][0]
ggs3 = pedigree_dogs[10][0]
ggd3 = pedigree_dogs[11][0]
ggs4 = pedigree_dogs[12][0]
ggd4 = pedigree_dogs[13][0]

gggs1 = pedigree_dogs[14][0]
gggd1 = pedigree_dogs[15][0]
gggs2 = pedigree_dogs[16][0]
gggd2 = pedigree_dogs[17][0]
gggs3 = pedigree_dogs[18][0]
gggd3 = pedigree_dogs[19][0]
gggs4 = pedigree_dogs[20][0]
gggd4 = pedigree_dogs[21][0]
gggs5 = pedigree_dogs[22][0]
gggd5 = pedigree_dogs[23][0]
gggs6 = pedigree_dogs[24][0]
gggd6 = pedigree_dogs[25][0]
gggs7 = pedigree_dogs[26][0]
gggd7 = pedigree_dogs[27][0]
gggs8 = pedigree_dogs[28][0]
gggd8 = pedigree_dogs[29][0]

# write ped to file... *needs work*
# generate_ped = input("Generate new ped? y/n: ")

# if generate_ped == "y" or generate_ped == "Y" or generate_ped == "yes" or generate_ped == "Yes" or generate_ped == "YES":
#     ped_name = input("What will you name the ped? ")
#     L = []
#     with open(ped_name, "a") as ped_name:
#         ped_name.writelines(L)

# Print ped
# ######################################################
print("                                  ", gggs1)
print("                         ", ggs1)
print("                                  ", gggd1)
print("                 ", gs1)
print("                                  ", gggs2)
print("                         ", ggd1)
print("                                  ", gggd2)
print("        ", sire)
print("                                  ", gggs3)
print("                         ", ggs2)
print("                                  ", gggd3)
print("                 ", gd1)
print("                                  ", gggs4)
print("                         ", ggd2)
print("                                  ", gggd4)
print(" ")
print(dog)
print(" ")
print("                                  ", gggs5)
print("                         ", ggs3)
print("                                  ", gggd5)
print("                 ", gs2)
print("                                  ", gggs6)
print("                         ", ggd3)
print("                                  ", gggd6)
print("        ", dam)
print("                                  ", gggs7)
print("                         ", ggs4)
print("                                  ", gggd7)
print("                 ", gd2)
print("                                  ", gggs8)
print("                         ", ggd4)
print("                                  ", gggd8)


# HTML Ped

view_html_ped = input("Would you like to view the html ped? y/n ")

if view_html_ped == "y":
    print("""<div class="stretchtable">
         <table>
            <thead>
                <tr>
                  <th scope="col">Gen -1</th>
                  <th scope="col">Gen -2</th>
                  <th scope="col">Gen -3</th>
                  <th scope="col">Gen -4</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td rowspan="8">""" + str(sire) + """</td>
                    <td rowspan="4">""" + str(gs1) + """</td>
                    <td rowspan="2">""" + str(ggs1) + """</td>
                    <td rowspan="1">""" + str(gggs1) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd1) + """</td>
                </tr>
                <tr>
                    <td rowspan="2">""" + str(ggd1) + """</td>
                    <td rowspan="1">""" + str(gggs2) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd2) + """</td>
                </tr>
                <tr>
                    <td rowspan="4">""" + str(gd1) + """</td>
                    <td rowspan="2">""" + str(ggs2) + """</td>
                    <td rowspan="1">""" + str(gggs3) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd3) + """</td>
                </tr>
                <tr>
                    <td rowspan="2">""" + str(ggd2) + """</td>
                    <td rowspan="1">""" + str(gggs4) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd4) + """</td>
                </tr>
                <tr>
                    <td rowspan="8">""" + str(dam) + """</td>
                    <td rowspan="4">""" + str(gs2) + """</td>
                    <td rowspan="2">""" + str(ggs3) + """</td>
                    <td rowspan="1">""" + str(gggs5) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd5) + """</td>
                </tr>
                <tr>
                    <td rowspan="2">""" + str(ggd3) + """</td>
                    <td rowspan="1">""" + str(gggs6) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd6) + """</td>
                </tr>
                <tr>
                    <td rowspan="4">""" + str(gd2) + """</td>
                    <td rowspan="2">""" + str(ggs3) + """</td>
                    <td rowspan="1">""" + str(gggs7) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd7) + """</td>
                </tr>
                <tr>
                    <td rowspan="2">""" + str(ggd4) + """</td>
                    <td rowspan="1">""" + str(gggs8) + """</td>
                </tr>
                <tr>
                    <td rowspan="1">""" + str(gggd8) + """</td>
                </tr>
            </tbody>
        </table>

    </div>""")

