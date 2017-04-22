# for i in range(11037):
#     print("R"+str(i))

if __name__ == '__main__':
    count_line = 24992;
    list_source = "'events'"
    cell_orig = "C"
    cell_transl = "D"
    flag_concat_origin = "Eo-"
    flag_concat_transl = "Et-"
    for i in range(count_line):
        # print("E" + str(i))
        print(r"=if(len(" + list_source + "!" + cell_transl + str(i) + ") > 0;"
              + 'CONCAT("' + flag_concat_transl + str(i) + ': ";' + list_source + '!' + cell_transl + str(i) + ");"
              + 'CONCAT("' + flag_concat_origin + str(i) + ': ";' + list_source + '!' + cell_orig + str(i) + "))")

        # no id

        # + list_source + "!" + cell_transl + str(i) + "; "

        # patterns

        # =if(len('Resources-2'!E63) > 0;'Resources-2'!E63; CONCAT("R2-63: ";'Resources-2'!C63))
        # print(r'=if(len(' + list_source + '!' + cell_orig + str(i) + ") > 0;\"\";" + list_source + "!" + cell_transl + str(i) + ")")
        # print(r"=if(len('Resources-2'!D" + str(i) + ") > 0;\"\"; 'Resources-2'!C" + str(i) + ")")
