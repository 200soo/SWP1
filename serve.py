WSGIScriptAlias /calc /GIT/SWP1/a.py
WSGIPythonPath /GIT/SWP1

<Directory "/GIT/SWP1">
    AllowOverride None
    Order deny,allow
    Require all granted
</Directory>
