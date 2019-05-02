# Copyright (c) 2019 Jannika Lossner
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from .base import _Base

from .. import _data as data
from .. import _rooms as rooms

class SingleRoomDRIR(_Base):
    name = "SingleRoomDRIR"
    version = "0.3"
    def __init__(self):
        _Base.__init__(self)
        self.default_objects["Source"]["coordinates"].View = [-1,0,0]
        self.default_objects["Emitter"]["count"] = 1

        self.conditions["must have 1 Emitter"] = lambda name, info_states, count: name != "Emitter" or count == 1
        self.conditions["must have Listener Up and View)"] = lambda name, info_states, count: name != "Listener" or (not data.spatial.Coordinates.State.is_used(info_states.Up))
        self.conditions["must have Source Up and View)"] = lambda name, info_states, count: name != "Source" or (not data.spatial.Coordinates.State.is_used(info_states.Up))

    def add_metadata(self, dataset):
        _Base.add_general_defaults(dataset)

        dataset.SOFAConventions = self.name
        dataset.SOFAConventionsVersion = self.version
        dataset.DataType = "FIR"
        dataset.RoomType = rooms.types.Reverb.value
        return

    def set_default_spatial_values(self, spobj):
        _Base._set_default_spatial_values(self, spobj)
        return