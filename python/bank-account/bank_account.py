from threading import Lock

class BankAccount(object):

    def __init__(self):
      self.is_open=False
      self.balance=0

    def account_is_open(func):
      def wrapped(self,*args):
        if self.is_open is not True:
          raise ValueError("Account is not open")
        return func(self,*args)
      return wrapped

    def thread_lock(lock):
      def wrapper(func):
        def wrapped(self, *args):
          with getattr(self,lock):
            return func(self,*args)
        return wrapped
      return wrapper

    def with_lock(lock):
        def wrapper(func):
            def wrapped(self, *args):
                with getattr(self, lock):
                    return func(self, *args)
            return wrapped
        return wrapper

    @account_is_open
    def get_balance(self):
      return self.balance

    def open(self):
      self.is_open=True
      self.balance = 0
      self.lock = Lock()

    @account_is_open
    @thread_lock('lock')
    def deposit(self, amount):
      if self.is_open and amount >0 :
        self.balance += amount
      else:
        raise ValueError("Transaction not valid")

    @account_is_open
    @thread_lock('lock')
    def withdraw(self, amount):
      if self.is_open and amount <= self.balance and amount > 0:
        self.balance -= amount
      else:
        raise ValueError("Transaction not valid")

    @account_is_open
    @thread_lock('lock')
    def close(self):
        self.is_open = False
