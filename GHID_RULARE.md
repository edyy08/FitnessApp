## Pasi (Windows, PowerShell), pentru fiecare piesa
1. Extract la arhiva
2. In folderul unde se gaseste 'run_piesa.py" se scrie in bara de sus 'powershell'
3. Se executa pe rand comenzile:
       python -m venv .venv
       Set-ExecutionPolicy -Scope Process RemoteSigned
       .venv\Scripts\activate
       pip install -r requirements.txt
4. Pornire:
       python run_piesa1.py               (EX)
