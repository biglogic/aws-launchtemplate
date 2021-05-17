import boto3 

session=boto3.Session(profile_name="atul",region_name='us-east-1')
client = session.client('ec2')
response = client.describe_launch_templates()
print(response)
print(response['LaunchTemplates'][0]['LatestVersionNumber'])
describe=client.describe_launch_template_versions(LaunchTemplateId=response['LaunchTemplates'][0]['LaunchTemplateId'],
 Versions=[
        str(response['LaunchTemplates'][0]['LatestVersionNumber']),
    ])
print(describe)
response2 = client.create_launch_template_version(
    LaunchTemplateId=response['LaunchTemplates'][0]['LaunchTemplateId'],
    SourceVersion=str(response['LaunchTemplates'][0]['LatestVersionNumber']),
    LaunchTemplateData={
        'EbsOptimized': False,
        'BlockDeviceMappings': [
            {
                'Ebs': {
                    'Encrypted': False,
                    'DeleteOnTermination': True,
                    'VolumeSize': 123,
                    'VolumeType': 'standard',
                     }
                
            },
        ],
        'ImageId': 'ami-0d5eff06f840b45e9',
        'InstanceType': 't2.large',
        'KeyName': 'Name',
        'Monitoring': {
            'Enabled': True
            },
        'Placement': {
            'AvailabilityZone': 'us-east-1',
            }        
    }
)