from language import Language

if __name__ == "__main__":
    vt = ['a', 'b', '$']
    vn = ['S', 'A', 'B', 'C']
    p = {
        'S': ['C$'],
        'C': ['Abb', 'Ba'],
        'Ab': ['a', 'Ca'],
        'B': ['b', 'Cb']
    }
    s = 'S'
    lang = Language(vt, vn, p, s)

    print(lang.get_kind())