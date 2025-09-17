from google.colab import userdata
import os

github_token = userdata.get('Git_Key')
owner = 'Penn2001' # Replace with the GitHub repository owner
repository = 'MSSP-607' # Replace with the GitHub repository name

clone_url = f'https://{github_token}@github.com/{owner}/{repository}.git'

# Clone the repository
import subprocess
subprocess.run(['git', 'clone', clone_url])

# Navigate into the cloned repository directory (optional, but often useful)
os.chdir(repository)
print(f"Changed directory to: {os.getcwd()}")
