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

"""Fastly CDN Provider implementation."""

from cdn.common import decorators
from cdn.openstack.common import log as logging
from cdn import provider
from cdn.provider.fastly import controllers

from oslo.config import cfg

import fastly

LOG = logging.getLogger(__name__)

FASTLY_OPTIONS = [
    cfg.StrOpt('apikey', help='Fastly API Key'),
]

FASTLY_GROUP = 'drivers:provider:fastly'


class CDNProvider(provider.CDNProviderBase):

    def __init__(self, conf):
        super(CDNProvider, self).__init__(conf)

        self.conf.register_opts(FASTLY_OPTIONS,
                                group=FASTLY_GROUP)
        self.fastly_conf = self.conf[FASTLY_GROUP]

        self.client = fastly.connect(self.fastly_conf.apikey)


    def is_alive(self):
        return True

    def client(self):
        return self.client

    @decorators.lazy_property(write=False)
    def service_controller(self):
        return controllers.ServiceController(self)
