import subprocess, os
args = ["~/test.sh"]
result = subprocess.Popen(args, shell=True, start_new_session=True, text=True, stdout=subprocess.PIPE, cwd=os.path.expanduser("~"))  # If cwd is not set in the flatpak /app/bin/StreamController cannot be found

print(result.communicate()[0].rstrip())