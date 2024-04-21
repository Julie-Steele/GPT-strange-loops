with open(__file__, "r+") as f:

    lines = f.readlines() + ["#counter"]
    f.seek(0)
    f.writelines(lines)
    f.truncate()

#counter#counter