import boto3, json
import image_helpers

def generate_data(url, flag):
    try:
        client = boto3.client('rekognition', region_name='us-east-1')
        imgbytes = image_helpers.get_image_from_url(url) if flag == 'URL' else image_helpers.get_image_from_file(url)
        rekresp = client.detect_labels(Image={'Bytes': imgbytes})
        with open('data.json', 'w') as f:
            f.write(json.dumps(rekresp))
    except Exception as e:
        print(e)