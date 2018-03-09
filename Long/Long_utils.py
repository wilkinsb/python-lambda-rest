"""Long_utils.py

Use this file for AWS connections, AWS interactions or Database connection/interaction.
Basically anything we need to call using an outside API (Boto3 package, Postgres DB)

As the application is built, edit this docstring to provide more information
"""
import boto3

import config

# Take an unknown number of keywords as args
def get_user_data(**kwargs):
    """
    Retrieve the user-data script that will be used to bootstrap
    ec2 workers.
    """

    user_data_template = """#!/bin/bash
set -x
set -v -v -v -v
set -e # exit if any command fails
# The following line gets replaced by Long/api.py  with
# environment variable definitions.
# __ENVIRONMENT_VARIABLE_DEFS__
# After the replacement happens, there should be
# environment variables exported called:
# ARG1, ARG2

. /envs/wenv/bin/activate

# terminate self after 55 minutes- safety precaution
echo "sudo halt" | at now + 55 minutes

# run script
cd /python-lambda/Long
python task.py
    """
    string_to_replace = "# __ENVIRONMENT_VARIABLE_DEFS__"
    replacement_string = ""
    for key, value in kwargs.items():
        replacement_string += "export {}=\"{}\"\n".format(
            key.upper(), value
        )
    user_data = user_data_template.replace(string_to_replace,
                                           replacement_string)
    return user_data

def find_image(region):
    """
    Finds the latest GeMS Worker AMI and return its ID.
    based on
    https://gist.github.com/robert-mcdermott/a9901aaafe208a6eb76e0fc3b9fc47c9
    """
    ec2 = boto3.resource('ec2', region_name=region)
    images = ec2.images.filter(
        Owners=['self'],
        Filters=[
            {'Name': 'tag:Type', 'Values': [
                'Long Task AMI']},
            {'Name': 'state', 'Values': ['available']}
        ]
    )
    candidates = {}
    for image in images:
        candidates[image.creation_date] = image.image_id
    cdate = sorted(candidates.keys(), reverse=True)[0]
    ami = candidates[cdate]
    return ami

def start_instances(user_data, env, ami_id):
    """
    Start all EC2 instances.
    """
    # Make sure env variables are all UPPER
    # env is not used here, but could be and is used when dynamocally allocating instance #
    # or other things that could be dynamic
    env0 = {}
    for key, value in env.items():
        env0[key.upper()] = value

    env = env0

    client = boto3.client('ec2', region_name="us-west-2")
    arn = 'arn:aws:iam::7########6:instance-profile/task-iam-user'

    response = client.run_instances(
        ImageId=ami_id,
        MinCount=1,
        MaxCount=1,
        KeyName=config.KEY_NAME,
        SecurityGroupIds=['sg-id'],
        UserData=user_data,
        InstanceType='t2.nano', 
        IamInstanceProfile={'Arn': arn},
        InstanceInitiatedShutdownBehavior='terminate'
    )
    instance_ids = [x['InstanceId'] for x in response['Instances']]
    reservation_id = response['ReservationId']

    return dict(instances_ids=instance_ids, reservation_id=reservation_id)


