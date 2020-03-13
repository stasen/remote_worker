from pypsexec.client import Client
from os.path import join, isdir
from shutil import copytree, rmtree


class Worker:
    def __init__(self):
        self.copy_worker()
        
    def copy_worker(self):
        """
        Copy remote_runner.pyw to remote PC
        """
        if isdir("directory/to/destination"): rmtree("directory/to/destination")
        copytree("directory/to/source", "directory/to/destination")

    def send_command(self, command):
        """
        Send command to remote mechine using pypsexec client
        """
        c = Client("remote_machine_ip", username="remote_machine_username", password="remote_machine_password")
        c.connect()
        c.create_service()
        py_exe = r"C:\Python38\pythonw.exe"
        arguments = join('c:\\', 'remote', 'file', 'path', 'remote_runner.pyw')
        arguments = arguments + " " + '-c' + " " + command
        c.run_executable(py_exe, arguments=arguments, interactive=True,
                                              interactive_session=1, run_elevated=True, use_system_account=True)
        c.remove_service()
        c.disconnect()
        