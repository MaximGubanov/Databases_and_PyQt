from setuptools import setup, find_packages

setup(name="py_messenger_client_by_maxg",
      version="0.1.1",
      description="Messenger Client",
      author="IMaximGubanov",
      author_email="max.gubanov@vk.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )