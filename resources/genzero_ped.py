dog = "POW Bulldog's Gen Zero"
pedigree_dogs = [["BDB's Koba"], ["IWK's Dagny"], ["BDB's Smoke"], ["BDB's Leye Leye"], ["Garner's Tramp Red Boy"], ["Garner's Ginger"], ["Impala Kennel's Deuce"], ["Patrick's Lisa"], ["AZ Heat's Blue"], ["AZ's Buttercup"], ["Cottingham's Redman"], ["Garner's Gloria"], ["Cottingham's Redman"], ["Garner's Gloria"], ["Latin Force Kennel's Baracuda"], ["Southern Kennel's Yellow Girl II"], ["Patrick's Rabbit"], ["Patrick's Wyatti"], ["Cooper's Amboss"], ["Patrick's Lisa"], ["BDB's Butterbean"], ["Maxey's Katelynn"], ["Cottingham's Boomer"], ["Cottingham's Ginger"], ["Cottingham's Redman"], ["Garner's Little Cherry"], ["Cottingham's Boomer"], ["Cottingham's Ginger"], ["Cottingham's Redman"], ["Garner's Little Cherry"]]

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


# Print ped
# #################################################################
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


# Print HTML ped
# #################################################################
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
