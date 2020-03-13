# remote_worker
Remote Windows Computer Worker

Use this file as a template to run code on the remote Windows computer, you have access to via LAN.
main_file.py copies remote_runnet.pyw to remote machine and runs it there using pypsexec client.
Client runs in interactive session, i.e., it may run cmd commands, and iterate with GUI objects, like buttons, etc.
