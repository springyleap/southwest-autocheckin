#from azure.mgmt.storage import StorageManagementClient
from azure.storage.queue import QueueService

class CheckinQueueClient(object):
    """Obtains next checkin object from queue"""
    queueName = 'checkinqueue'
    
    def __init__(self, account_name, account_key):
        self._queueService = QueueService(account_name, account_key)

    def startCheckinProcess(processData):
        while(True):
            message = self._queueService.get_messages(queueName,  num_messages=1, visibility_timeout=30)
            processData(message)