import boto
import os
from django.conf import settings
from django.http import JsonResponse, HttpResponse
boto.pyami.config.Config(path="C:/Users/Administrator/Downloads/boto.config")
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
client = boto3.client('rekognition')
client=boto3.client('rekognition')
   

def brain(img2):
	imageSource = open(os.path.join(settings.VEHICLE_DIR, 'img1.jpg'), 'rb')

	imageTarget = open(os.path.join(settings.VEHICLE_DIR, img2), 'rb')

	response=client.compare_faces(SimilarityThreshold=80,
									SourceImage={'Bytes': imageSource.read()},
									TargetImage={'Bytes': imageTarget.read()})
		
	for faceMatch in response['FaceMatches']:
		position = faceMatch['Face']['BoundingBox']
		similarity = str(faceMatch['Similarity'])
		print(similarity + '% confidence')
		

	imageSource.close()
	imageTarget.close()     
	response = client.detect_faces(
		Image={
			'Bytes':open(os.path.join(settings.VEHICLE_DIR, img2),'rb').read()
			
		},
		Attributes=[
			'DEFAULT',
		]
	)
	len(response['FaceDetails'])
	
	response['FaceDetails'][0]['Pose']
	return HttpResponse("asd")
