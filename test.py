import get_elements as ge

if __name__ == '__main__':
    file_object = open('index.html', 'r')
    page = ''
    try:
        all_the_text = file_object.read()
        page = all_the_text
    finally:
        file_object.close()
    res = ge.getContent(page)
    writer = open('res', 'w+')
    for r in res:
        try:
            writer.write(r[1]+"\n")
        except Exception as e:
            print e
    print res
