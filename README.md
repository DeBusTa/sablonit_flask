# API on Cloud Compute Engine
### 1. Flask server using Python Language

- Save the model in the same directory as `main.py` in `'.h5'` format.
- In `main.py`, load the model and write Flask code.
- Run `main.py` to test the Flask server locally, then copy the local URL assigned to postman for image testing.
- Choose **POST** for HTTP Request, click form-data in Body and then field the key and choose image file

### 2. Setup VM in Google Cloud Platform
- Create a Virtual Machine (VM) on Google Compute Engine 
- Select `debian-10-tf-2-4-1-v20210412` as the boot disk
- Select Management, security, disks, networking, sole tenancy
- Choose Networking tab -> name network tag `deploy`
- Create a firewall with the same network tag as the VM.

### 3. Setup VM for Machine Learning Model
- Run SSH on created VM
- Upload your model to the VM or clone it through Git
- Install Flask in VM with command : `pip install flask`
- Run `main.py` with command : `python3 main.py`

