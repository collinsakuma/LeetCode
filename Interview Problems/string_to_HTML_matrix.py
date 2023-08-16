class Solution:
    def string_to_matrix(input):
        list = input.split(";")
        header_column = [""]
        list.pop(-1)
        for i in range(len(list)):
            list[i] = list[i].split(":")
            header_column.append(list[i].pop(-1)[1:])
            list[i] = list[i][0].split(",")

        # rows = [[] for _ in range(len(list[0]) // (len(header_column) - 1))]
        rows = []
        count = 0
        for i in list:
            rows.append(i[:(len(header_column) - 1)])


        print(rows)
        # print(header_column)
        # print(list)





# # # # Test Case # # # #

test_input = "5,100,5.5,110,6,102:L10;5,101,5.5,103,6,120:L20;"

Solution.string_to_matrix(test_input)