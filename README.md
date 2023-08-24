# PlusOne Task

## Local Setup using WSL:

1. Clone repo  
  ```
git clone https://github.com/khaled5321/plusone.git
```
3. Install Odoo from source  
    a. Clone Odoo repo  
    ```
   git clone https://github.com/odoo/odoo.git -b 16.0 --depth=1
    ```  
    b. Create a virtual environment  
    ```
    python -m venv venv
    ```
    c. Activate virtual environment
    ```
    source ./venv/bin/activate
    ```
    d. Install requirements
    ```
    pip install -r ./odoo/requirements.txt
    ```
    e. Install odoo
    ```
    pip install -e ./odoo
    ```  
4. Run Odoo with the new module
   ```
   odoo --addons-path="./plusone,./odoo/addons" -d database -i my_module
   ```
