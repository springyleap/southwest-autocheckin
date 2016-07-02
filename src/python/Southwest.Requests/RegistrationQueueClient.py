from azure.storage.queue import QueueService

class RegistrationQueueClient(object):
    """Obtains next registration object from queue"""
    queueName = 'registrationsqueue'

    def __init__(self, account_name, account_key):
        self._queueService = QueueService(account_name, account_key)
        print("RegistrationQueue Initialized")

    def LookupTicket(self, processData):
        message = self._queueService.get_messages(self.queueName, num_messages=1)
        if(processData(message)):
            self._queueService.delete_message(self.queueName, message.message_id, message.pop_receipt)



