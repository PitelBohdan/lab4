import boto3

def get_public_ip(instance_id):
    ec2 = boto3.client('ec2', region_name='us-east-1')

    response = ec2.describe_instances(InstanceIds=[instance_id])

    public_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']

    return public_ip

# Виклик функції та отримання публічної IP-адреси
instance_id = 'i-04a6a97535c71f551'
public_ip = get_public_ip(instance_id)

print(f"Public IP: {public_ip}")
