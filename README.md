# local airflow setup

## Step 1: Set up Kubernetes
1. Open Docker and go to Settings > Kubernetes. 
2. Select the Enable Kubernetes checkbox. 
3. Click Apply and Restart. 
4. Click Install in the Kubernetes Cluster Installation dialog.

    Docker restarts and the status indicator changes to green to indicate Kubernetes is running.
## Step 2: Update the kubeconfig file
1. Update [config](/include/.kube/config) file.
   1. Update the `<certificate-authority-data>`, `<client-certificate-data>`, and `<client-key-data>` values in the config file with the values for your organization. Which is present at `$HOME/.kube/config`.
## Run your container.
1. To start service `astro dev start` and to stop service `astro dev stop`
   1. Now go to http://localhost:8080/
   
Note: `image_pull_policy` in KubernateDagOperator should be `Never` else dag will start looking docker image at Docker Hub.

## You are all set :clap: :clap:

### Update [Dag image](./dags/test.py) and cmd based on you Dag-job

### Astro [Ref](https://docs.astronomer.io/software/kubepodoperator-local)
