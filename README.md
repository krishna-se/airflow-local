# local airflow setup

## Step 1: Set up Kubernetes
1. Open Docker and go to Settings > Kubernetes. 
2. Select the Enable Kubernetes checkbox. 
3. Click Apply and Restart. 
4. Click Install in the Kubernetes Cluster Installation dialog.

    Docker restarts and the status indicator changes to green to indicate Kubernetes is running.
## Step 2: Update the kubeconfig file
1. Update [config](/include/.kube/config) file.
   1. Update `certificate-authority-data` under `-cluster` and `client-key-data` under `-user` based on your system kube config `$HOME/.kube/config`.

## Run your container.
1. To start service `astro dev start` and to stop service `astro dev stop`
   1. Now go to http://localhost:8080/
   
## You are all set :clap: :clap:

### Update [Dag image](./dags/test.py) and cmd based on you Dag-job

### Astro [Ref](https://docs.astronomer.io/software/kubepodoperator-local)
