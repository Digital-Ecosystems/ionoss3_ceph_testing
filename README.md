# ionoss3_ceph_testing

This script aims to display the timing of the availabilty of a IONOS S3 key using the new [S3 Management API](https://api.ionos.com/docs/s3-management/v1/).

## Iteration Results
Command to run the test: 
```bash
python3 IonosS3_Ceph_Testing.py
```
Bellow we have an example of a list of timings. For each iteration, we are:
- creating the S3 key;
- checking the S3 key availability;
- removing the S3 key.

The time is obtained using the availability timestamp minus the creation timestamp of the S3 key.

| Iteration | Time Difference (seconds) |
|-----------|---------------------------|
| 1/10      | 13.589043                 |
| 2/10      | 8.306913                  |
| 3/10      | 9.476576                  |
| 4/10      | 8.570000                  |
| 5/10      | 9.712359                  |
| 6/10      | 14.781061                 |
| 7/10      | 11.999958                 |
| 8/10      | 8.100124                  |
| 9/10      | 9.589218                  |
| 10/10     | 9.397787                  |

