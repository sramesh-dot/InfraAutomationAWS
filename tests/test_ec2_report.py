
import unittest
from unittest.mock import patch

from ec2_report import generate_ec2_report


class TestEC2Report(unittest.TestCase):

    @patch("ec2_report.boto3.client")
    def test_returns_matching_instances(self, mock_boto_client):
        mock_ec2 = mock_boto_client.return_value

        mock_ec2.describe_instances.return_value = {
            "Reservations": [
                {
                    "Instances": [
                        {
                            "InstanceId": "i-test123",
                            "State": {"Name": "running"},
                        },
                        {
                            "InstanceId": "i-test456",
                            "State": {"Name": "stopped"},
                        },
                    ]
                }
            ]
        }

        result = generate_ec2_report()

        self.assertEqual(len(result), 2)
        self.assertEqual(result[0]["instance_id"], "i-test123")
        self.assertEqual(result[0]["state"], "running")
        self.assertEqual(result[1]["instance_id"], "i-test456")
        self.assertEqual(result[1]["state"], "stopped")

        mock_boto_client.assert_called_once_with(
            "ec2", region_name="ap-southeast-2"
        )

        mock_ec2.describe_instances.assert_called_once_with(
            Filters=[
                {
                    "Name": "tag:Project",
                    "Values": ["aws-python-terraform-jenkins"],
                }
            ]
        )

    @patch("ec2_report.boto3.client")
    def test_returns_empty_list_when_no_instances_match(
        self, mock_boto_client
    ):
        mock_ec2 = mock_boto_client.return_value

        mock_ec2.describe_instances.return_value = {
            "Reservations": []
        }

        result = generate_ec2_report()

        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
