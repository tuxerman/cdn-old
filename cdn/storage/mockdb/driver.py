# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Storage driver implementation."""

from cdn.common import decorators
from cdn.openstack.common import log as logging
from cdn import storage
from cdn.storage.mockdb import controllers

from oslo.config import cfg

LOG = logging.getLogger(__name__)

MOCKDB_OPTIONS = [
    cfg.StrOpt('database', default='cdn',
               help='Database for all queries made in session')
]

MOCKDB_GROUP = 'drivers:storage:mockdb'


def _connection():
    

    return None


class StorageDriver(storage.StorageDriverBase):

    def __init__(self, conf, providers):
        super(StorageDriver, self).__init__(conf, providers)

        self.conf.register_opts(MOCKDB_OPTIONS,
                                group=MOCKDB_GROUP)
        self.mockdb_conf = self.conf[MOCKDB_GROUP]

    def is_alive(self):
        return True


    @decorators.lazy_property(write=False)
    def connection(self):
        """Connection instance."""
        return _connection()

    @decorators.lazy_property(write=False)
    def service_controller(self):
        return controllers.ServicesController(self)

    @decorators.lazy_property(write=False)
    def service_database(self):
        return self.connection
