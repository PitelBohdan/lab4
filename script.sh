#!/bin/bash

instance_id="i-04a6a97535c71f551"

public_ip=$(aws ec2 describe-instances --instance-ids "$instance_id" --region us-east-1 --query 'Reservations[].Instances[].PublicIpAddress' --output text)

echo "Public IP: $public_ip"
