def libraryFine(d1, m1, y1, d2, m2, y2):
    y_diff=y1-y2
    m_diff=m1-m2
    d_diff=d1-d2
    if y_diff >= 1:
        return 10000 * y_diff
    elif m_diff >= 1 and y_diff == 0:
        return 500 * m_diff
    elif d_diff >= 1 and m_diff == 0 and y_diff == 0:
        return 15 * d_diff
    else:
        return 0