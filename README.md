# python-project-template

This is a simple python project template for Visual studio code. 

Create and activate virtual environment:

   ```sh
   python -m venv .venv
   ```
   ```sh
   "./.venv/Scripts/activate"
   ```
   
Clear git cached files and directories:

   ```sh
   git rm --cached -r .vscode 
   ```
   ```sh
   git rm --cached .env
   ```
    
Set path to project root directory in `.env`, e.g.:

   ```sh
   PYTHONPATH=C:\\Users\\janezla\\Documents\\python-project-template
   ```
