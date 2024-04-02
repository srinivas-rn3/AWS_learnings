import boto3

def lambda_handler(event, context):
    # Specify EC2 parameters
    instance_type = 't2.micro'
    ami_id = 'your-ami-id'
    key_name = 'your-key-pair-name'
    security_group_ids = ['your-security-group-id']

    # Create EC2 client
    ec2 = boto3.client('ec2')

    # Launch EC2 instance
    response = ec2.run_instances(
        ImageId=ami_id,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroupIds=security_group_ids,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    print(f'Instance {instance_id} launched successfully.')
'''
Remember to replace 'your-ami-id', 'your-key-pair-name', 
and 'your-security-group-id' with your actual values.

'''