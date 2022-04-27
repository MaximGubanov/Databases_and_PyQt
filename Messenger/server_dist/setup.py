from setuptools import setup, find_packages

setup(name="py_messenger_server_by_maxg",
      version="0.1.1",
      description="Messenger Server",
      author="MaximGubanov",
      author_email="max.gubanov@vk.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      # scripts=['server/server_run']
      )