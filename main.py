import respgen

# before running, using os.environ, specify os.environ['ACCESS_ID'] = 'your id',  os.environ['ACCESS_KEY'] = 'your secret'
# imgurl='https://upload.wikimedia.org/wikipedia/commons/7/7e/1993ToyotaMR2Hardtop.jpg'
# imgurl2='https://upload.wikimedia.org/wikipedia/commons/1/13/Red_2019_Ferrari_SF90_Stradale_%2848264238897%29_%28cropped%29.jpg'

def main():
    imgurl = input('Enter the image URL: ')
    testlabel = input('Enter keyword label: ')
    print('Labels generating...')
    try:
        respgen.generate_data(imgurl, 'URL' if 'http' in imgurl else 'LOCAL' )
    except:
        print("")
    return testlabel.lower()
