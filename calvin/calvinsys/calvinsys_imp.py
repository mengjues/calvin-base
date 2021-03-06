# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import events as calvin_events
import io as calvin_io
import network as calvin_network

class CalvinSys(object):

    """CalvinSys is the interface to the calvin runtime for the actor"""

    def __init__(self, node):
        super(CalvinSys, self).__init__()
        self._node = node
        self.events = calvin_events.Events(node)
        self.io = calvin_io.Io(node)
        self.network = calvin_network.Network(node)
        # TODO add the storage subsystems
