def matched(s):
    mlist = []
    for i in range(0,len(s)):
        if s[i] == "(":
            mlist.append("(")
        elif s[i] == ")":
            if not mlist:
                return False
            else:
                mlist.pop()
    if not mlist:
        return True
    else:
        return False

matched("zb%78")
matched("(7)(a")
matched("a)*(?")
matched("((jkl)78(A)&l(8(dd(FJI:),):)?)")
