m_list = set()
m = int(input('kol-vo knig h:'))
n_list = set()
n = int(input('kol-vo knig s:'))

for q in range(m):
    book = (input('h_book:'))
    m_list.add(book)
for w in range(n):
    book = (input('s_book:'))
    n_list.add(book)

    if book in m_list:
        print('y')
    else:
        print('n')
