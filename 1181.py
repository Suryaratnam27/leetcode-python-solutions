def balloon(text):
    b=text.count("b")
    a=text.count("a")
    l=text.count("l")
    o=text.count("o")
    n=text.count("n")
    return min(b,a,l//2,o//2,n) 
sad=balloon("loonbalxballpoon")
print(sad)
