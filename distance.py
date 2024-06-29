import streamlit as st
'''4. Khoảng cách Levenshtein.
Viết chương trình tính khoảng cách chỉnh sửa tối thiểu Levenshtein.'''


def levenshtein_distance(source, target):
    """
    Disc:
        Bước 1: Xây dựng ma trận lưu trữ có số hàng là M và số cột là N. Trong đó M là số lượng
  các ký tự trong từ source + 1, N là số lượng các ký tự trong từ target + 1. Vì vậy với ví dụ
  'yu' và 'you', ta có ma trận được biểu diễn như hình 1. Ký hiệu '#' đại diện cho chuỗi rỗng.
  Gọi là ma trận D.
        Bước 2: Hoàn thiện hàng và cột đầu tiên. Với hàng đầu tiên, các giá trị đại diện cho chuỗi
bắt đầu là chuỗi '#' và phép biến đổi là thêm (insert) từ chuỗi '#' thành '#', '#y', '#yo',
'#you' lần lượt là 0, 1, 2, 3 tương ứng với ô D[0, 0], D[0, 1], D[0, 2], D[0, 3]. Với cột đầu tiên,
các giá trị đại diện cho chuỗi '#', '#y', '#yu' và phép biến đổi là xoá (delete) để thu được
chuỗi '#' lần lượt là: 0, 1, 2 tương ứng với ô D[0, 0], D[1, 0], D[2, 0]. Ta được hình 2.
        Bước 3. Tính toán các giá trị với các ô còn lại trong ma trận.
        Bước 4: Sau khi hoàn thành ma trận, chúng ta đi tìm đường đi từ ô cuối cùng D[2, 3] có giá
trị là 1. Vì vậy khoảng cách chỉnh sửa từ source: 'yu' sang thành target: 'you' là 1. Đầu tiên
ký tự 'y' giữ nguyên sau đó thực hiện 1 phép thêm ký tự 'o' vào sau ký tự 'y' và cuối cùng
ký tự 'u' được giữ nguyên.
    Args:
        source là từ cần thay đổi
        target là từ sau khi thay đổi
    Raises:

    Prompts:
        nhập từ cần thay đổi = source
        nhập từ sau khi thay đổi = target
    Returns:

    """

    # step 1: create 2d matrix d with m rows and n cols
    m_rows = len(source) + 1
    n_cols = len(target) + 1
    d_matrix = [[0]*n_cols for _ in range(m_rows)]

    # step 2: first col and first row, insert target and delete source

    for c in range(n_cols):
        d_matrix[0][c] = c
    for r in range(m_rows):
        d_matrix[r][0] = r

    # step 3: calculate remain value
    for r in range(1, m_rows):
        for c in range(1, n_cols):
            if min(d_matrix[r][0], d_matrix[0][c]) == 0:
                d_matrix[r][c] = max(d_matrix[r][0], d_matrix[0][c])
            else:
                sub_cost = 0
                if source[r - 1] == target[c - 1]:
                    sub_cost = d_matrix[r - 1][c - 1]
                else:
                    sub_cost = d_matrix[r - 1][c - 1] + 1
                d_matrix[r][c] = min(d_matrix[r][c - 1] + 1,
                                     d_matrix[r - 1][c] + 1, sub_cost)

    # step 4: print distance
    # for index in range(m_rows):
    #     print(d_matrix[index])
    # print(f"Distance: {d_matrix[m_rows - 1][n_cols - 1]}")
    return d_matrix[m_rows - 1][n_cols - 1]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

        words = sorted(set([line.strip().lower() for line in lines]))
        return words


vocabs = load_vocab(file_path="./source/vocab.txt")

st.title('Word Correction')
word = st.text_input("Your word")

if st.button("Compute"):
    distances = dict()
    for vocab in vocabs:
        distace = levenshtein_distance(word, vocab)
        distances[vocab] = distace

    sorted_distances = dict(
        sorted(distances.items(), key=lambda item: item[1]))
    correct_words = list(sorted_distances.keys())[0]
    st.write('Correct:', correct_words)
