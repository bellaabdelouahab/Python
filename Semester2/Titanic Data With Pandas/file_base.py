with open('NFS-315_.sql','r') as base:
    a=base.readlines()
    dataset=[]
    for text in a:
        if ';' not in text:
            if 'REM' not in text:
                dataset.append(text[0:-1])
        else:
            dataset.append(text)
            print(text)
with open('new_dataset','w') as base:
    base.write(''.join(dataset))