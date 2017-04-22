# for i in range(11037):
#     print("R"+str(i))

if __name__ == '__main__':
    count_line = 2;
    list_source = "'Resources-2'"
    cell_orig = "D"
    cell_transl = "C"
    flag_concat_origin = "R2-"
    flag_concat_transl = "R2-"
    for i in range(count_line):
        print(r"=if(len(" + list_source + "!" + cell_transl + str(i) + " > 0;"
              + 'CONCAT("' + flag_concat_origin + str(i) + ': ";' + list_source + '!' + cell_orig + str(i) + ");"
              + 'CONCAT("' + flag_concat_transl + str(i) + ': ";' + list_source + '!' + cell_orig + str(i) + "))")

        # no id

        # + list_source + "!" + cell_transl + str(i) + "; "

        # patterns

        # =if(len('Resources-2'!E63) > 0;'Resources-2'!E63; CONCAT("R2-63: ";'Resources-2'!C63))
        # print(r'=if(len(' + list_source + '!' + cell_orig + str(i) + ") > 0;\"\";" + list_source + "!" + cell_transl + str(i) + ")")
        # print(r"=if(len('Resources-2'!D" + str(i) + ") > 0;\"\"; 'Resources-2'!C" + str(i) + ")")
