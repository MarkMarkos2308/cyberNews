import subprocess
import webbrowser

webbrowser.open('http://127.0.0.1:8000/')

cmd = 'python manage.py runserver'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
result = p.communicate()[0]
print(result)


