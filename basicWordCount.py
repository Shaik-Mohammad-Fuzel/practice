text="i like red color, but my father doesnot like red color , he likes yellow in color"
a={}
def wordcount(text):
    w=text.strip('.').split()
    for i in w:
        w=i.strip(',')
        if w not in a:
            a[w]=1
        else :
            a[w]+=1
    print(a)
wordcount(text)
            
