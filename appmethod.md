# Internal Docs for imports and methods

- Flask
- render_template
- request
- url_for

## Python Vitual Environment

Install with pip or pip3  
`pip3 install virtualenv`  
Create env  
`virtualenv venv --python=python3.6`  
Start env  
`source venv/bin/activate`  
Stop env  
`deactivate`  
List installed package and libraries
`pip freeze`

### Secret Tokens

``` python
import secrets
secrets.token_hex(16)
'6dfed00d10b6d7034c0ebff2972bd97d'
```

