# Task 3: Lost Data Retrieval (Digital Forensics)

## Objective
To simulate a data loss scenario and successfully recover "permanently" deleted files from a storage device.

## Tools Used
* Windows Disk Management (to create a virtual test environment)
* Recuva (for data recovery)

## Steps Taken
1. **Environment Setup:** Created a 500MB Virtual Hard Disk (VHD) to simulate a USB drive.
2. **Data Creation:** Created a file named `Secret_Treasure` on the drive.
3. **The Deletion:** Used `Shift + Delete` to bypass the Recycle Bin and permanently delete the file.
4. **The Recovery:** Ran a scan using Recuva on the virtual drive. The tool successfully identified the deleted file clusters.
5. **The Result:** Successfully restored the file to the Desktop.

## Evidence
(I have uploaded the screenshots of this process to this folder.)
