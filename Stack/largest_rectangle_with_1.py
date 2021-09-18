""" Finding the Largest Rectangular Area With ALl 1s: We are given a binary matrix and our job is to find the largest
    rectangular sub-matrix in this """

from largest_rectangular_area import rec_area


def largest_sub_matrix(og_mat):
    res = 0
    for i in range(len(og_mat)):
        for j in range(len(og_mat[i])):
            if og_mat[i][j] == 0:
                continue
            else:
                row = i
                col = j
                while row < len(og_mat) and og_mat[row][j] != 0:
                    row += 1
                while col < len(og_mat[i]) and og_mat[i][col] != 0:
                    col += 1
                row = row - 1
                col = col - 1
                i2 = i+1
                j2 = j
                while j2 <= col:
                    if i2 > row:
                        sub_mat = (row - i + 1) * (col - j + 1)
                        res = max(res, sub_mat)
                        break
                    if og_mat[i2][j2] == 0:
                        i2 = i2 - 1
                        sub_mat = (row - i2 + 1) * (col - j + 1)
                        res = max(res, sub_mat)
                        break
                    if j2 == col:
                        j2 = j
                        i2 += 1
                    else:
                        j2 += 1
    return res


""" We consider the columns as bins of the histogram to use the rectangular area code. If the matrix value is 1 we 
    add the result of prev row """


def rec1(og_mat):
    res = rec_area(og_mat[0])
    for i in range(1, len(og_mat)):
        for j in range(len(og_mat[i])):
            if og_mat[i][j] == 1:
                og_mat[i][j] += og_mat[i-1][j]
        res = max(res, rec_area(og_mat[i]))
    return res


def main():
    arr_input = [[0, 1, 1, 0],
                 [1, 1, 1, 1],
                 [1, 1, 1, 1],
                 [1, 1, 0, 0]]
    print(rec1(arr_input))


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
