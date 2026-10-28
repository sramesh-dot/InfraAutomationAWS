
import boto3


def generate_ec2_report(region="ap-southeast-2"):
    ec2 = boto3.client("ec2", region_name=region)

    response = ec2.describe_instances(
        Filters=[
            {
                "Name": "tag:Project",
                "Values": ["aws-python-terraform-jenkins"],
            }
        ]
    )

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instances.append({
                "instance_id": instance["InstanceId"],
                "state": instance["State"]["Name"],
            })

    print(f"\nTotal project instances found: {len(instances)}")

    for instance in instances:
        print(
            f"Instance ID: {instance['instance_id']}, "
            f"State: {instance['state']}"
        )

    return instances


if __name__ == "__main__":
    generate_ec2_report()
