"""MongoDB Storage Driver for CDN"""

from cdn.storage.cassandra import driver

# Hoist classes into package namespace
StorageDriver = driver.StorageDriver
