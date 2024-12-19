text="i like red color , but my father doesnot like red color , he likes yellow in color"
a={}
def wordcount(text):
    w=text.split()
    for i in w:
        if i not in a:
            a[i]=1
        else :
            a[i]+=1
    print(a)
wordcount(text)
            
