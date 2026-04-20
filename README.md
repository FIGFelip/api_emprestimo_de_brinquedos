# DDD_template
Template para projetos DDD com Python

### Linux/MacOS setup
```
    python3 -m venv .venv
    source .venv/bin/activate

```

### Windows setup
```
    python -m venv .venv
    
    venv\Scripts\activate.bat (se cmd.exe) - Recomendado
    ou
    venv\Scripts\Activate.ps1 (se PowerShell)
```

### instalando bibliotecas
```pip install <biblioteca(s)>```

### Criando requirements.txt e uninstall.txt

``` 
    pip freeze requirements.txt
    pip freeze uninstall.txt    
```
### Importante
Lembrar de adicionar qualquer arquivo sensível ao .gitignore
